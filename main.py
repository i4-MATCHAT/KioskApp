#main_page

from ctypes.wintypes import SIZE
import tkinter as tk
import tkinter.font


window=tk.Tk()
window.title("MATCHAT")
window.geometry('800x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')

font=tkinter.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font2=tkinter.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)

#구매자
def click_buy():
    window.destroy()
    import buy 


#판매자
def click_sale():
    window.destroy()
    import sale


label=tk.Label(window, text="   MATCHAT", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label.pack()
bt1=tk.Button(window,text="구매자",font=font,background='white',width=15,height=5,command=click_buy)
bt1.place(x=430,y=200)
bt2=tk.Button(window,text="판매자",font=font,background='white',width=15,height=5,command=click_sale)
bt2.place(x=160,y=200)
window.mainloop()
