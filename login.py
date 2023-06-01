from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

root = Tk()
root.title('Welcome  -  J-iDE')
root.geometry('800x800+150+50')
root.resizable(False, False)


def get_info():
    master = Tk()
    master.geometry('1000x800')
    master.title("Untitled  -  J-iDE")
    
    
    
    
    master.mainloop()


def log_in():
    root.destroy()
    
    # new window
    window = Tk()
    window.title('Login  -  J-iDE')
    window.geometry('700x700')
    
    l_ = Image.open('images/login.jpg')
    log_res = l_.resize((700, 700))
    login_page = ImageTk.PhotoImage(image=log_res)
    Label(window, image=login_page).place(x=0, y=0)
    
    ### entries for getting username & password
    name = Entry(window, width=16, font='Arial 15').place(x=270, y=332)
    password = Entry(window, width=16, font='Arial 15', show='▪️').place(x=270, y=382)
    
    # login button
    login_btn = ctk.CTkButton(window,
                              text= "SIGN IN",
                              width=120, height=40, 
                              hover_color='#071826', 
                              fg_color='#071826',
                              bg_color='#6bd170',
                              corner_radius=30,
                              command=get_info
                              )
    login_btn.place(x=300, y=430)
    
    window.mainloop()


# frame 
frame1 = Frame(root, width=1000, height=1000)

# load background image and resize
ide_ = Image.open('images/ide.jpg')
ide_res = ide_.resize((800, 800))
ide = ImageTk.PhotoImage(image=ide_res)

Label(frame1, image=ide).place(x=0, y=0)

# loging button
login = Button(frame1, text="Login", font='Roboto 14', bg='#FFF', relief='flat', cursor='hand2', command=log_in).place(x=100, y=100)
signup = Button(frame1, text="Sign Up", font='Roboto 14', bg='#FFF', relief='flat', cursor='hand2', command=log_in).place(x=200, y=100)



frame1.place(x=0, y=0)
    
    
    
    
    
# ide_screen()

root.mainloop()