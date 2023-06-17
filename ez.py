import customtkinter
from math import *
app = customtkinter.CTk()
app.title("Porn hub")
app.geometry("500x500")

#ข้อความแสดงผล
label = customtkinter.CTkLabel(app, text="Calculator" , fg_color="transparent" , font=('Blackoak Std' , 30))
label.pack(pady=(30, 0))

#กล่องรับค่า inputs
entry = customtkinter.CTkEntry(app, placeholder_text="คุณสามารถพิมพ์ได้ตรงนี้" )
entry.pack(pady=(50, 0))

#ข้อความแสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_laber = customtkinter.CTkLabel(app , textvariable=answer_text,font=("Blackoak Std" , 20) )
answer_laber.pack(pady=(20,0))

#ปุ่มกด  
def button_event():
    inputs = entry.get()
    answer = eval(inputs)
    answer_text.set(answer)
    print(answer)
button = customtkinter.CTkButton(app , text="Clik me", command=button_event)
button.pack(pady=(15, 0))

app.mainloop()