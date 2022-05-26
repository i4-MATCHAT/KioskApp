#구매 완료 page
from ctypes.wintypes import SIZE
import tkinter as tk
import tkinter.font
import RPi.GPIO as GPIO
from time import sleep
import time
import requests
import json
import buy
from buy import save_key

window=tk.Tk()
window.title("MATCHAT")
window.geometry('800x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')

font=tkinter.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font2=tkinter.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)

#GPIO 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)   #gpio핀들의 번호를 지정하는 규칙 설정
GPIO.setup(12,GPIO.OUT)     #서보핀을 출력으로 설정
p=GPIO.PWM(12,50)   #서보핀을 PWM모드 50hz로 사용
p.start(0)



state=2
key=buy.save_key


#잠금 닫힘,구매 완료 상태(3)로 변화 requests
def lock_close():
    p.ChangeDutyCycle(7.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    r = requests.post("http://ec2-3-39-141-76.ap-northeast-2.compute.amazonaws.com/api_finish/result/",
                    json={ "state" : state, "key" : key } )
    text = r.text
    data = json.loads(text)
    time.sleep(2)
    window.destroy()
    import main


label=tk.Label(window, text="   MATCHAT[구매자]", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label.pack()


label2=tk.Label(window,text='상품 수령 후,',bg="#1abc9c",font=font2)
label2.place(x=310,y=120)
label3=tk.Label(window,text='구매확정 버튼을 눌러주세요.',bg="#1abc9c",font=font2)
label3.place(x=220,y=165)

btn=tk.Button(window,text='구매 확정',background='white',width=15,height=2,font=font2,command=lock_close)
btn.place(x=290,y=290)


window.mainloop()
