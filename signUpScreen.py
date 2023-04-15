from tkinter import *
from PIL import ImageTk

global emailEntry, usernameEntry, passwordEntry, confirmEntry, signupButton, loginButton, signup_window


def init_signup_screen():
    global emailEntry, usernameEntry, passwordEntry, confirmEntry, signupButton, loginButton, signup_window
    # GUI Part
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
    terms = Checkbutton(frame, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 9, 'bold'),
                        fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
                        cursor='hand2')
    terms.grid(row=9, column=0, pady=10, padx=15)
    # signUp Button
    signupButton = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'), bd=0
                          , bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white',
                          width=17)
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

    # Functional Part


def login_page():
    signup_window.destroy()
    from signinScreen import initScreen
    initScreen()
