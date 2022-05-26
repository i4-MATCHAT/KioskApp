#구매자 인증번호 입력 page
from tkinter import *
import tkinter as tk
from turtle import width
import requests
import json
import tkinter.font
from tkinter import messagebox
import time
import RPi.GPIO as GPIO
from time import sleep


window=tk.Tk()
window.title('MATCHAT')
window.geometry("800x450")
window.configure(background="#1abc9c")
window.resizable(False,False)


#폰트
font=tk.font.Font(family="Consolas",size=15,weight=tk.font.BOLD)
font2=tk.font.Font(family="Consolas",size=20,weight=tk.font.BOLD)

#GPIO 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    #gpio핀들의 번호를 지정하는 규칙 설정
GPIO.setup(12,GPIO.OUT)     #서보핀을 출력으로 설정
p=GPIO.PWM(12,50)          #서보핀을 PWM모드 50hz로 사용
p.start(0)

#--닫히는 코드
# p.ChangeDutyCycle(7.5)
# p.ChangeDutyCycle(12.5)
# time.sleep(1)


equa = ""
equation = tk.StringVar()

def btnPress(num):
    global equa
    buy_key_input.delete(0, tk.END)
    equa = equa + str(num)
    equation.set(equa)   
    buy_key_input.insert(0,  str(equa))
    
    print(equa)


def ClearPress():
    global equa
    equa = ""
    equation.set("")

# def EnterPress():
#     global equa
#     global save_key
#     total = str(eval(equa))
#     equation.set(total)
#     save_key=str(eval(equa))
#     print(type(save_key))
#     print(save_key)
#     window.destroy()
#     import sale_camera


#잠금 열림
def lock_open():
    print('test')
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.stop()


#인증번호 비교
def EnterPress():

    global equa
    global save_key
    total = str(eval(equa))
    equation.set(total)
    save_key=str(eval(equa))
    print(type(save_key))
    print(save_key)
    #결제 완료된 상품의 인증번호가 맞는지 확인   
    url="http://ec2-3-39-94-66.ap-northeast-2.compute.amazonaws.com/api_paycheck/result/"
    r = requests.post(url,
              json={'key': save_key})
    text = r.text
    data = json.loads(text)
    result = data['status']
    print(result)
    print(type(result))
        
        # 상품 결제 완료==2
    if result ==str(1):
        lock_open()       
        window.destroy()
        import buy_success
    elif result == str(2):
        messagebox.showwarning('warning','없는 인증번호 입니다.')
    else:
        messagebox.showwarning('warning','결제 완료된 상품이 아닙니다.')



 




label1=tk.Label(window, text="   MATCHAT[구매자]", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label1.pack()



buy_key_label=tk.Label(window,text="인증번호를 입력해주세요 : ",bg="#1abc9c",font=font2)
buy_key_label.place(x=50,y=90)
buy_key_input=tk.Entry(window,width=10,insertwidth=10,bg="#1abc9c",font=font2)
buy_key_input.place(x=400,y=90)


Button1 = tk.Button(window, text="1", bg='white',command=lambda: btnPress(1), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button1.place(x=120,y=160)
Button2 = tk.Button(window, text="2", bg='white',command=lambda: btnPress(2), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button2.place(x=240,y=160)
Button3 = tk.Button(window, text="3", bg='white',command=lambda: btnPress(3), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button3.place(x=360,y=160)
Button4 = tk.Button(window, text="4", bg='white',command=lambda: btnPress(4), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button4.place(x=120,y=230)
Button5 = tk.Button(window, text="5", bg='white',command=lambda: btnPress(5), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button5.place(x=240,y=230)
Button6 = tk.Button(window, text="6", bg='white',command=lambda: btnPress(6), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button6.place(x=360,y=230)
Button7 = tk.Button(window, text="7", bg='white',command=lambda: btnPress(7), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button7.place(x=120,y=300)
Button8 = tk.Button(window, text="8", bg='white',command=lambda: btnPress(8), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button8.place(x=240,y=300)
Button9 = tk.Button(window, text="9", bg='white',command=lambda: btnPress(9), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button9.place(x=360,y=300)
Button0 = tk.Button(window, text="0", bg='white',command=lambda: btnPress(0), height=3, width=15, borderwidth=1, relief=tk.SOLID)
Button0.place(x=240,y=370)
#clear버튼

Clear = tk.Button(window, text="C", bg='white',command=ClearPress, height=3, width=15, borderwidth=1, relief=tk.SOLID)
Clear.place(x=120,y=370)

#enter 버튼(확인)
Enter = tk.Button(window, text="확인", bg='white',command=EnterPress, height=3, width=15, borderwidth=1, relief=tk.SOLID)
Enter.place(x=360,y=370)


window.mainloop()