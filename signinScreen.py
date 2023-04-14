from tkinter import *
from PIL import ImageTk

global root, usernameEntry, passwordEntry, openEye, closeEye , eyeButton


def initScreen():
    # initilize the First Screen of Program
    global usernameEntry, passwordEntry, openEye, closeEye,eyeButton
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

    #forgot password button
    forgetButton = Button(loginWindow, text= 'Forgot Password?', bd=0, bg='white', activebackground='white'
                       , cursor='hand2',font=('Microsoft Yahei UI Light',9, 'bold'),
                          fg= 'firebrick1',activeforeground='firebrick1')
    forgetButton.place(x=715, y=295)
    #login button

    loginButton = Button(loginWindow, text= 'Login', font=('Open Sans',16,'bold'),
                         fg='white',bg='firebrick1',activeforeground='white',
                         activebackground='firebrick1',cursor='hand2',bd=0,width=19)
    loginButton.place(x=578, y=350)
    #orLabel

    orLabel=Label(loginWindow,text='---------------OR---------------',font=('Open Sans',16,'bold')
                  ,bg='white',fg='firebrick1')
    orLabel.place(x=583, y=400)

    #facebook login
    facebook_logo_path="images/LoginScreenImages/facebook.png"
    fbimg = ImageTk.PhotoImage(file = facebook_logo_path)
    fbLabel= Label(loginWindow,image=fbimg,bg='white')
    fbLabel.place(x=690,y=440)
    # google login
    google_logo_path = "images/LoginScreenImages/google.png"
    googImg = ImageTk.PhotoImage(file=google_logo_path)
    googleLabel = Label(loginWindow, image=googImg , bg='white')
    googleLabel.place(x=740, y=440)
    # twitter login
    twitter_logo_path = "images/LoginScreenImages/twitter.png"
    twitterImg = ImageTk.PhotoImage(file=twitter_logo_path)
    twitterLabel = Label(loginWindow, image=twitterImg, bg='white')
    twitterLabel.place(x=640, y=440)

    #signup button
    orLabel = Label(loginWindow, text='Dont have an account?', font=('Open Sans', 9, 'bold')
                    , bg='white', fg='firebrick1')
    orLabel.place(x=590, y=500)

    newAccountButton = Button(loginWindow, text='Create New one', font=('Open Sans', 9, 'bold underline'),
                         fg='blue', bg='white', activeforeground='blue',
                         activebackground='white', cursor='hand2', bd=0)
    newAccountButton.place(x=727, y=500)


    loginWindow.mainloop()
# functional Part
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