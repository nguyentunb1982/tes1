import serial.tools.list_ports
import subprocess
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p)
from tkinter import *
def clicked():
     
    lbl.configure(text="Button was clicked !!")
    subprocess.call("C:/Program Files (x86)/AtHomeVideoStreamer/AtHomeVideoStreamer.exe",shell=True)
window = Tk()

window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Đi chợ", font=("Arial Bold", 50))
btn = Button(window, text="Click Tôi", font =("Arial Bold", 10), bg="green", fg="red", command=clicked)
btn.grid(column=1, row=0)
lbl.grid(column=0, row=0)
window.mainloop()
pridisia
