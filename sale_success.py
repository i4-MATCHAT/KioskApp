#판매 등록 완료 page
import tkinter as tk
import tkinter
import tkinter.font
import sale_camera
from sale_camera import kiosk_result
from PIL import ImageTk,Image

window=tk.Tk()
window.title("MATCHAT")
window.geometry('800x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')

font=tk.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font1=tk.font.Font(family="Consolas",size=13,weight=tkinter.font.BOLD)
font2=tk.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)


photo=Image.open('/home/pi/save_folder/product.jpg')
photo_resize=photo.resize((250,200))
photo_resize.save('/home/pi/save_folder/product_resize.jpg')
img=ImageTk.PhotoImage(photo_resize)



label=tk.Label(window, text="   MATCHAT[판매자]", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label.pack()

label2=tk.Label(window,text='* 상품명 : '+kiosk_result,bg="#1abc9c",font=font1)
label2.place(x=70,y=85)
label3=tk.Label(window,text='동일 상품으로 상품 등록이 완료되었습니다.',bg="#1abc9c",font=font1)
label3.place(x=70,y=130)

label4=tk.Label(window,image=img)
label4.place(x=90,y=160)

btn=tk.Button(window,text='확인',background='white',width=8,height=1,font=font2)
btn.place(x=315,y=375)


window.mainloop()
