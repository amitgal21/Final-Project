from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk

# global variable of initScreen
global root, usernameEntry, passwordEntry, openEye, closeEye, eyeButton, loginWindow
# global Variable of forgot password screen
global user_Entry2, password_Entry2, submit_button2, confirm_Entry, window


def initScreen():
    # initilize the First Screen of Program
    global usernameEntry, passwordEntry, openEye, closeEye, eyeButton, loginWindow
    loginWindow = Tk()
    loginWindow.geometry('990x660+50+50')
    loginWindow.resizable(0, 0)
    loginWindow.title('Login Page')
    bgPath = "images/LoginScreenImages/bg.jpg"
    bgImage = ImageTk.PhotoImage(file=bgPath)
    bgLabel = Label(loginWindow, image=bgImage)
    bgLabel.place(x=0, y=0)
    heading = Label(loginWindow, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
                    bg='white', fg='firebrick1')
    heading.place(x=620, y=120)
    # Username GUI
    usernameEntry = Entry(loginWindow, width=20, font=('Microsoft Yahei UI Light', 11, 'bold')
                          , bd=0, fg='firebrick1')
    usernameEntry.place(x=580, y=200)
    usernameEntry.insert(0, 'Username')
    usernameEntry.bind('<FocusIn>', user_enter)
    frame1 = Frame(loginWindow, width=250, height=2, bg='firebrick1')
    frame1.place(x=580, y=222)
    # Password GUI
    passwordEntry = Entry(loginWindow, width=20, font=('Microsoft Yahei UI Light', 11, 'bold')
                          , bd=0, fg='firebrick1')
    passwordEntry.place(x=580, y=260)
    passwordEntry.insert(0, 'Password')
    passwordEntry.bind('<FocusIn>', password_enter)
    frame2 = Frame(loginWindow, width=250, height=2, bg='firebrick1')
    frame2.place(x=580, y=282)
    # eye Button In Password
    global openEye, closeEye
    openEyePath = "images/LoginScreenImages/openeye.png"
    closeEyePath = "images/LoginScreenImages/closeye.png"
    openEye = ImageTk.PhotoImage(file=openEyePath)
    closeEye = ImageTk.PhotoImage(file=closeEyePath)
    eyeButton = Button(loginWindow, image=openEye, bd=0, bg='white', activebackground='white'
                       , cursor='hand2', command=hide)
    eyeButton.place(x=800, y=255)

    # forgot password button
    forgetButton = Button(loginWindow, text='Forgot Password?', bd=0, bg='white', activebackground='white'
                          , cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),
                          fg='firebrick1', activeforeground='firebrick1', command=forgot_password)
    forgetButton.place(x=715, y=295)
    # login button

    loginButton = Button(loginWindow, text='Login', font=('Open Sans', 16, 'bold'),
                         fg='white', bg='firebrick1', activeforeground='white',
                         activebackground='firebrick1', cursor='hand2', bd=0,
                         width=19, command=login)
    loginButton.place(x=578, y=350)
    # orLabel

    orLabel = Label(loginWindow, text='---------------OR---------------', font=('Open Sans', 16, 'bold')
                    , bg='white', fg='firebrick1')
    orLabel.place(x=583, y=400)
    # signup button
    orLabel = Label(loginWindow, text='Dont have an account?', font=('Open Sans', 9, 'bold')
                    , bg='white', fg='firebrick1')
    orLabel.place(x=590, y=500)

    newAccountButton = Button(loginWindow, text='Create New one', font=('Open Sans', 9, 'bold underline'),
                              fg='blue', bg='white', activeforeground='blue',
                              activebackground='white', cursor='hand2', bd=0, command=sign_up_page)
    newAccountButton.place(x=727, y=500)

    loginWindow.mainloop()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ functional Part @@@@@@@@@@@@@@@@@@@@@@@@@222
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    global openEye, closeEye
    if passwordEntry.cget('show') == '':
        passwordEntry.config(show='*')
        eyeButton.config(image=closeEye)
    else:
        passwordEntry.config(show='')
        eyeButton.config(image=openEye)


def sign_up_page():
    loginWindow.destroy()
    from signUpScreen import init_signup_screen
    init_signup_screen()


def login():
    # login clicked
    if usernameEntry.get() == '' or passwordEntry.get() == '' \
            or usernameEntry.get() == 'Username' or passwordEntry.get() == 'Password':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Shitrit1!')
            cursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connective Issue, Please Try Again')
            return
        query = 'SELECT * FROM final_project_db.`users` WHERE username=%s and password=%s'
        cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Username or Password Invalid')
        else:
            messagebox.showerror('Successful', 'Login is successful')


def forgot_password():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    global user_Entry2, password_Entry2, submit_button2, confirm_Entry, window
    window = Toplevel()
    window.title('Change Password')
    bgPath2 = "images/forgotScreen/background.jpg"
    bgImage2 = ImageTk.PhotoImage(file=bgPath2)
    bgLabel2 = Label(window, image=bgImage2)
    bgLabel2.grid()
    heading2 = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'),
                     bg='white', fg='magenta2')
    heading2.place(x=480, y=60)
    # user entry
    user_label = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white'
                       , fg='magenta2', highlightthickness=0)
    user_label.place(x=470, y=130)

    user_Entry2 = Entry(window, width=25, font=('arial', 11, 'bold'),
                        bd=0, fg='magenta2')
    user_Entry2.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    # password Entry
    password_label = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white'
                           , fg='magenta2', highlightthickness=0)
    password_label.place(x=470, y=210)

    password_Entry2 = Entry(window, width=25, font=('arial', 11, 'bold'),
                            bd=0, fg='magenta2')
    password_Entry2.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    # confirm password
    confirm_label = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white',
                          fg='magenta2', highlightthickness=0)
    confirm_label.place(x=470, y=290)

    confirm_Entry = Entry(window, width=25, font=('arial', 11, 'bold'),
                          bd=0, fg='magenta2')
    confirm_Entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)
    submit_button2 = Button(window, text='Submit', font=('Open Sans', 16, 'bold'),
                            fg='white', bg='magenta2', width=19, activeforeground='white',
                            activebackground='magenta2', cursor='hand2', bd=0, command=change_password)
    submit_button2.place(x=470, y=390)
    window.mainloop()


def change_password():
    # functional part of change password here we do all gui test and Updateing the data base
    # user_Entry2, password_Entry2, submit_button2, submit_Entry2

    if user_Entry2.get() == '' or password_Entry2.get() == '' or confirm_Entry.get() == '':
        messagebox.showerror('Error', 'All Field Required', parent=window)
    elif password_Entry2.get() != confirm_Entry.get():
        messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Shitrit1!')
            cursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connective Issue, Please Try Again')
            return

        query = 'SELECT * FROM final_project_db.`users` WHERE username=%s'
        cursor.execute(query, user_Entry2.get())
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Username Not Exist', parent=window)
        else:
            query = 'UPDATE final_project_db.`users` SET password=%s WHERE username=%s'
            cursor.execute(query, (password_Entry2.get(), user_Entry2.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Password is reset, Please login with new password', parent=window)
            window.destroy()
