import customtkinter
from math import *
import random

app = customtkinter.CTk()
app.title("Porn hub")
app.geometry("500x500")

#ข้อความแสดงผล
label = customtkinter.CTkLabel(app, text="คุณลองพิมพ์ชื่อของคุณดูสิ" , fg_color="transparent" , font=('Aria' , 50))
label.pack(pady=(30, 0))

#กล่องรับค่า inputs
entry = customtkinter.CTkEntry(app, placeholder_text="คุณสามารถพิมพ์ได้ตรงนี้" )
entry.pack(pady=(50, 0))

#ข้อความแสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_laber = customtkinter.CTkLabel(app , textvariable=answer_text,font=("Arai" , 20) )
answer_laber.pack(pady=(20,0))

#ปุ่มกด  
def button_event():
    List_Trashtalk = ["น่ารักจัดชอบอะ", "เหี้ยนี่โง่ควายโง่ปัญญาอ่อน"]
    persent = {
        "1":0.25,
        "2":0.75
    }
    answer_Word = random.choices(List_Trashtalk, weights = persent.values(),k=1)[0]
    answer_text.set(answer_Word)

    print(answer_Word)
button = customtkinter.CTkButton(app , text="Clik me", command=button_event)
button.pack(pady=(15, 0))

app.mainloop()

