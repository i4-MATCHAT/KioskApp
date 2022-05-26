#상품 촬영 page
from ctypes.wintypes import SIZE
import tkinter as tk
import tkinter.font
import boto3
from sale import sale_key_input,sale_key
from config import REGION,BUCKET_NAME
import sale
import requests
import json
from tkinter import messagebox
from picamera import PiCamera



window=tk.Tk()
window.title("MATCHAT")
window.geometry('800x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')


camera=PiCamera()

def capture():
    camera.start_preview()
    camera.capture('/home/pi/save_folder/product.jpg')
    camera.stop_preview() 
    try:
        s3 = boto3.client('s3')
        
        #인증번호 저장
        key=sale.sale_key
        print(key)

        #이미지 이름 저장
        image_name='raspberrypi/'+key+".jpg"
        print(image_name)

        #s3 이미지 업로드 및 url 저장
        s3.upload_file("/home/pi/save_folder/product.jpg", "matchat", 'raspberrypi/'+key+".jpg")
        print('success')   
        url="https://s3-%s.amazonaws.com/%s/%s" %(REGION,BUCKET_NAME,image_name)
        print(url)
        kiosk_photo=url

        #detection결과 저장
        detection_url="http://ec2-15-164-129-198.ap-northeast-2.compute.amazonaws.com:5000/predict"
        image_path="/home/pi/save_folder/product.jpg"
        image_data = open(image_path, "rb").read()
        response = requests.post(detection_url, files={"image": image_data}).json()
        print(response[0]['name'])
        kiosk_result=response[0]['name']
        
        #동일상품확인 api 요청
        r = requests.post("http://ec2-3-39-141-76.ap-northeast-2.compute.amazonaws.com/api_same_check/result/",
                  json={'key': key, 'kiosk_result': kiosk_result, 'kiosk_photo': kiosk_photo})

        text = r.text
        data = json.loads(text)
        print(data)
        result = data['status']
        print(result)
        
        
        #result=0:다른상품, result=1:같은상품
        if result==str(0):
            messagebox.showwarning('warning','사전 등록 상품과 다른 상품입니다.물건을 다시 투입해주세요.')
        else:
            window.destroy()
            import sale_success



    except Exception as err:
        print("input error", err)




font=tkinter.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font2=tkinter.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)



label1=tk.Label(window, text="   MATCHAT[판매자]", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label1.pack()

label2=tk.Label(window,text='상품배치가 완료되면',font=font2,bg="#1abc9c")
label2.place(x=275,y=150)

label3=tk.Label(window,text='사진찍기 버튼을 눌러주세요.',font=font2,bg="#1abc9c")
label3.place(x=230,y=195)

bt1=tk.Button(window,text="사진찍기",font=font, width=15,height=3)
bt1.place(x=320,y=290)


window.mainloop()
