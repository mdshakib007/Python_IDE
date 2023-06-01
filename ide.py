from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import os
import subprocess
import webbrowser

root = Tk()
root.title("*Untitled  -  J-iDE")
root.geometry("1280x770+150+50")
root.configure(bg='grey')
root.resizable(False, False)

file = None


### menu commands
def new_file():
    root.title("*Untitled  -  J-iDE")
    code_area.delete(1.0, END)


def python_file():
    pass


def open_file():
    global file 
    
    file = askopenfilename(defaultextension="*.py", 
                           filetypes=[
                               ("Python Files", "*.py"), 
                               ("Text Document", "*.txt"), 
                               ("Other Files", "*.*")
                           ])
    
    with open(file, 'r') as f:
        content = f.read()
        code_area.delete(1.0, END)
        code_area.insert(1.0, content)
        
        root.title(os.path.basename(file) + "  -  J-iDE")


def save_file():
    global file
    
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.py", 
                                 defaultextension='.py', 
                                 filetypes=[
                                     ("Python File", "*.py"),
                                     ("Text Document", "*.txt"),
                                     ("Other Files", "*.*")
                                 ])
        
        if file == "":
            file = None
        else:
            f = open(file, 'w') 
            f.write(code_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "  -  J-iDE")
        
    else:
        f = open(file, 'w')
        f.write(code_area.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "  -  JiDE")



def save_as():
    global file 
    
    file = asksaveasfilename(defaultextension=".py", 
                             filetypes=[
                                 ("python File", "*.py"), 
                                 ("Text Document", "*.txt"), 
                                 ("Other Files", "*.*")
                             ])
    
    with open(file, "w") as f:
        content = code_area.get(1.0, END)
        f.write(content)
        
        root.title(os.path.basename(file) + "  -  J-iDE")
    



### work of commands
def select_language():
    messagebox.showinfo("Language", "Python was found! We cannot find other languages!")
    
    
    
def run_file():
    global file
    
    if file is None:
        save = messagebox.askquestion("Save", "You need to save first. Do you want to save the file?")
        if save == "yes":
            save_file()
        else:
            return  # If the user chooses not to save, return without running the file

    command = f"python3 {file}"  # Add "python3" before the file path
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    show_output.insert(END, output)  # Use END instead of 1.0 to insert at the end of the text widget
    show_output.insert(END, error)



def settings():
    messagebox.showerror("Settings", "This feature is not completed yet! (comming soon)")


def python():
    pass


def user_id():
    pass


def github_profile():
    webbrowser.open("https://github.com/mdshakib007")


def information():
    messagebox.showinfo("Information", "This is very simple IDE, made with python(Tkinter).")


def exit_window():
    ask = messagebox.askokcancel("Exit", "Are you sure to Exit?")
    
    if ask:
        root.destroy() 
        
    else:
        pass
    
    
def edit_undo():
    pass


def edit_redo():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def expand_output():
    pass
    
    
def max_window():
    pass


def how_work():
    pass


def all_command():
    pass


def source_code():
    pass


def report():
    pass
    

def about():
    pass
    
######## Menu
### File menu ###
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=False)

file_menu.add_command(label="New File", accelerator="Ctrl+N", command=new_file)
file_menu.add_command(label="Python File", accelerator="Ctrl+P", command=python_file)
file_menu.add_command(label="Open file", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save as...", accelerator="Ctrl+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=exit_window)

main_menu.add_cascade(menu=file_menu, label="File", font="Arial 13")


### Edit Menu
edit_menu = Menu(main_menu, tearoff=False)

edit_menu.add_command(label="Undo", accelerator='Ctrl+Z', command=edit_undo)
edit_menu.add_command(label="Redo", accelerator='Ctrl+Y', command=edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator='Ctrl+X', command=cut)
edit_menu.add_command(label="Copy", accelerator='Ctrl+C', command=copy)
edit_menu.add_command(label="Paste", accelerator='Ctrl+V', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Expand Output Window", accelerator='Ctrl+E', command=expand_output)
edit_menu.add_command(label="Max Window", accelerator='Alt+M', command=max_window)
edit_menu.add_command(label="Exit", accelerator='Ctrl+Q', command=exit_window)

main_menu.add_cascade(menu=edit_menu, label='Edit', font='Arial 13')


### Run Menu
run_menu = Menu(main_menu, tearoff=0)

run_menu.add_command(label='Start Debugging', accelerator='Ctrl+R', command=run_file)
run_menu.add_command(label='Run Without Debugging', accelerator='Ctrl+R', command=run_file)
run_menu.add_separator()
run_menu.add_command(label='Quit', accelerator='Ctrl+Q', command=exit_window)

main_menu.add_cascade(menu=run_menu, label='Run', font='Arial 13')


### Help menu
help_menu = Menu(main_menu, tearoff=0)

help_menu.add_command(label="How It's Work?", command=how_work)
help_menu.add_command(label="Show All Commands...", command=all_command)
help_menu.add_command(label="Source Code", command=source_code)
help_menu.add_separator()
help_menu.add_command(label="Report...", command=report)
help_menu.add_command(label="About", command=about)

main_menu.add_cascade(menu=help_menu, label="Help", font='Arial 13')

root.config(menu=main_menu)



# code area
code_area = Text(root, font='consolas 14')
code_area.place(x=120, y=0, width=1150, height=770)

# output
show_output = Text(root, font='consolas 12', bg='black', fg='lightgreen')
show_output.place(x=120, y=600, width=1150, height=300)


### buttons ###

# select language 
select = Image.open("images/language.png")
s_res = select.resize((60, 60))
se_lang = ImageTk.PhotoImage(image=s_res)
se_btn = Button(root, image=se_lang, bg='grey', command=select_language)
se_btn.place(x=25, y=100)

# run 
run_ = Image.open("images/run.png")
run_res = run_.resize((60, 60))
run = ImageTk.PhotoImage(image=run_res)
run_btn = Button(root, image=run, bg='grey', command=run_file)
run_btn.place(x=25, y=170)

# settings
setting_ = Image.open("images/settings.png")
setting_res = setting_.resize((60, 60))
setting = ImageTk.PhotoImage(image=setting_res)
setting_btn = Button(root, image=setting, bg='grey', command=settings)
setting_btn.place(x=25, y=240)

# python
py_ = Image.open("images/py.png")
py_res = py_.resize((60, 60))
py = ImageTk.PhotoImage(image=py_res)
py_btn = Button(root, image=py, bg='grey', command=python)
py_btn.place(x=25, y=310)

# user 
user_ = Image.open("images/user.png")
user_res = user_.resize((60, 60))
user = ImageTk.PhotoImage(image=user_res)
user_btn = Button(root, image=user, bg='grey', command=user_id)
user_btn.place(x=25, y=380)


# github
github_ = Image.open("images/github.png")
github_res = github_.resize((60, 60))
github = ImageTk.PhotoImage(image=github_res)
github_btn = Button(root, image=github, bg='grey', command=github_profile)
github_btn.place(x=25, y=460)

# info
info_ = Image.open("images/info.png")
info_res = info_.resize((60, 60))
info = ImageTk.PhotoImage(image=info_res)
info_btn = Button(root, image=info, bg='grey', command=information)
info_btn.place(x=25, y=530)

# cancel
cancel_ = Image.open("images/cancel.png")
cancel_res = cancel_.resize((60, 60))
cancel = ImageTk.PhotoImage(image=cancel_res)
cancel_btn = Button(root, image=cancel, bg='grey', command=exit_window)
cancel_btn.place(x=25, y=600)


root.mainloop()
