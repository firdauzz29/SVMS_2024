import os
import time
import random
import string
import logging
import zipfile
from tkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
from datetime import datetime

global username_info

def main_account_screen():
    # Main welcoming window
    logging.info("CUR-MAIN_ACCOUNT_SCREEN")
    global main_screen
    main_screen = Tk()
    main_screen.title("Login Page")
    main_screen.attributes('-fullscreen', True)

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/welcome-screen.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(main_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    welcome_screen_title = Label(text="Street Vendor Management System", fg="#1061fe", bg="#ffffff", font=("Stem-bold", 24, "bold"))
    welcome_screen_title.place(relx=0.75, rely=0.30, anchor=CENTER)

    welcome_screen_description1 = Label(text='"In software systems it is often the early bird that makes the worm."', fg="#1f2d3b", bg="#ffffff", font=("Stem-bold", 14))
    welcome_screen_description1.place(relx=0.75, rely=0.35, anchor=CENTER)
    welcome_screen_description2 = Label(text="                                                                 - Alan Perlis", fg="#1f2d3b", bg="#ffffff", font=("Stem-bold", 14))
    welcome_screen_description2.place(relx=0.75, rely=0.38, anchor=CENTER)

    login_button = PhotoImage(file="graphics/login-screen-login.png")
    welcome_screen_login_button = Button(main_screen, image=login_button, borderwidth=0, bg="#ffffff", command=login)
    welcome_screen_login_button.place(relx=0.75, rely=0.50, anchor=CENTER)

    register_button = PhotoImage(file="graphics/login-screen-register.png")
    welcome_screen_register_button = Button(main_screen, image=register_button, borderwidth=0, bg="#ffffff", command=register)
    welcome_screen_register_button.place(relx=0.75, rely=0.65, anchor=CENTER)

    exit_button = PhotoImage(file="graphics/exit.png")
    welcome_screen_exit_button = Button(main_screen, image=exit_button, borderwidth=0, bg="#ffffff", command=quit_system)
    welcome_screen_exit_button.place(relx=0.75, rely=0.80, anchor=CENTER)

    main_screen.mainloop()

def register():
    # User registration screen
    logging.info("CUR-REGISTER")
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.attributes('-fullscreen', True)

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/register-screen.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(register_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    # Credential
    global username
    global password
    global regiskey
    global username_entry
    global password_entry
    global regiskey_entry

    username = StringVar()
    password = StringVar()
    regiskey = StringVar()

    register_screen_text = Label(register_screen, text="Register", fg="#febe10", bg="#ffffff", font=("Stem-bold", 36, "bold"))
    register_screen_text.place(relx=0.50, rely=0.30, relwidth=0.20, relheight=0.10, anchor=CENTER)

    username_label = Label(register_screen, text="Username", font=("Stem-bold", 14, "bold"))
    username_label.place(relx=0.50, rely=0.40, relwidth=0.10, relheight=0.02, anchor=CENTER)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(relx=0.50, rely=0.45, relwidth=0.10, relheight=0.02, anchor=CENTER)

    password_label = Label(register_screen, text="Password", font=("Stem-bold", 14, "bold"))
    password_label.place(relx=0.50, rely=0.50, relwidth=0.10, relheight=0.02, anchor=CENTER)
    password_entry = Entry(register_screen, textvariable=password, show="*")
    password_entry.place(relx=0.50, rely=0.55, relwidth=0.10, relheight=0.02, anchor=CENTER)

    regiskey_label = Label(register_screen, text="Regiskey", font=("Stem-bold", 14, "bold"))
    regiskey_label.place(relx=0.50, rely=0.60, relwidth=0.10, relheight=0.02, anchor=CENTER)
    regiskey_entry = Entry(register_screen, textvariable=regiskey, show="*")
    regiskey_entry.place(relx=0.50, rely=0.65, relwidth=0.10, relheight=0.02, anchor=CENTER)

    register_button = PhotoImage(file="graphics/register.png")
    register_screen_register_button = Button(register_screen, image=register_button, borderwidth=0, bg="#ffffff", command=register_user)
    register_screen_register_button.place(relx=0.50, rely=0.70, anchor=CENTER)

    back_button = PhotoImage(file="graphics/back.png")
    login_screen_back_button = Button(register_screen, image=back_button, borderwidth=0, bg="#ffffff", command=delete_register)
    login_screen_back_button.place(relx=0.50, rely=0.75, anchor=CENTER)

    register_screen.mainloop()

def register_user():
    # Check user credential
    logging.info("CUR-REGISTER_USER")
    username_info = username.get()
    password_info = password.get()
    regiskey_info = regiskey.get()

    list_of_user  = os.listdir("credentials")
    file_of_rkeyx = open("regiskey/" + "regiskey.txt", "r")
    list_of_rkey  = file_of_rkeyx.read().splitlines()
    file_of_rkeyx.close()

    if username_info in list_of_user:
        exist_register_user()
    elif regiskey_info in list_of_rkey:
        new_register_user()
    else:
        invalid_register_user()

def exist_register_user():
    # User already exists
    logging.info("CUR-EXIST_REGISTER_USER")
    global exist_register_user_screen
    exist_register_user_screen = Toplevel(register_screen)
    exist_register_user_screen.title("")
    exist_register_user_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/register-failed.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(exist_register_user_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    regiskey_entry.delete(0, END)

    register_user_failed_description = Label(exist_register_user_screen, text="Welcome to SVMS\nPlease login with\nexisting username!", fg="#ce393c", bg="#fef9f9", font=("Stem-bold", 12, "bold"))
    register_user_failed_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    register_user_failed_button = Label(exist_register_user_screen, text="User Exists", fg="#212828", bg="#fef9f9", font=("Stem-bold", 12, "bold"))
    register_user_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    register_user_failed_ok_button = Button(exist_register_user_screen, image=next_button_image, borderwidth=0, command=delete_exist_register_user_screen)
    register_user_failed_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    exist_register_user_screen.mainloop()

def delete_exist_register_user_screen():
    logging.info("CUR-DELETE_EXIST_REGISTER_USER_SCREEN")
    exist_register_user_screen.destroy()

def invalid_register_user():
    # User already exists
    logging.info("CUR-INVALID_REGISTER_USER")
    global invalid_register_user_screen
    invalid_register_user_screen = Toplevel(register_screen)
    invalid_register_user_screen.title("")
    invalid_register_user_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/register-failed.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(invalid_register_user_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    regiskey_entry.delete(0, END)

    register_user_failed_description = Label(invalid_register_user_screen, text="Welcome to SVMS\nPlease login with\nvalid authentication\ncode!", fg="#ce393c", bg="#fef9f9", font=("Stem-bold", 12, "bold"))
    register_user_failed_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    register_user_failed_button = Label(invalid_register_user_screen, text="Invalid Authentication Code", fg="#212828", bg="#fef9f9", font=("Stem-bold", 12, "bold"))
    register_user_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    register_user_failed_ok_button = Button(invalid_register_user_screen, image=next_button_image, borderwidth=0, command=delete_invalid_register_user_screen)
    register_user_failed_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    invalid_register_user_screen.mainloop()

def delete_invalid_register_user_screen():
    logging.info("CUR-INVALID_REGISTER_USER_SCREEN_DESTROY")
    invalid_register_user_screen.destroy()

def new_register_user():
    # New user
    logging.info("CUR-NEW_REGISTER_USER")
    global new_register_user_screen
    new_register_user_screen = Toplevel(register_screen)
    new_register_user_screen.title("")
    new_register_user_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/register-success.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(new_register_user_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    username_info = username.get()
    password_info = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    regiskey_entry.delete(0, END)

    create_directory("credentials")

    file = open("credentials/" + username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write("")
    file.close()

    register_user_success_description = Label(new_register_user_screen, text="Welcome to SVMS\n" + username_info + "!", fg="#3f88a3", bg="#fefcf9", font=("Stem-bold", 12, "bold"))
    register_user_success_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    register_user_success_button = Label(new_register_user_screen, text="Successfully Registered", fg="#212828", bg="#fefcf9", font=("Stem-bold", 12, "bold"))
    register_user_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    register_user_success_ok_button = Button(new_register_user_screen, image=next_button_image, borderwidth=0, command=delete_new_register_user_screen)
    register_user_success_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    new_register_user_screen.mainloop()

def delete_new_register_user_screen():
    logging.info("CUR-DELETE_NEW_REGISTER_USER_SCREEN")
    new_register_user_screen.destroy()

def login():
    # Login screen for administrator and user
    logging.info("CUR-LOGIN")
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.attributes('-fullscreen', True)

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/login-screen.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(login_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    # Credential
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    login_screen_text = Label(login_screen, text="Login", fg="#1061fe", bg="#ffffff", font=("Stem-bold", 36, "bold"))
    login_screen_text.place(relx=0.50, rely=0.30, relwidth=0.20, relheight=0.10, anchor=CENTER)

    login_screen_id = Label(login_screen, text="Username", font=("Stem-bold", 14, "bold"))
    login_screen_id.place(relx=0.50, rely=0.40, relwidth=0.10, relheight=0.02, anchor=CENTER)

    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(relx=0.50, rely=0.45, relwidth=0.10, relheight=0.02, anchor=CENTER)

    login_screen_pw = Label(login_screen, text="Password", font=("Stem-bold", 14, "bold"))
    login_screen_pw.place(relx=0.50, rely=0.50, relwidth=0.10, relheight=0.02, anchor=CENTER)

    password_login_entry = Entry(login_screen, textvariable=password_verify, show="*")
    password_login_entry.place(relx=0.50, rely=0.55, relwidth=0.10, relheight=0.02, anchor=CENTER)

    login_button_image = PhotoImage(file="graphics/login.png")
    login_screen_login_button = Button(login_screen, image=login_button_image, borderwidth=0, bg="#ffffff", command=login_verify)
    login_screen_login_button.place(relx=0.50, rely=0.60, anchor=CENTER)

    back_button_image = PhotoImage(file="graphics/back.png")
    login_screen_back_button = Button(login_screen, image=back_button_image, borderwidth=0, bg="#ffffff", command=delete_login)
    login_screen_back_button.place(relx=0.50, rely=0.65, anchor=CENTER)

    login_screen.mainloop()

def login_verify():
    # Verify credential
    logging.info("CUR-LOGIN_VERIFY")
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir("credentials")

    if username1 == "svms" and password1 == "svms123":
        is_admin()

    elif username1 in list_of_files:
        file = open("credentials/" + username1, "r")
        verify = file.read().splitlines()
        file.close()
        if password1 == verify[1]:
            login_success()
        else:
            password_not_recognized()

    else:
        user_not_found()

def is_admin():
    # Logged in as administrator
    logging.info("CUR-IS_ADMIN")
    global admin_login_success_screen
    admin_login_success_screen = Toplevel(login_screen)
    admin_login_success_screen.title("Welcome Administrator")
    admin_login_success_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/login-success.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_login_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_login_success_description = Label(admin_login_success_screen, text="Login Success\nWelcome back\nadministrator!", fg="#2d7691", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    admin_login_success_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    admin_login_success_button = Label(admin_login_success_screen, text="Successfully Logged In", fg="#ffa853", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    admin_login_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    admin_login_success_ok_button = Button(admin_login_success_screen, image=next_button_image, borderwidth=0, command=delete_admin_login_success_screen)
    admin_login_success_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    admin_login_success_screen.mainloop()

def login_success():
    # Login success
    logging.info("CUR-LOGIN_SUCCESS")
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/login-success.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(login_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    user_login_success_description = Label(login_success_screen, text="Login Success\nWelcome back\n" + username1 + "!", fg="#2d7691", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_success_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    user_login_success_button = Label(login_success_screen, text="Successfully Logged In", fg="#ffa853", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    user_login_success_ok_button = Button(login_success_screen, image=next_button_image, borderwidth=0, command=delete_login_success)
    user_login_success_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    login_success_screen.mainloop()

def delete_register():
    logging.info("CUR-DELETE_REGISTER")
    register_screen.destroy()

def delete_login():
    logging.info("CUR-DELETE_LOGIN")
    login_screen.destroy()

def delete_login_success():
    logging.info("CUR-DELETE_LOGIN_SUCCESS")
    login_screen.destroy()
    user_view()

def delete_admin_login_success_screen():
    logging.info("CUR-DELETE_ADMIN_LOGIN_SUCCESS_SCREEN")
    login_screen.destroy()
    admin_view()

def quit_system():
    logging.info("CUR-QUIT_SYSTEM")
    main_screen.destroy()

def password_not_recognized():
    logging.info("CUR-PASSWORD_NOT_RECOGNIZED")
    # Wrong password
    global password_not_recognized_screen
    password_not_recognized_screen = Toplevel(login_screen)
    password_not_recognized_screen.title("")
    password_not_recognized_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/login-failed.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(password_not_recognized_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    user_login_failed_description = Label(password_not_recognized_screen, text="Invalid Username or\nPassword!", fg="#205d8c", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_failed_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    user_login_failed_button = Label(password_not_recognized_screen, text="Login Failed", fg="#932a53", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    user_login_failed_ok_button = Button(password_not_recognized_screen, image=next_button_image, borderwidth=0, command=delete_password_not_recognized)
    user_login_failed_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    password_not_recognized_screen.mainloop()

def delete_password_not_recognized():
    logging.info("CUR-DELETE_PASSWORD_NOT_RECOGNIZED")
    password_not_recognized_screen.destroy()

def user_not_found():
    # Wrong username
    logging.info("CUR-USER_NOT_FOUND")
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("")
    user_not_found_screen.geometry("220x475")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/login-failed.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(user_not_found_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    user_login_failed_description = Label(user_not_found_screen, text="Invalid Username or\nPassword!", fg="#205d8c", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_failed_description.place(relx=0.50, rely=0.60, anchor=CENTER)

    user_login_failed_button = Label(user_not_found_screen, text="Login Failed", fg="#932a53", bg="#ffffff", font=("Stem-bold", 12, "bold"))
    user_login_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    next_button_image = PhotoImage(file="graphics/next-button.png")
    user_login_failed_ok_button = Button(user_not_found_screen, image=next_button_image, borderwidth=0, command=delete_user_not_found_screen)
    user_login_failed_ok_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    user_not_found_screen.mainloop()

def delete_user_not_found_screen():
    logging.info("CUR-DELETE_USER_NOT_FOUND_SCREEN")
    user_not_found_screen.destroy()

def admin_view():
    # Administrator view
    logging.info("CUR-ADMIN_VIEW")
    global admin_view_screen
    admin_view_screen = Toplevel(main_screen)
    admin_view_screen.title("Welcome Administrator")
    admin_view_screen.attributes('-fullscreen', True)

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    random_images = ["graphics/admin-screen.png", "graphics/admin-screen.png"]
    random_image  = random.choice(random_images)
    image = Image.open(random_image)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_view_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_view_text_right = Label(admin_view_screen, text="Welcome back, Administrator!", fg="#31346b", bg="#ffffff", font=("Stem-bold", 36, "bold"))
    admin_view_text_right.place(relx=0.77, rely=0.20, anchor=CENTER)

    admin_add_court_button_image = PhotoImage(file="graphics/admin-view-profile.png")
    admin_add_court_button = Button(admin_view_screen, image=admin_add_court_button_image, borderwidth=0, bg="#ffffff", command=admin_view_profile)
    admin_add_court_button.place(relx=0.77, rely=0.30, anchor=CENTER)

    admin_modify_court_button_image = PhotoImage(file="graphics/admin-view-listing.png")
    admin_modify_court_button = Button(admin_view_screen, image=admin_modify_court_button_image, borderwidth=0, bg="#ffffff", command=admin_view_listing)
    admin_modify_court_button.place(relx=0.77, rely=0.40, anchor=CENTER)

    admin_delete_court_button_image = PhotoImage(file="graphics/admin-delete-listing.png")
    admin_delete_court_button = Button(admin_view_screen, image=admin_delete_court_button_image, borderwidth=0, bg="#ffffff", command=admin_delete_listing)
    admin_delete_court_button.place(relx=0.77, rely=0.50, anchor=CENTER)

    admin_view_court_button_image = PhotoImage(file="graphics/admin-view-feedback.png")
    admin_view_court_button = Button(admin_view_screen, image=admin_view_court_button_image, borderwidth=0, bg="#ffffff", command=admin_view_feedback)
    admin_view_court_button.place(relx=0.77, rely=0.60, anchor=CENTER)

    admin_2fa_button_image = PhotoImage(file="graphics/admin-generate-2fa.png")
    admin_2fa_button = Button(admin_view_screen, image=admin_2fa_button_image, borderwidth=0, bg="#ffffff", command=admin_generate_2fa)
    admin_2fa_button.place(relx=0.77, rely=0.70, anchor=CENTER)

    admin_view_2fa_button_image = PhotoImage(file="graphics/admin-view-2fa.png")
    admin_view_2fa_button = Button(admin_view_screen, image=admin_view_2fa_button_image, borderwidth=0, bg="#ffffff", command=admin_view_2fa)
    admin_view_2fa_button.place(relx=0.77, rely=0.80, anchor=CENTER)

    admin_view_sales_button_image = PhotoImage(file="graphics/admin-view-sales.png")
    admin_view_sales_button = Button(admin_view_screen, image=admin_view_sales_button_image, borderwidth=0, bg="#ffffff", command=admin_view_sales)
    admin_view_sales_button.place(relx=0.77, rely=0.90, anchor=CENTER)

    logout_button_image = PhotoImage(file="graphics/logout.png")
    admin_logout_button = Button(admin_view_screen, image=logout_button_image, borderwidth=0, command=delete_admin_view)
    admin_logout_button.place(relx=0.50, rely=0.95, anchor=CENTER)

    admin_view_screen.mainloop()

def delete_admin_view():
    logging.info("CUR-DELETE_ADMIN_VIEW")
    admin_view_screen.destroy()

def admin_view_profile():
    # view profile details
    logging.info("CUR-ADMIN_VIEW_PROFILE")
    global view_profile_screen
    view_profile_screen = Toplevel(admin_view_screen)
    view_profile_screen.title("View Profile")
    view_profile_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-02-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(view_profile_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    list_of_profile = os.listdir("credentials/")

    big_inventory = []
    for i in range(len(list_of_profile)):
        inventory = []
        content = time.ctime((os.path.getctime("credentials/" + list_of_profile[i])))
        inventory.append(list_of_profile[i])
        inventory.append(str(datetime.strptime(content, "%a %b %d %H:%M:%S %Y")))
        big_inventory.append(inventory)

    admin_view_vendor_profile_name = Label(view_profile_screen, text="Vendor", fg="black", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_name.place(relx=0.05, rely=0.10, relwidth=0.30, relheight=0.06)
    admin_view_vendor_profile_date = Label(view_profile_screen, text="Creation Date", fg="black", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.56, rely=0.10, relwidth=0.30, relheight=0.06)

    for i in range(len(big_inventory)):
        for j in range(len(big_inventory[0])):
            e = Entry(view_profile_screen, width=20, fg="blue", font=("Arial", 16, "bold"))
            if i==0:
                pady = (100, 2)
            else:
                pady = (2, 2)
            if j+1 % 2:
                e.grid(row=i, column=j, padx=30, pady=pady)
            else:
                e.grid(row=i, column=j, padx=50, pady=pady)
            e.insert(END, big_inventory[i][j])


    back_button = PhotoImage(file="graphics/back.png")
    admin_view_profile_back_button = Button(view_profile_screen, image=back_button, borderwidth=0, bg="#ffffff", command=delete_admin_view_profile)
    admin_view_profile_back_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    view_profile_screen.mainloop()

def delete_admin_view_profile():
    logging.info("CUR-DELETE_ADMIN_VIEW_PROFILE")
    view_profile_screen.destroy()

def admin_view_listing():
    # view listing details
    logging.info("CUR-ADMIN_VIEW_LISTING")
    global view_listing_label_vendor_name_value

    global view_listing_screen
    view_listing_screen = Toplevel(admin_view_screen)
    view_listing_screen.title("View Listing")
    view_listing_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-02-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(view_listing_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    view_listing_label_vendor_name = Label(view_listing_screen, text="Vendor Name", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    view_listing_label_vendor_name.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    view_listing_label_vendor_name_value = Entry(view_listing_screen)
    view_listing_label_vendor_name_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    check_listing_submit_button_image = PhotoImage(file="graphics/next-button.png")
    check_listing_label_submit = Button(view_listing_screen, image=check_listing_submit_button_image, borderwidth=0, command=check_view_admin_listing_record)
    check_listing_label_submit.place(relx=0.50, rely=0.9, anchor=CENTER)

    view_listing_screen.mainloop()

def check_view_admin_listing_record():
    # Verify listing details
    logging.info("CUR-CHECK_VIEW_ADMIN_LISTING_RECORD")
    global admin_view_listing_vendor_name

    admin_view_listing_vendor_name = view_listing_label_vendor_name_value.get()
    list_of_profile = os.listdir("credentials/")

    if admin_view_listing_vendor_name not in list_of_profile:
        check_view_admin_listing_record_error()
    else:
        check_view_admin_listing_record_success()

def check_view_admin_listing_record_error():
    # Court payment
    logging.info("CUR-CHECK_VIEW_ADMIN_LISTING_RECORD_ERROR")
    global check_view_admin_listing_record_error_screen
    check_view_admin_listing_record_error_screen = Toplevel(admin_view_screen)
    check_view_admin_listing_record_error_screen.title("View Listing")
    check_view_admin_listing_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_view_admin_listing_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    view_admin_listing_text = Label(check_view_admin_listing_record_error_screen, text="Error!", fg="#212828", bg="#ffffff")
    view_admin_listing_text.place(relx=0.50, rely=0.10, anchor=N)

    view_admin_listing_button_image = PhotoImage(file="graphics/next-button.png")
    view_admin_listing_button = Button(check_view_admin_listing_record_error_screen, image=view_admin_listing_button_image, borderwidth=0, command=check_check_view_admin_listing_record_error_screen)
    view_admin_listing_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_view_admin_listing_record_error_screen.mainloop()

def check_check_view_admin_listing_record_error_screen():
    logging.info("CUR-CHECK_CHECK_VIEW_ADMIN_LISTING_RECORD_ERROR_SCREEN")
    check_view_admin_listing_record_error_screen.destroy()
    view_listing_screen.destroy()

def check_view_admin_listing_record_success():
    logging.info("CUR-CHECK_VIEW_ADMIN_LISTING_RECORD_SUCCESS")
    view_listing_screen.destroy()
    admin_view_listing_by_vendor_name()

def admin_view_listing_by_vendor_name():
    # Verify listing details
    logging.info("CUR-ADMIN_VIEW_LISTING_BY_VENDOR_NAME")
    global view_listing_by_vendor_name_screen_back_button
    global view_listing_by_vendor_name_screen
    view_listing_by_vendor_name_screen = Toplevel(admin_view_screen)
    view_listing_by_vendor_name_screen.title("View Listing")
    view_listing_by_vendor_name_screen.geometry("1900x960")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-08-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(view_listing_by_vendor_name_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)


    list_of_profile = os.listdir("credentials/")

    """
    admin_view_vendor_profile_name = Label(view_listing_by_vendor_name_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_name.place(relx=0.02, rely=0.05, relwidth=0.20, relheight=0.04)
    admin_view_vendor_profile_date = Label(view_listing_by_vendor_name_screen, text="Product Name", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.22, rely=0.05, relwidth=0.20, relheight=0.04)
    admin_view_vendor_profile_date = Label(view_listing_by_vendor_name_screen, text="Price", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.42, rely=0.05, relwidth=0.20, relheight=0.04)
    admin_view_vendor_profile_date = Label(view_listing_by_vendor_name_screen, text="Quantity", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.62, rely=0.05, relwidth=0.20, relheight=0.04)
    admin_view_vendor_profile_date = Label(view_listing_by_vendor_name_screen, text="Location", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.72, rely=0.05, relwidth=0.20, relheight=0.04)
    admin_view_vendor_profile_date = Label(view_listing_by_vendor_name_screen, text="Contact", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_profile_date.place(relx=0.92, rely=0.05, relwidth=0.20, relheight=0.04)
    """

    big_inventory = []
    list_of_listing = os.listdir("listing_record/" + admin_view_listing_vendor_name)

    for i in range(len(list_of_listing)):
        file = open("listing_record/" + admin_view_listing_vendor_name + "/" + list_of_listing[i], "r")
        content = file.read().splitlines()
        big_inventory.append(content)
        file.close()

    for i in range(len(big_inventory)):
        for j in range(len(big_inventory[0])):
            e = Entry(view_listing_by_vendor_name_screen, width=20, fg="blue", font=("Arial", 16, "bold"))
            if i == 0:
                pady = (100, 2)
            else:
                pady = (2, 2)
            if j + 1 % 2:
                e.grid(row=i, column=j, padx=30, pady=pady)
            else:
                e.grid(row=i, column=j, padx=50, pady=pady)
            e.insert(END, big_inventory[i][j])

    back_button = PhotoImage(file="graphics/back.png")
    view_listing_by_vendor_name_screen_back_button = Button(view_listing_by_vendor_name_screen, image=back_button, borderwidth=0, bg="#ffffff", command=delete_admin_view_listing_by_vendor_name_screen)
    view_listing_by_vendor_name_screen_back_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    view_listing_by_vendor_name_screen.mainloop()

def delete_admin_view_listing_by_vendor_name_screen():
    logging.info("CUR-DELETE_ADMIN_VIEW_LISTING_BY_VENDOR_NAME_SCREEN")
    view_listing_by_vendor_name_screen.destroy()
    view_listing_screen.destroy()

def admin_delete_listing():
    # Delete listing details
    logging.info("CUR-ADMIN_DELETE_LISTING")
    global admin_delete_listing_label_vendor_name_value
    global admin_delete_listing_label_product_id_value

    global admin_delete_listing_screen
    admin_delete_listing_screen = Toplevel(admin_view_screen)
    admin_delete_listing_screen.title("Delete Listing")
    admin_delete_listing_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-02-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_delete_listing_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_delete_listing_label_vendor_name = Label(admin_delete_listing_screen, text="Vendor Name", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_delete_listing_label_vendor_name.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    admin_delete_listing_label_vendor_name_value = Entry(admin_delete_listing_screen)
    admin_delete_listing_label_vendor_name_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    admin_delete_listing_label_product_id = Label(admin_delete_listing_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_delete_listing_label_product_id.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    admin_delete_listing_label_product_id_value = Entry(admin_delete_listing_screen)
    admin_delete_listing_label_product_id_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    admin_check_listing_submit_button_image = PhotoImage(file="graphics/next-button.png")
    admin_check_listing_label_submit = Button(admin_delete_listing_screen, image=admin_check_listing_submit_button_image, borderwidth=0, command=admin_check_admin_delete_listing_record)
    admin_check_listing_label_submit.place(relx=0.50, rely=0.9, anchor=CENTER)

    admin_delete_listing_screen.mainloop()

def admin_check_admin_delete_listing_record():
    # Verify listing details
    logging.info("CUR-ADMIN_CHECK_ADMIN_DELETE_LISTING_RECORD")
    admin_delete_listing_vendor_name = admin_delete_listing_label_vendor_name_value.get()
    admin_delete_listing_product_id  = admin_delete_listing_label_product_id_value.get()

    if not os.path.isdir("listing_record/" + admin_delete_listing_vendor_name) or admin_delete_listing_product_id not in os.listdir("listing_record/" + admin_delete_listing_vendor_name + "/"):
        check_admin_delete_listing_record_error()
    else:
        admin_delete_listing_record()

def check_admin_delete_listing_record_error():
    # listing details error
    logging.info("CUR-CHECK_ADMIN_DELETE_LISTING_RECORD_ERROR")
    global check_admin_delete_listing_record_error_screen
    check_admin_delete_listing_record_error_screen = Toplevel(admin_delete_listing_screen)
    check_admin_delete_listing_record_error_screen.title("Delete Listing")
    check_admin_delete_listing_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_admin_delete_listing_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_delete_listing_record_failed_text = Label(check_admin_delete_listing_record_error_screen, text="Profile or product not found!", fg="#212828", bg="#ffffff")
    admin_delete_listing_record_failed_text.place(relx=0.50, rely=0.10, anchor=N)

    admin_delete_listing_record_failed_button_image = PhotoImage(file="graphics/small-next-button.png")
    admin_delete_listing_record_failed_button = Button(check_admin_delete_listing_record_error_screen, image=admin_delete_listing_record_failed_button_image, borderwidth=0, command=delete_check_admin_delete_listing_record_error_screen)
    admin_delete_listing_record_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_admin_delete_listing_record_error_screen.mainloop()

def delete_check_admin_delete_listing_record_error_screen():
    logging.info("CUR-DELETE_CHECK_ADMIN_DELETE_LISTING_RECORD_ERROR_SCREEN")
    check_admin_delete_listing_record_error_screen.destroy()

def admin_delete_listing_record():
    # Delete listing details
    logging.info("CUR-ADMIN_DELETE_LISTING_RECORD")
    admin_delete_listing_vendor_name = admin_delete_listing_label_vendor_name_value.get()
    admin_delete_listing_product_id  = admin_delete_listing_label_product_id_value.get()
    os.remove("listing_record/" + admin_delete_listing_vendor_name + "/" + admin_delete_listing_product_id)
    admin_delete_listing_record_success()

def admin_delete_listing_record_success():
    # listing deleted
    logging.info("CUR-ADMIN_DELETE_LISTING_RECORD_SUCCESS")
    global admin_delete_listing_record_success_screen
    admin_delete_listing_record_success_screen = Toplevel(admin_delete_listing_screen)
    admin_delete_listing_record_success_screen.title("Delete Listing")
    admin_delete_listing_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_delete_listing_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_delete_listing_record_success_text = Label(admin_delete_listing_record_success_screen, text="Product record successfully deleted.", fg="#212828", bg="#ffffff")
    admin_delete_listing_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    admin_delete_listing_record_success_button_image = PhotoImage(file="graphics/small-next-button.png")
    admin_delete_listing_record_success_button = Button(admin_delete_listing_record_success_screen, image=admin_delete_listing_record_success_button_image, borderwidth=0, command=delete_admin_delete_listing_record_success_screen)
    admin_delete_listing_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    admin_delete_listing_record_success_screen.mainloop()

def delete_admin_delete_listing_record_success_screen():
    logging.info("CUR-DELETE_ADMIN_DELETE_LISTING_RECORD_SUCCESS_SCREEN")
    admin_delete_listing_record_success_screen.destroy()
    admin_delete_listing_screen.destroy()

def admin_view_feedback():
    # view feedback details
    logging.info("CUR-ADMIN_VIEW_FEEBACK")
    global admin_view_feedback_label_vendor_name_value

    global admin_view_feedback_screen
    admin_view_feedback_screen = Toplevel(admin_view_screen)
    admin_view_feedback_screen.title("Feedback")
    admin_view_feedback_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-02-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_view_feedback_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_view_feedback_label_vendor_name = Label(admin_view_feedback_screen, text="Vendor Name", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_feedback_label_vendor_name.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    admin_view_feedback_label_vendor_name_value = Entry(admin_view_feedback_screen)
    admin_view_feedback_label_vendor_name_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    admin_check_feedback_submit_button_image = PhotoImage(file="graphics/next-button.png")
    admin_check_feedback_label_submit = Button(admin_view_feedback_screen, image=admin_check_feedback_submit_button_image, borderwidth=0, command=admin_check_admin_view_feedback_record)
    admin_check_feedback_label_submit.place(relx=0.50, rely=0.9, anchor=CENTER)

    admin_view_feedback_screen.mainloop()

def admin_check_admin_view_feedback_record():
    # Verify feedback details
    logging.info("CUR-ADMIN_CHECK_ADMIN_VIEW_FEEDBACK_RECORD")
    admin_view_feedback_vendor_name = admin_view_feedback_label_vendor_name_value.get()

    if admin_view_feedback_vendor_name not in os.listdir("feedback/"):
        check_admin_view_feedback_record_error()
    else:
        admin_view_feedback_record()

def check_admin_view_feedback_record_error():
    # feedback details error
    logging.info("CUR-CHECK_ADMIN_VIEW_FEEDBACK_RECORD_ERROR")
    global check_admin_view_feedback_record_error_screen
    check_admin_view_feedback_record_error_screen = Toplevel(admin_view_feedback_screen)
    check_admin_view_feedback_record_error_screen.title("Feedback")
    check_admin_view_feedback_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_admin_view_feedback_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    admin_view_feedback_record_failed_text = Label(check_admin_view_feedback_record_error_screen, text="Feedback not found!", fg="#212828", bg="#ffffff")
    admin_view_feedback_record_failed_text.place(relx=0.50, rely=0.10, anchor=N)

    admin_view_feedback_record_failed_button_image = PhotoImage(file="graphics/small-next-button.png")
    admin_view_feedback_record_failed_button = Button(check_admin_view_feedback_record_error_screen, image=admin_view_feedback_record_failed_button_image, borderwidth=0, command=view_check_admin_view_feedback_record_error_screen)
    admin_view_feedback_record_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_admin_view_feedback_record_error_screen.mainloop()

def view_check_admin_view_feedback_record_error_screen():
    logging.info("CUR-VIEW_CHECK_ADMIN_VIEW_FEEDBACK_RECORD_ERROR_SCREEN")
    check_admin_view_feedback_record_error_screen.destroy()

def admin_view_feedback_record():
    # view feedback details
    logging.info("CUR-ADMIN_VIEW_FEEDBACK_RECORD")
    admin_view_feedback_vendor_name = admin_view_feedback_label_vendor_name_value.get()

    feedback_record = open("feedback/" + admin_view_feedback_vendor_name, "r")
    feedback_record_read = feedback_record.readlines()
    feedback_record.close()

    global new_court_label_title_value, new_court_label_status_value

    show_feedback_text = Text(admin_view_feedback_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
    show_feedback_text.insert(END, str(feedback_record_read)[1:-1])
    show_feedback_text.place(relx=0.05, rely=0.35, relwidth=0.80, relheight=0.30)

    back_button = PhotoImage(file="graphics/next-button.png")
    admin_view_feedback_record_back_button = Button(admin_view_feedback_screen, image=back_button, borderwidth=0, command=view_admin_view_feedback_record_success_screen)
    admin_view_feedback_record_back_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    admin_view_feedback_screen.mainloop()

def view_admin_view_feedback_record_success_screen():
    logging.info("CUR-VIEW_ADMIN_VIEW_FEEDBACK_RECORD_SUCCESS_SCREEN")
    admin_view_feedback_screen.destroy()

def admin_generate_2fa():
    # listing details error
    logging.info("CUR-ADMIN_GENERATE_2FA")
    global admin_generate_2fa_screen
    admin_generate_2fa_screen = Toplevel(admin_view_screen)
    admin_generate_2fa_screen.title("Generate Security Key")
    admin_generate_2fa_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_generate_2fa_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    res = []
    for i in range(10):
        res.append("".join(random.choices(string.ascii_uppercase + string.digits, k=6)))

    file = open("regiskey/regiskey.txt", "w")
    for i in range(10):
        file.write(res[i] + "\n")
    file.close()

    admin_generate_2fa_text = Label(admin_generate_2fa_screen, text="New 2FA key generated!", fg="#212828", bg="#ffffff")
    admin_generate_2fa_text.place(relx=0.50, rely=0.10, anchor=N)

    admin_generate_2fa_button_image = PhotoImage(file="graphics/next-button.png")
    admin_generate_2fa_button = Button(admin_generate_2fa_screen, image=admin_generate_2fa_button_image, borderwidth=0, command=delete_generate_2fa_screen)
    admin_generate_2fa_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    admin_generate_2fa_screen.mainloop()

def delete_generate_2fa_screen():
    logging.info("CUR-DELETE_GENERATE_2FA_SCREEN")
    admin_generate_2fa_screen.destroy()

def admin_view_2fa():
    # listing details error
    logging.info("CUR-ADMIN_VIEW_2FA")
    global admin_view_2fa_screen
    admin_view_2fa_screen = Toplevel(admin_view_screen)
    admin_view_2fa_screen.title("View Security Key")
    admin_view_2fa_screen.geometry("400x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-06-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(admin_view_2fa_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    if len(os.listdir("regiskey")) != 0:
        file = open("regiskey/regiskey.txt", "r")
        list_of_rkey = file.read().splitlines()
        file.close()

        admin_view_2fa_text = Text(admin_view_2fa_screen, fg="#212828", bg="#ffffff")
        for i in range (10):
            admin_view_2fa_text.insert(END, str(list_of_rkey[i]) + "\n")
        admin_view_2fa_text.place(relx=0.05, rely=0.10, relwidth=0.80, relheight=0.30)

    else:
        list_of_rkey = ""

    admin_view_2fa_button_image = PhotoImage(file="graphics/next-button.png")
    admin_view_2fa_button = Button(admin_view_2fa_screen, image=admin_view_2fa_button_image, borderwidth=0, command=delete_view_2fa_screen)
    admin_view_2fa_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    admin_view_2fa_screen.mainloop()

def delete_view_2fa_screen():
    logging.info("CUR-DELETE_VIEW_2FA_SCREEN")
    admin_view_2fa_screen.destroy()

def admin_view_sales():
    # view sales details
    logging.info("CUR-ADMIN_VIEW_SALES")
    global view_sales_screen
    view_sales_screen = Toplevel(admin_view_screen)
    view_sales_screen.title("View sales")
    view_sales_screen.geometry("1900x960")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-08-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(view_sales_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    list_of_sales = os.listdir("credentials/")

    big_inventory = []
    for i in range(len(list_of_sales)):
        inventory = []
        content = time.ctime((os.path.getctime("credentials/" + list_of_sales[i])))
        inventory.append(list_of_sales[i])
        inventory.append(str(datetime.strptime(content, "%a %b %d %H:%M:%S %Y")))
        big_inventory.append(inventory)

    admin_view_vendor_sales_name = Label(view_sales_screen, text="Vendor", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_sales_name.place(relx=0.05, rely=0.10, relwidth=0.20, relheight=0.06)
    admin_view_vendor_sales_date = Label(view_sales_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_sales_date.place(relx=0.30, rely=0.10, relwidth=0.20, relheight=0.06)
    admin_view_vendor_sales_date = Label(view_sales_screen, text="Vendor", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    admin_view_vendor_sales_date.place(relx=0.52, rely=0.10, relwidth=0.20, relheight=0.06)

    sales_record_directory = os.listdir("sales_record")

    sales_record_vendor = []
    sales_record_product = []
    sales_record_quantity = []

    sales_record_count = len(sales_record_directory)

    if sales_record_count != 0:
        for i in range(len(sales_record_directory)):
            sales_record_directory_file = os.listdir("sales_record/" + sales_record_directory[i])
            for j in range(len(sales_record_directory_file)):
                sales_record_file = open("sales_record/" + sales_record_directory[i] + "/" + sales_record_directory_file[j], "r")
                sales_record_qty = sales_record_file.readlines()[0]
                sales_record_file.close()

                sales_record_vendor.append(sales_record_directory[i])
                sales_record_product.append(sales_record_directory_file[i].split("__")[0])
                sales_record_quantity.append(sales_record_qty)

        sales_record_vendor_copy1 = sales_record_vendor.copy()
        sales_record_product_copy1 = sales_record_product.copy()
        sales_record_quantity_copy1 = sales_record_quantity.copy()

        top1_sales_index = sales_record_quantity.index(max(sales_record_quantity))
        sales_record_vendor_copy2 = sales_record_vendor.copy()
        sales_record_product_copy2 = sales_record_product.copy()
        sales_record_quantity_copy2 = sales_record_quantity.copy()

        del sales_record_vendor[top1_sales_index]
        del sales_record_product[top1_sales_index]
        del sales_record_quantity[top1_sales_index]

        if sales_record_count > 1:
            top2_sales_index = sales_record_quantity.index(max(sales_record_quantity))
            sales_record_vendor_copy3 = sales_record_vendor.copy()
            sales_record_product_copy3 = sales_record_product.copy()
            sales_record_quantity_copy3 = sales_record_quantity.copy()

            if sales_record_count > 2:
                del sales_record_vendor[top2_sales_index]
                del sales_record_product[top2_sales_index]
                del sales_record_quantity[top2_sales_index]

                top3_sales_index = sales_record_quantity.index(max(sales_record_quantity))

        view_sales_top1_product = Label(view_sales_screen, text="Top 1", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
        view_sales_top1_product.place(relx=0.05, rely=0.20, relwidth=0.20, relheight=0.04)
        view_sales_top1_product_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
        view_sales_top1_product_text.insert(END, str(sales_record_quantity_copy1[top1_sales_index]))
        view_sales_top1_product_text.place(relx=0.30, rely=0.20, relwidth=0.20, relheight=0.04)
        view_sales_top1_vendor_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
        view_sales_top1_vendor_text.insert(END, str(sales_record_vendor_copy1[top1_sales_index]))
        view_sales_top1_vendor_text.place(relx=0.52, rely=0.20, relwidth=0.20, relheight=0.04)

        if sales_record_count > 1:
            view_sales_top2_product = Label(view_sales_screen, text="Top 2", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
            view_sales_top2_product.place(relx=0.05, rely=0.30, relwidth=0.20, relheight=0.04)
            view_sales_top2_product_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
            view_sales_top2_product_text.insert(END, str(sales_record_quantity_copy2[top2_sales_index]))
            view_sales_top2_product_text.place(relx=0.30, rely=0.30, relwidth=0.20, relheight=0.04)
            view_sales_top2_vendor_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
            view_sales_top2_vendor_text.insert(END, str(sales_record_vendor_copy2[top2_sales_index]))
            view_sales_top2_vendor_text.place(relx=0.52, rely=0.30, relwidth=0.20, relheight=0.04)

            if sales_record_count > 2:
                view_sales_top3_product = Label(view_sales_screen, text="Top 3", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
                view_sales_top3_product.place(relx=0.05, rely=0.40, relwidth=0.20, relheight=0.04)
                view_sales_top3_product_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
                view_sales_top3_product_text.insert(END, str(sales_record_quantity_copy3[top3_sales_index]))
                view_sales_top3_product_text.place(relx=0.30, rely=0.40, relwidth=0.20, relheight=0.04)
                view_sales_top3_vendor_text = Text(view_sales_screen, bg="white", fg="black", font=("Roboto", 12, "bold"))
                view_sales_top3_vendor_text.insert(END, str(sales_record_vendor_copy3[top3_sales_index]))
                view_sales_top3_vendor_text.place(relx=0.52, rely=0.40, relwidth=0.20, relheight=0.04)

    back_button = PhotoImage(file="graphics/back.png")
    admin_view_sales_back_button = Button(view_sales_screen, image=back_button, borderwidth=0, bg="#ffffff", command=delete_admin_view_sales)
    admin_view_sales_back_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    view_sales_screen.mainloop()

def delete_admin_view_sales():
    logging.info("CUR-DELETE_ADMIN_VIEW_SALES")
    view_sales_screen.destroy()

def user_view():
    # User view
    logging.info("CUR-USER_VIEW")
    global user_view_screen
    user_view_screen = Toplevel(main_screen)
    user_view_screen.title("Welcome to SVMS")
    user_view_screen.attributes('-fullscreen', True)

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    random_images = ["graphics/user-screen.png", "graphics/user-screen.png"]
    random_image  = random.choice(random_images)
    image = Image.open(random_image)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(user_view_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    user_view_text_right = Label(user_view_screen, text="Welcome back, " + username1 + "!", fg="#ff6c00", bg="#ffffff", font=("Stem-bold", 36, "bold"))
    user_view_text_right.place(relx=0.77, rely=0.20, anchor=CENTER)

    update_profile_button = PhotoImage(file="graphics/user-update-profile.png")
    user_update_profile_button = Button(user_view_screen, image=update_profile_button, borderwidth=0, bg="#ffffff", command=user_update_profile)
    user_update_profile_button.place(relx=0.76, rely=0.30, anchor=CENTER)

    add_listing_button = PhotoImage(file="graphics/user-add-listing.png")
    user_add_listing_button = Button(user_view_screen, image=add_listing_button, borderwidth=0, bg="#ffffff", command=user_add_listing)
    user_add_listing_button.place(relx=0.76, rely=0.40, anchor=CENTER)

    modify_listing_button = PhotoImage(file="graphics/user-modify-listing.png")
    user_modify_listing_button = Button(user_view_screen, image=modify_listing_button, borderwidth=0, bg="#ffffff", command=user_modify_listing)
    user_modify_listing_button.place(relx=0.76, rely=0.50, anchor=CENTER)

    delete_court_button = PhotoImage(file="graphics/user-delete-listing.png")
    user_delete_court_button = Button(user_view_screen, image=delete_court_button, borderwidth=0, bg="#ffffff", command=user_delete_listing)
    user_delete_court_button.place(relx=0.76, rely=0.60, anchor=CENTER)

    feedback_court_button = PhotoImage(file="graphics/user-add-feedback.png")
    user_feedback_court_button = Button(user_view_screen, image=feedback_court_button, borderwidth=0, bg="#ffffff", command=user_add_feedback)
    user_feedback_court_button.place(relx=0.76, rely=0.70, anchor=CENTER)

    payment_court_button = PhotoImage(file="graphics/user-rental-payment.png")
    user_payment_court_button = Button(user_view_screen, image=payment_court_button, borderwidth=0, bg="#ffffff", command=user_rental_payment)
    user_payment_court_button.place(relx=0.76, rely=0.80, anchor=CENTER)

    update_sales_court_button = PhotoImage(file="graphics/user-update-sales.png")
    user_update_sales_court_button = Button(user_view_screen, image=update_sales_court_button, borderwidth=0, bg="#ffffff", command=user_update_sales)
    user_update_sales_court_button.place(relx=0.76, rely=0.90, anchor=CENTER)

    logout_button_image = PhotoImage(file="graphics/logout.png")
    user_logout_button = Button(user_view_screen, image=logout_button_image, borderwidth=0, command=delete_user_view)
    user_logout_button.place(relx=0.50, rely=0.95, anchor=CENTER)

    user_view_screen.mainloop()

def user_update_profile():
    # update/update profile details
    logging.info("CUR-USER_UPDATE_PROFILE")
    global new_profile_label_id_value

    global update_profile_screen, new_profile_label_title_value, new_profile_label_status_value
    update_profile_screen = Toplevel(user_view_screen)
    update_profile_screen.title("Update Profile")
    update_profile_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(update_profile_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    new_profile_label_id = Label(update_profile_screen, text="New Username", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_profile_label_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    new_profile_label_id_value = Entry(update_profile_screen)
    new_profile_label_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    new_profile_label_title = Label(update_profile_screen, text="New Password", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_profile_label_title.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    new_profile_label_title_value = Entry(update_profile_screen)
    new_profile_label_title_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    new_profile_label_status = Label(update_profile_screen, text="New Contact", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_profile_label_status.place(relx=0.05, rely=0.40, relwidth=0.30, relheight=0.08)
    new_profile_label_status_value = Entry(update_profile_screen)
    new_profile_label_status_value.place(relx=0.40, rely=0.40, relwidth=0.50, relheight=0.08)

    new_profile_label_submit_button_image = PhotoImage(file="graphics/submit.png")
    new_profile_label_submit = Button(update_profile_screen, image=new_profile_label_submit_button_image, borderwidth=0, command=update_profile_record)
    new_profile_label_submit.place(relx=0.50, rely=0.90, anchor=CENTER)

    update_profile_screen.mainloop()

def update_profile_record():
    # Update profile record
    logging.info("CUR-UPDATE_PROFILE_RECORD")
    global username_info, new_profile_id, new_profile_title, new_profile_status
    global username1

    new_profile_id     = new_profile_label_id_value.get()
    new_profile_title  = new_profile_label_title_value.get()
    new_profile_status = new_profile_label_status_value.get()
    new_profile_status = new_profile_status.lower()

    os.remove("credentials/" + username1)

    insert_profile_record = open("credentials/" + new_profile_id, "w")
    insert_profile_record.write(new_profile_id + "\n")
    insert_profile_record.write(new_profile_title + "\n")
    insert_profile_record.write(new_profile_status)
    insert_profile_record.close()

    update_profile_record_success()

def update_profile_record_success():
    # profile details modified
    logging.info("CUR-UPDATE_PROFILE_RECORD_SUCCESS")
    global update_profile_record_success_screen
    update_profile_record_success_screen = Toplevel(update_profile_screen)
    update_profile_record_success_screen.title("Update Profile")
    update_profile_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(update_profile_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    update_profile_record_success_text = Label(update_profile_record_success_screen, text="profile record successfully modified.", fg="#212828", bg="#ffffff")
    update_profile_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    update_profile_record_success_button_image = PhotoImage(file="graphics/small-next-button.png")
    update_profile_record_success_button = Button(update_profile_record_success_screen, image=update_profile_record_success_button_image, borderwidth=0, command=delete_update_profile_record_success_screen)
    update_profile_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    update_profile_record_success_screen.mainloop()

def delete_update_profile_record_success_screen():
    logging.info("CUR-DELETE_UPDATE_PROFILE_RECORD_SUCCESS_SCREEN")
    update_profile_record_success_screen.destroy()
    update_profile_screen.destroy()

def user_add_listing():
    # user add new listing
    logging.info("CUR-USER_ADD_LISTING")
    global listing_label_product_id_value, listing_label_product_type_value, listing_label_product_quantity_value, listing_label_product_price_value, listing_label_location_value, listing_label_contact_value

    global add_listing_screen
    add_listing_screen = Toplevel(user_view_screen)
    add_listing_screen.title("Add Listing")
    add_listing_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(add_listing_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    listing_label_product_id = Label(add_listing_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_product_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    listing_label_product_id_value = Entry(add_listing_screen)
    listing_label_product_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    listing_label_product_type = Label(add_listing_screen, text="Product Type", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_product_type.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    listing_label_product_type_value = Entry(add_listing_screen)
    listing_label_product_type_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    listing_label_product_quantity = Label(add_listing_screen, text="Product Quantity", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_product_quantity.place(relx=0.05, rely=0.40, relwidth=0.30, relheight=0.08)
    listing_label_product_quantity_value = Entry(add_listing_screen)
    listing_label_product_quantity_value.place(relx=0.40, rely=0.40, relwidth=0.50, relheight=0.08)

    listing_label_product_price = Label(add_listing_screen, text="Product Price", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_product_price.place(relx=0.05, rely=0.50, relwidth=0.30, relheight=0.08)
    listing_label_product_price_value = Entry(add_listing_screen)
    listing_label_product_price_value.place(relx=0.40, rely=0.50, relwidth=0.50, relheight=0.08)

    listing_label_location = Label(add_listing_screen, text="Location", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_location.place(relx=0.05, rely=0.60, relwidth=0.30, relheight=0.08)
    listing_label_location_value = Entry(add_listing_screen)
    listing_label_location_value.place(relx=0.40, rely=0.60, relwidth=0.50, relheight=0.08)

    listing_label_contact = Label(add_listing_screen, text="Contact", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    listing_label_contact.place(relx=0.05, rely=0.70, relwidth=0.30, relheight=0.08)
    listing_label_contact_value = Entry(add_listing_screen)
    listing_label_contact_value.place(relx=0.40, rely=0.70, relwidth=0.50, relheight=0.08)

    listing_label_submit_button_image = PhotoImage(file="graphics/submit.png")
    listing_label_submit_button = Button(add_listing_screen, image=listing_label_submit_button_image, borderwidth=0, command=add_listing_record)
    listing_label_submit_button.place(relx=0.50, rely=0.90, anchor=CENTER)

    add_listing_screen.mainloop()

def add_listing_record():
    # Insert listing record
    logging.info("CUR-ADD_LISTING_RECORD")
    global listing_product_id, listing_product_type, listing_product_quantity, listing_product_price, listing_location, listing_contact

    listing_product_id       = listing_label_product_id_value.get()
    listing_product_type     = listing_label_product_type_value.get()
    listing_product_quantity = listing_label_product_quantity_value.get()
    listing_product_price    = listing_label_product_price_value.get()
    listing_location         = listing_label_location_value.get()
    listing_contact          = listing_label_contact_value.get()

    create_directory("listing_record/" + username1)

    list_of_listings = os.listdir("listing_record/" + username1)

    if listing_product_id in list_of_listings:
        add_listing_record_error()
    else:
        insert_listing_record = open("listing_record/" + username1 + "/" + listing_product_id, "w")
        insert_listing_record.write(listing_product_id + "\n")
        insert_listing_record.write(listing_product_type + "\n")
        insert_listing_record.write(listing_product_quantity + "\n")
        insert_listing_record.write(listing_product_price + "\n")
        insert_listing_record.write(listing_location + "\n")
        insert_listing_record.write(listing_contact)
        insert_listing_record.close()

        add_listing_record_success()

def add_listing_record_error():
    # listing detail exists
    logging.info("CUR-ADD_LISTING_RECORD_ERROR")
    global add_listing_record_error_screen
    add_listing_record_error_screen = Toplevel(add_listing_screen)
    add_listing_record_error_screen.title("Add Listing")
    add_listing_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(add_listing_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    list_of_listings = os.listdir("listing_record")

    existing_listing_record = open("listing_record/" + username1 + "/" + listing_product_id, "r")
    existing_listing_product_type = existing_listing_record.readlines()[1]
    existing_listing_record.close()

    add_listing_record_error_text = Label(add_listing_record_error_screen, text="Product exists! Please modify record\nProduct ID: " + listing_product_id + "\nProduct Type: " + existing_listing_product_type, fg="#212828", bg="#ffffff")
    add_listing_record_error_text.place(relx=0.50, rely=0.10, anchor=N)

    add_listing_record_error_button_image = PhotoImage(file="graphics/small-next-button.png")
    add_listing_record_error_button = Button(add_listing_record_error_screen, image=add_listing_record_error_button_image, borderwidth=0, command=delete_add_listing_record_error_screen)
    add_listing_record_error_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    add_listing_record_error_screen.mainloop()

def delete_add_listing_record_error_screen():
    logging.info("CUR-DELETE_ADD_LISTING_RECORD_ERROR_SCREEN")
    add_listing_record_error_screen.destroy()

def add_listing_record_success():
    # listing successfully added
    logging.info("CUR-ADD_LISTING_RECORD_SUCCESS")
    global add_listing_record_success_screen
    add_listing_record_success_screen = Toplevel(add_listing_screen)
    add_listing_record_success_screen.title("Add Listing")
    add_listing_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(add_listing_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    add_listing_record_success_text = Label(add_listing_record_success_screen, text="Product record successfully added.", fg="#212828", bg="#ffffff")
    add_listing_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    add_listing_record_success_button_image = PhotoImage(file="graphics/small-next-button.png")
    add_listing_record_success_button = Button(add_listing_record_success_screen, image=add_listing_record_success_button_image, borderwidth=0, command=delete_add_listing_record_success_screen)
    add_listing_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    add_listing_record_success_screen.mainloop()

def delete_add_listing_record_success_screen():
    logging.info("CUR-DELETE_ADD_LISTING_RECORD_SUCCESS_SCREEN")
    add_listing_record_success_screen.destroy()
    add_listing_screen.destroy()

def user_modify_listing():
    # Modify/update listing details
    logging.info("CUR-USER_MODIFY_LISTING")
    global new_listing_label_product_id_value

    global modify_listing_screen
    modify_listing_screen = Toplevel(user_view_screen)
    modify_listing_screen.title("Modify Listing")
    modify_listing_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(modify_listing_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    new_listing_label_product_id = Label(modify_listing_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    new_listing_label_product_id_value = Entry(modify_listing_screen)
    new_listing_label_product_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    check_listing_product_type_submit_button_image = PhotoImage(file="graphics/small-next-button.png")
    check_listing_product_type_submit = Button(modify_listing_screen, image=check_listing_product_type_submit_button_image, borderwidth=0, command=check_modify_listing_record)
    check_listing_product_type_submit.place(relx=0.50, rely=0.90, anchor=CENTER)

    modify_listing_screen.mainloop()

def check_modify_listing_record():
    # Update listing details
    logging.info("CUR-CHECK_MODIFY_LISTING_RECORD")
    global new_listing_label_product_id_value, previous_listing_product_id

    previous_listing_product_id = new_listing_label_product_id_value.get()
    list_of_listings    = os.listdir("listing_record/" + username1 + "/")

    if previous_listing_product_id not in list_of_listings:
        check_modify_listing_record_error()
    else:
        modify_listing_record()

def check_modify_listing_record_error():
    # Update listing details error
    logging.info("CUR-CHECK_MODIFY_LISTING_RECORD_ERROR")
    global check_modify_listing_record_error_screen
    check_modify_listing_record_error_screen = Toplevel(modify_listing_screen)
    check_modify_listing_record_error_screen.title("Modify Listing")
    check_modify_listing_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_modify_listing_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    modify_listing_record_error_text = Label(check_modify_listing_record_error_screen, text="Product not found!", fg="#212828", bg="#ffffff")
    modify_listing_record_error_text.place(relx=0.50, rely=0.10, anchor=N)

    modify_listing_record_error_button_image = PhotoImage(file="graphics/small-next-button.png")
    modify_listing_record_error_button = Button(check_modify_listing_record_error_screen, image=modify_listing_record_error_button_image, borderwidth=0, command=delete_check_modify_listing_record_error_screen)
    modify_listing_record_error_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_modify_listing_record_error_screen.mainloop()

def delete_check_modify_listing_record_error_screen():
    logging.info("CUR-DELETE_CHECK_MODIFY_LISTING_RECORD_ERROR_SCREEN")
    check_modify_listing_record_error_screen.destroy()

def modify_listing_record():
    # Modify listing details
    logging.info("CUR-MODIFY_LISTING_RECORD")
    global new_listing_label_product_id_value, new_listing_label_product_type_value, new_listing_label_product_quantity_value, new_listing_label_product_price_value, new_listing_label_location_value, new_listing_label_contact_value

    new_listing_label_product_id = Label(modify_listing_screen, text="New ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    new_listing_label_product_id_value = Entry(modify_listing_screen)
    new_listing_label_product_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    new_listing_label_product_type = Label(modify_listing_screen, text="New Type", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_type.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    new_listing_label_product_type_value = Entry(modify_listing_screen)
    new_listing_label_product_type_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    new_listing_label_product_quantity = Label(modify_listing_screen, text="New Quantity", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_quantity.place(relx=0.05, rely=0.40, relwidth=0.30, relheight=0.08)
    new_listing_label_product_quantity_value = Entry(modify_listing_screen)
    new_listing_label_product_quantity_value.place(relx=0.40, rely=0.40, relwidth=0.50, relheight=0.08)

    new_listing_label_product_price = Label(modify_listing_screen, text="New Price", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_price.place(relx=0.05, rely=0.50, relwidth=0.30, relheight=0.08)
    new_listing_label_product_price_value = Entry(modify_listing_screen)
    new_listing_label_product_price_value.place(relx=0.40, rely=0.50, relwidth=0.50, relheight=0.08)

    new_listing_label_location = Label(modify_listing_screen, text="New Location", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_location.place(relx=0.05, rely=0.60, relwidth=0.30, relheight=0.08)
    new_listing_label_location_value = Entry(modify_listing_screen)
    new_listing_label_location_value.place(relx=0.40, rely=0.60, relwidth=0.50, relheight=0.08)

    new_listing_label_contact = Label(modify_listing_screen, text="New Contact", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_contact.place(relx=0.05, rely=0.70, relwidth=0.30, relheight=0.08)
    new_listing_label_contact_value = Entry(modify_listing_screen)
    new_listing_label_contact_value.place(relx=0.40, rely=0.70, relwidth=0.50, relheight=0.08)

    new_listing_label_submit_button_image = PhotoImage(file="graphics/submit.png")
    new_listing_label_submit = Button(modify_listing_screen, image=new_listing_label_submit_button_image, borderwidth=0, command=update_listing_record)
    new_listing_label_submit.place(relx=0.50, rely=0.90, anchor=CENTER)

    modify_listing_screen.mainloop()

def update_listing_record():
    # Update listing record
    logging.info("CUR-UPDATE_LISTING_RECORD")
    global new_listing_product_id, new_listing_product_type, new_listing_product_quantity, new_listing_product_price, new_listing_location, new_listing_contact

    new_listing_product_id       = new_listing_label_product_id_value.get()
    new_listing_product_type     = new_listing_label_product_type_value.get()
    new_listing_product_quantity = new_listing_label_product_quantity_value.get()
    new_listing_product_price    = new_listing_label_product_price_value.get()
    new_listing_location         = new_listing_label_location_value.get()
    new_listing_contact          = new_listing_label_contact_value.get()

    os.remove("listing_record/" + username1 + "/" + previous_listing_product_id)

    insert_listing_record = open("listing_record/" + username1 + "/" + new_listing_product_id, "w")
    insert_listing_record.write(new_listing_product_id + "\n")
    insert_listing_record.write(new_listing_product_type + "\n")
    insert_listing_record.write(new_listing_location + "\n")
    insert_listing_record.write(new_listing_contact)
    insert_listing_record.close()

    modify_listing_record_success()

def modify_listing_record_success():
    # listing details modified
    logging.info("CUR-MODIFY_LISTING_RECORD_SUCCESS")
    global modify_listing_record_success_screen
    modify_listing_record_success_screen = Toplevel(modify_listing_screen)
    modify_listing_record_success_screen.title("Modify Listing")
    modify_listing_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(modify_listing_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    modify_listing_record_success_text = Label(modify_listing_record_success_screen, text="Product record successfully modified.", fg="#212828", bg="#ffffff")
    modify_listing_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    modify_listing_record_success_button_image = PhotoImage(file="graphics/small-next-button.png")
    modify_listing_record_success_button = Button(modify_listing_record_success_screen, image=modify_listing_record_success_button_image, borderwidth=0, command=delete_modify_listing_record_success_screen)
    modify_listing_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    modify_listing_record_success_screen.mainloop()

def delete_modify_listing_record_success_screen():
    logging.info("CUR-DELETE_MODIFY_LISTING_RECORD_SUCCESS_SCREEN")
    modify_listing_record_success_screen.destroy()
    modify_listing_screen.destroy()

def user_delete_listing():
    # Delete listing details
    logging.info("CUR-USER_DELETE_LISTING")
    global new_listing_label_product_id_value

    global delete_listing_screen
    delete_listing_screen = Toplevel(user_view_screen)
    delete_listing_screen.title("Delete Listing")
    delete_listing_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(delete_listing_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    new_listing_label_product_id = Label(delete_listing_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    new_listing_label_product_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    new_listing_label_product_id_value = Entry(delete_listing_screen)
    new_listing_label_product_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    check_listing_submit_button_image = PhotoImage(file="graphics/next-button.png")
    check_listing_label_submit = Button(delete_listing_screen, image=check_listing_submit_button_image, borderwidth=0, command=check_delete_listing_record)
    check_listing_label_submit.place(relx=0.50, rely=0.90, anchor=CENTER)

    delete_listing_screen.mainloop()

def check_delete_listing_record():
    # Verify listing details
    logging.info("CUR-CHECK_DELETE_LISTING_RECORD")
    listing_product_id   = new_listing_label_product_id_value.get()
    list_of_listings = os.listdir("listing_record/" + username1 + "/")

    if listing_product_id not in list_of_listings:
        check_delete_listing_record_error()
    else:
        delete_listing_record()

def check_delete_listing_record_error():
    # listing details error
    logging.info("CUR-CHECK_DELETE_LISTING_RECORD_ERROR")
    global check_delete_listing_record_error_screen
    check_delete_listing_record_error_screen = Toplevel(delete_listing_screen)
    check_delete_listing_record_error_screen.title("Delete Listing")
    check_delete_listing_record_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_delete_listing_record_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    delete_listing_record_failed_text = Label(check_delete_listing_record_error_screen, text="Product not found!", fg="#212828", bg="#ffffff")
    delete_listing_record_failed_text.place(relx=0.50, rely=0.10, anchor=N)

    delete_listing_record_failed_button_image = PhotoImage(file="graphics/small-next-button.png")
    delete_listing_record_failed_button = Button(check_delete_listing_record_error_screen, image=delete_listing_record_failed_button_image, borderwidth=0, command=delete_check_delete_listing_record_error_screen)
    delete_listing_record_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_delete_listing_record_error_screen.mainloop()

def delete_check_delete_listing_record_error_screen():
    logging.info("CUR-DELETE_CHECK_DELETE_LISTING_RECORD_ERROR_SCREEN")
    check_delete_listing_record_error_screen.destroy()

def delete_listing_record():
    # Delete listing details
    logging.info("CUR-DELETE_LISTING_RECORD")
    listing_product_id = new_listing_label_product_id_value.get()
    os.remove("listing_record/" + username1 + "/" + listing_product_id)
    delete_listing_record_success()

def delete_listing_record_success():
    # Listing deleted
    logging.info("CUR-DELETE_LISTING_RECORD_SUCCESS")
    global delete_listing_record_success_screen
    delete_listing_record_success_screen = Toplevel(delete_listing_screen)
    delete_listing_record_success_screen.title("Delete Listing")
    delete_listing_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(delete_listing_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    delete_listing_record_success_text = Label(delete_listing_record_success_screen, text="Product record successfully deleted.", fg="#212828", bg="#ffffff")
    delete_listing_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    delete_listing_record_success_button_image = PhotoImage(file="graphics/small-next-button.png")
    delete_listing_record_success_button = Button(delete_listing_record_success_screen, image=delete_listing_record_success_button_image, borderwidth=0, command=delete_delete_listing_record_success_screen)
    delete_listing_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    delete_listing_record_success_screen.mainloop()

def delete_delete_listing_record_success_screen():
    logging.info("CUR-DELETE_DELETE_LISTING_RECORD_SUCCESS_SCREEN")
    delete_listing_record_success_screen.destroy()
    delete_listing_screen.destroy()

def user_add_feedback():
    # Delete listing details
    logging.info("CUR-USER_ADD_FEEDBACK")
    global feedback_label_text_value

    global user_add_feedback_screen
    user_add_feedback_screen = Toplevel(user_view_screen)
    user_add_feedback_screen.title("Feedback")
    user_add_feedback_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(user_add_feedback_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    feedback_label_text = Label(user_add_feedback_screen, text="Feedback", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    feedback_label_text.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    feedback_label_text_value = Entry(user_add_feedback_screen)
    feedback_label_text_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.30)

    feedback_text_submit_button_image = PhotoImage(file="graphics/next-button.png")
    feedback_text_label_text_submit = Button(user_add_feedback_screen, image=feedback_text_submit_button_image, borderwidth=0, command=user_add_feedback_record)
    feedback_text_label_text_submit.place(relx=0.50, rely=0.90, anchor=CENTER)

    user_add_feedback_screen.mainloop()

def user_add_feedback_record():
    # Verify listing details
    logging.info("CUR-USER_ADD_FEEDBACK_RECORD")
    feedback_text = feedback_label_text_value.get()

    insert_feedback_record = open("feedback/" + username1, "w")
    insert_feedback_record.write(feedback_text)
    insert_feedback_record.close()

    add_feedback_record_success()

def add_feedback_record_success():
    # listing deleted
    logging.info("CUR-ADD_FEEDBACK_RECORD_SUCCESS")
    global add_feedback_record_success_screen
    add_feedback_record_success_screen = Toplevel(user_add_feedback_screen)
    add_feedback_record_success_screen.title("Feedback")
    add_feedback_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(add_feedback_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    add_feedback_record_success_text = Label(add_feedback_record_success_screen, text="Feedback successfully added.", fg="#212828", bg="#ffffff")
    add_feedback_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    add_feedback_record_success_button_image = PhotoImage(file="graphics/next-button.png")
    add_feedback_record_success_button = Button(add_feedback_record_success_screen, image=add_feedback_record_success_button_image, borderwidth=0, command=delete_add_feedback_record_success_screen)
    add_feedback_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    add_feedback_record_success_screen.mainloop()

def delete_add_feedback_record_success_screen():
    logging.info("CUR-DELETE_ADD_FEEDBACK_RECORD_SUCCESS_SCREEN")
    add_feedback_record_success_screen.destroy()
    user_add_feedback_screen.destroy()

def user_rental_payment():
    # Checkout payment
    logging.info("CUR-USER_RENTAL_PAYMENT")
    global rental_payment_screen
    rental_payment_screen = Toplevel(user_view_screen)
    rental_payment_screen.title("Rental Payment")
    rental_payment_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/tng_square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(rental_payment_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    """
    rental_payment_label_payment_card_number = Label(rental_payment_screen, text="Card Number", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    rental_payment_label_payment_card_number.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    rental_payment_label_payment_card_number_value = Entry(rental_payment_screen)
    rental_payment_label_payment_card_number_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    rental_payment_label_payment_card_name = Label(rental_payment_screen, text="Full Name", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    rental_payment_label_payment_card_name.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    rental_payment_label_payment_card_name_value = Entry(rental_payment_screen)
    rental_payment_label_payment_card_name_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    rental_payment_label_payment_card_cvv = Label(rental_payment_screen, text="CVV", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    rental_payment_label_payment_card_cvv.place(relx=0.05, rely=0.40, relwidth=0.30, relheight=0.08)
    rental_payment_label_payment_card_cvv_value = Entry(rental_payment_screen)
    rental_payment_label_payment_card_cvv_value.place(relx=0.40, rely=0.40, relwidth=0.50, relheight=0.08)

    rental_payment_label_payment_card_exp = Label(rental_payment_screen, text="Expiration", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    rental_payment_label_payment_card_exp.place(relx=0.05, rely=0.50, relwidth=0.30, relheight=0.08)
    rental_payment_label_payment_card_exp_value = Entry(rental_payment_screen)
    rental_payment_label_payment_card_exp_value.place(relx=0.40, rely=0.50, relwidth=0.50, relheight=0.08)

    rental_payment_label_payment_card_amount = Label(rental_payment_screen, text="Amount (RM)", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    rental_payment_label_payment_card_amount.place(relx=0.05, rely=0.60, relwidth=0.30, relheight=0.08)
    rental_payment_label_payment_card_amount_value = Entry(rental_payment_screen)
    rental_payment_label_payment_card_amount_value.place(relx=0.40, rely=0.60, relwidth=0.50, relheight=0.08)
    """

    global rental_payment_submit_button_image

    rental_payment_submit_button_image = PhotoImage(file="graphics/next-button.png")
    rental_payment_submit_button = Button(rental_payment_screen, image=rental_payment_submit_button_image, borderwidth=0, command=check_payment_loading)
    rental_payment_submit_button.image = rental_payment_submit_button_image
    rental_payment_submit_button.place(relx=0.50, rely=0.90, anchor=CENTER)

def check_payment_loading():
    # Court payment
    logging.info("CUR-CHECK_PAYMENT_LOADING")
    global check_payment_loading_screen
    check_payment_loading_screen = Toplevel(rental_payment_screen)
    check_payment_loading_screen.title("Rental Payment")
    check_payment_loading_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_payment_loading_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    check_payment_label_invoice_number = Label(check_payment_loading_screen, text="Invoice Number", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    check_payment_label_invoice_number.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    check_payment_label_invoice_number_value = Entry(check_payment_loading_screen)
    check_payment_label_invoice_number_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    check_payment_label_payment_amount = Label(check_payment_loading_screen, text="Payment Amount (RM)", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    check_payment_label_payment_amount.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    check_payment_label_payment_amount_value = Entry(check_payment_loading_screen)
    check_payment_label_payment_amount_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    global check_payment_submit_button_image

    check_payment_submit_button_image = PhotoImage(file="graphics/next-button.png")
    check_payment_submit_button = Button(check_payment_loading_screen, image=check_payment_submit_button_image, borderwidth=0, command=check_payment)
    check_payment_submit_button.image = check_payment_submit_button_image
    check_payment_submit_button.place(relx=0.50, rely=0.90, anchor=CENTER)


    check_payment_loading_screen.mainloop()

def check_payment():
    # Court payment
    logging.info("CUR-CHECK_PAYMENT")
    check_payment_loading_screen.destroy()

    global payment_court_record_success_screen
    payment_court_record_success_screen = Toplevel(rental_payment_screen)
    payment_court_record_success_screen.title("Rental Payment")
    payment_court_record_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(payment_court_record_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    payment_court_record_success_text = Label(payment_court_record_success_screen, text="Payment successfully!", fg="#212828", bg="#ffffff")
    payment_court_record_success_text.place(relx=0.50, rely=0.10, anchor=N)

    payment_court_record_success_button_image = PhotoImage(file="graphics/next-button.png")
    payment_court_record_success_button = Button(payment_court_record_success_screen, image=payment_court_record_success_button_image, borderwidth=0, command=check_payment_success_screen)
    payment_court_record_success_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    payment_court_record_success_screen.mainloop()

def check_payment_success_screen():
    logging.info("CUR-CHECK_PAYMENT_SUCCESS_SCREEN")
    payment_court_record_success_screen.destroy()
    rental_payment_screen.destroy()

def user_update_sales():
    # Checkout payment
    logging.info("CUR-USER_UPDATE_SALES")
    global update_sales_label_product_id_value, update_sales_label_product_sold_quantity_value, update_sales_label_product_date_value, update_sales_label_product_sold_date

    global update_sales_screen
    update_sales_screen = Toplevel(user_view_screen)
    update_sales_screen.title("Sales Log")
    update_sales_screen.geometry("600x600")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-01-square.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(update_sales_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    update_sales_label_product_id = Label(update_sales_screen, text="Product ID", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    update_sales_label_product_id.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.08)
    update_sales_label_product_id_value = Entry(update_sales_screen)
    update_sales_label_product_id_value.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.08)

    update_sales_label_product_sold_quantity = Label(update_sales_screen, text="Quantity", bg="black", fg="white", font=("Roboto", 16, "bold"), anchor=W)
    update_sales_label_product_sold_quantity.place(relx=0.05, rely=0.30, relwidth=0.30, relheight=0.08)
    update_sales_label_product_sold_quantity_value = Entry(update_sales_screen)
    update_sales_label_product_sold_quantity_value.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.08)

    update_sales_label_product_sold_date = Calendar(update_sales_screen, selectmode="day", year=2023, month=3, day=1, date_pattern="yyyy-mm-dd")
    update_sales_label_product_sold_date.place(relx=0.40, rely=0.40)

    def grad_date():
        which_date = date.config(text="Date is: " + update_sales_label_product_sold_date.get_date())

    update_sales_label_product_date_value = Button(update_sales_screen, text="Get Date", command=grad_date)
    update_sales_label_product_date_value.place(relx=0.50, rely=0.82, anchor=CENTER)
    date = Label(update_sales_screen, text="")
    date.pack(pady=20)

    global update_sales_submit_button_image
    update_sales_submit_button_image = PhotoImage(file="graphics/next-button.png")
    update_sales_submit_button = Button(update_sales_screen, image=update_sales_submit_button_image, borderwidth=0, command=check_product_id)
    update_sales_submit_button.image = update_sales_submit_button_image
    update_sales_submit_button.place(relx=0.50, rely=0.90, anchor=CENTER)

def check_product_id():
    logging.info("CUR-CHECK_PRODUCT_ID")
    listing_product_id   = update_sales_label_product_id_value.get()
    list_of_listings = os.listdir("listing_record/" + username1 + "/")

    if listing_product_id not in list_of_listings:
        check_product_id_error()
    else:
        check_product_id_success()

def check_product_id_error():
    # listing details error
    logging.info("CUR-CHECK_PRODUCT_ID_ERROR")
    global check_product_id_error_screen
    check_product_id_error_screen = Toplevel(update_sales_screen)
    check_product_id_error_screen.title("Sales Log")
    check_product_id_error_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_product_id_error_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    delete_listing_record_failed_text = Label(check_product_id_error_screen, text="Product not found!", fg="#212828", bg="#ffffff")
    delete_listing_record_failed_text.place(relx=0.50, rely=0.10, anchor=N)

    delete_listing_record_failed_button_image = PhotoImage(file="graphics/small-next-button.png")
    delete_listing_record_failed_button = Button(check_product_id_error_screen, image=delete_listing_record_failed_button_image, borderwidth=0, command=delete_check_product_id_error_screen)
    delete_listing_record_failed_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_product_id_error_screen.mainloop()

def delete_check_product_id_error_screen():
    logging.info("CUR-DELETE_CHECK_PRODUCT_ID_ERROR_SCREEN")
    check_product_id_error_screen.destroy()

def check_product_id_success():
    # listing details error
    logging.info("CUR-CHECK_PRODUCT_ID_SUCCESS")
    global check_product_id_success_screen
    check_product_id_success_screen = Toplevel(update_sales_screen)
    check_product_id_success_screen.title("Sales Log")
    check_product_id_success_screen.geometry("400x100")

    def resize_image(event):
        new_width  = event.width
        new_height = event.height
        image      = copy_of_image.resize((new_width, new_height))
        photo      = ImageTk.PhotoImage(image)
        label.config(image=photo)
        # Avoid garbage collection
        label.image= photo

    image = Image.open("graphics/background-03-long.png")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(check_product_id_success_screen, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    if not os.path.exists("sales_record/" + username1):
        os.makedirs("sales_record/" + username1)

    insert_product_sales = open("sales_record/" + username1 + "/" + update_sales_label_product_id_value.get() + "__" + update_sales_label_product_sold_date.get_date(), "w")
    insert_product_sales.write(update_sales_label_product_id_value.get())
    insert_product_sales.close()

    check_product_id_success_text = Label(check_product_id_success_screen, text="Sales record added successfully!", fg="#212828", bg="#ffffff")
    check_product_id_success_text.place(relx=0.50, rely=0.10, anchor=N)

    check_product_id_success_text_button_image = PhotoImage(file="graphics/small-next-button.png")
    check_product_id_success_text_button = Button(check_product_id_success_screen, image=check_product_id_success_text_button_image, borderwidth=0, command=delete_check_product_id_success_screen)
    check_product_id_success_text_button.place(relx=0.50, rely=0.80, anchor=CENTER)

    check_product_id_success_screen.mainloop()

def delete_check_product_id_success_screen():
    logging.info("CUR-DELETE_CHECK_PRODUCT_ID_SUCCESS_SCREEN")
    check_product_id_success_screen.destroy()
    update_sales_screen.destroy()

def delete_user_view():
    logging.info("CUR-DELETE_USER_VIEW")
    user_view_screen.destroy()

def create_directory(directory_name):
    logging.info("CUR-CREATE_DIRECTORY")
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def keep_securities():
    logging.info("CUR-KEEP_SECURITIES")
    current_snap = os.listdir("securities/SYSTEM_SNAPS")

    while len(current_snap) > 9:
        snap_to_delete = current_snap.pop(0)
        os.remove("securities/SYSTEM_SNAPS/" + snap_to_delete)

def load_securities():
    logging.info("CUR-LOAD_SECURITIES")
    snap_boot = datetime.now()
    snap_time = snap_boot.strftime("SNAP%Y_%m_%d_%HHOUR%MMIN%SSECOND")
    snap_path = "securities/SYSTEM_SNAPS/" + snap_time + ".zip"

    zippy = zipfile.ZipFile(snap_path, "w")
    for dirname, subdirs, files in os.walk("./"):
        if ".idea" in subdirs:
            subdirs.remove(".idea")
        if "securities" in subdirs:
            subdirs.remove("securities")

        zippy.write(dirname)

        for filename in files:
            zippy.write(os.path.join(dirname, filename))
    zippy.close()

if __name__ == "__main__":
    logging.basicConfig(
        filename = "securities/SYSTEM_LOGS/SYSTEM_ROOT_LOG",
        filemode = "a",
        format   = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt  = "%H:%M:%S",
        level    = logging.DEBUG
    )

    logging.info("CUR-SYSTEM STARTUP")
    keep_securities()
    load_securities()
    main_account_screen()
    logger = logging.getLogger("SVMS")

# EOF
