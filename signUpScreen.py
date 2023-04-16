from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
global emailEntry, usernameEntry, passwordEntry, confirmEntry, signupButton, loginButton, signup_window
global check


def init_signup_screen():
    global emailEntry, usernameEntry, passwordEntry, confirmEntry, signupButton, loginButton, signup_window
    global check
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ GUI Part @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Init The Screen
    signup_window = Tk()
    signup_window.title('Signup Page')
    signup_window.resizable(False, False)
    signup_bg_path = "images/LoginScreenImages/bg.jpg"
    background = ImageTk.PhotoImage(file=signup_bg_path)
    bgLabel = Label(signup_window, image=background)
    bgLabel.grid()

    frame = Frame(signup_window)
    frame.place(x=554, y=100)
    heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'),
                    bg='white', fg='firebrick1')
    heading.grid(row=0, column=0, padx=10, pady=10)
    # email Label Entry
    emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'),
                       bg='white', fg='firebrick1')
    emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
    emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                       fg='white', bg='firebrick1')
    emailEntry.grid(row=2, column=0, sticky='w', padx=25)
    # username Label Entry
    usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'),
                          bg='white', fg='firebrick1')
    usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
    usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='white', bg='firebrick1')
    usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

    # password Label Entry
    passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'),
                          bg='white', fg='firebrick1')
    passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
    passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='white', bg='firebrick1')
    passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

    # Confirm password Label Entry
    confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'),
                         bg='white', fg='firebrick1')
    confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
    confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                         fg='white', bg='firebrick1')
    confirmEntry.grid(row=8, column=0, sticky='w', padx=25)
    # term and condition
    check = IntVar()
    terms = Checkbutton(frame, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 9, 'bold'),
                        fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
                        cursor='hand2', variable=check)
    terms.grid(row=9, column=0, pady=10, padx=15)
    # signUp Button
    signupButton = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'), bd=0
                          , bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white',
                          width=17, command=empty_field)
    signupButton.grid(row=10, column=0, pady=10)
    # all Ready Account
    alrac = Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
                  bg='white', fg='firebrick1')
    alrac.grid(row=11, column=0, sticky='w', padx=25, pady=10)
    loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'),
                         fg='blue', bg='white', activeforeground='blue',
                         activebackground='white', cursor='hand2', bd=0, command=login_page)
    loginButton.place(x=171, y=404)

    signup_window.mainloop()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Functional Part@@@@@@@@@@@@@@@@@@@@@@@@
# log in button
def login_page():
    signup_window.destroy()
    from signinScreen import initScreen
    initScreen()


# empty field message box

def empty_field():
    if (emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == ''
            or confirmEntry.get() == ''):
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Passwords Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Condition')
    else:
        # insert to DB The Details
        try:
            con = pymysql.connect(host='localhost', user='root', password='Shitrit1!')

        except:
            messagebox.showerror('Error', 'Database Connective Issue, Please Try Again')
            return
        cursor = con.cursor()
        email = emailEntry.get()
        username = usernameEntry.get()
        password = passwordEntry.get()
        # Check if Email And Username Exist
        query = 'SELECT * FROM final_project_db.`users` WHERE username=%s'
        cursor.execute(query, usernameEntry.get())
        row = cursor.fetchone()

        if row != None:
            messagebox.showerror('Error', 'Username already exist')
        else:
            query = 'SELECT * FROM final_project_db.`users` WHERE mail=%s'
            cursor.execute(query, emailEntry.get())
            row = cursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Email already exist')
            else:
                # All The Details Correct And Legal InSERT to DB
                query = "INSERT INTO final_project_db.`users` (`mail`, `username`, `password`) VALUES (%s, %s, %s)"
                cursor.execute(query, (email, username, password))
                con.commit()
                cursor.close()
                con.close()
                messagebox.showerror('Successful', 'Registration is successful')
                clear()


def clear():
    # clear the field and go back to login screen
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)
    login_page()

