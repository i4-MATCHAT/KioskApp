import tkinter as tk
import tkinter.font


window=tk.Tk()
window.title("MATCHAT")
window.geometry('635x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')

font=tkinter.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font2=tkinter.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)


label=tk.Label(window, text="   MATCHAT", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label.pack()
window.mainloop()
