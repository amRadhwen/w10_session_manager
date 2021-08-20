from tkinter import Tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Button
from os import system
from tkinter import messagebox


#callBack functions
def shutdown(event):
    response = messagebox.askyesno("Shutodwn", "Are you shure ?")
    if response:
        system("shutdown /s /t 0")
        messagebox.showwarning("Shutdown", "Windows will stop...")

def reboot(event):
    response = messagebox.askyesno("Reboot", "Are you shure ?")
    if response:
        system("shutdown /r")
        messagebox.showwarning("Reboot", "Windows will restart...")


def hibernate(event):
    response = messagebox.askyesno("Hibernate", "Are you shure ?")
    if response:
        system("shutdown /h")

def logoff(event):
    response = messagebox.askyesno("LogOff", "Are you shure ?")
    if response:
        system("shutdown /l")
        messagebox.showwarning("Logoff", "Session will end...")

def lock(event):
    response = messagebox.askyesno("Lock", "Are you shure ?");
    if response:
        system("rundll32.exe user32.dll,LockWorkStation")

def abort(event):
    system("shutdown /a")
    messagebox.showinfo("Shutdown operation aborted", "Shutdown operation aborted")

#root
root = Tk();

#main window config
root.resizable(False, False);
root.wm_iconbitmap("./files/icon/windows.ico")
root.title("Windows 10 Session Manager")


#images
shutdown_img = PhotoImage(file = "./files/images/shutdown.png").subsample(5, 5)
reboot_img = PhotoImage(file = r"./files/images/reboot.png").subsample(5, 5)
hibernate_img = PhotoImage(file = r"./files/images/hibernate.png").subsample(5, 5)
logoff_img = PhotoImage(file = r"./files/images/logoff.png").subsample(5, 5)
lock_img = PhotoImage(file = r"./files/images/lock.png").subsample(5, 5)
abort_img = PhotoImage(file = r"./files/images/abort.png").subsample(5, 5)

#buttons
shutdown_button = Button(root, text="Shutdown", image=shutdown_img)
reboot_button = Button(root, text="Reboot", image=reboot_img)
hibernate_button = Button(root, text="Hibernate", image=hibernate_img)
logoff_button = Button(root, text="Logoff", image=logoff_img)
lock_button = Button(root, text="Lock", image=lock_img)
abort_button = Button(root, text="Abort", image=abort_img)

#buttons align
shutdown_button.grid(column=0, row=0, padx=5, pady=5)
reboot_button.grid(column=1, row=0, padx=5, pady=5)
hibernate_button.grid(column=2, row=0, padx=5, pady=5)
logoff_button.grid(column=3, row=0, padx=5, pady=5)
lock_button.grid(column=4, row=0, padx=5, pady=5)
abort_button.grid(column=5, row=0, padx=5, pady=5)

#event listeners
shutdown_button.bind("<Button-1>", shutdown);
reboot_button.bind("<Button-1>", reboot);
hibernate_button.bind("<Button-1>", hibernate);
logoff_button.bind("<Button-1>", logoff);
lock_button.bind("<Button-1>", lock);
abort_button.bind("<Button-1>", abort);



#main
if __name__ == "__main__":
    root.mainloop()