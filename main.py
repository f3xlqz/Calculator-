import customtkinter

app = customtkinter.CTk()
app.title('playlist')
app.geometry('500x750')

# เเสดงข้อความ
label = customtkinter.CTkLabel(app, text="Calculator", fg_color="transparent", font=('Aria' , 40))
label.pack(pady=(20, 0))
label = customtkinter.CTkLabel(app, text="คณิตศาสตร์ง่ายง่าย", fg_color="transparent", font=('Aria' , 30))
label.pack(pady=(10, 0))
label = customtkinter.CTkLabel(app, text="หาพื้นที่วงกลม", fg_color="transparent", font=('Aria' , 20))
label.pack(pady=(10, 0))

# เเสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 40))
answer_label.pack(pady=(20, 0))

# กล่องรับค่า Inputs
entry2 = customtkinter.CTkEntry(app, placeholder_text="ค้นหาคำตอบ...   ")
entry2.pack(pady=(10, 0))

# ปุ่มกด
import math
def button_event():
    user_input = entry2.get()
    radius = float(user_input)
    area = math.pi * (radius*2)
    answer_text.set(area)
    print("Radius", area)
    print("Area", area)
button = customtkinter.CTkButton(app, text="ค้นหาคำตอบ", command=button_event)
button.pack(pady=(10, 0))

#---------------------------------------------------------------------------------------
label = customtkinter.CTkLabel(app, text="หาเส้นรอบวงของวงกลม", fg_color="transparent", font=('Aria' , 20))
label.pack(pady=(30, 0))

# แสดงคำตอบ เส้นรอบวง
circle_text = customtkinter.StringVar()
circle_label = customtkinter.CTkLabel(app, textvariable=circle_text, font=('Aria', 40))
circle_label.pack(pady=(20, 0))

# กล่องรับค่า Inputs
entry = customtkinter.CTkEntry(app, placeholder_text="ค้นหาคำตอบ...   ")
entry.pack(pady=(10, 0))

# ปุ่มกด
import math
def button_event():
    user_input = entry.get()
    radius = float(user_input)
    circumference = 2 * math.pi * (radius)
    circle_text.set(circumference)
    print("Radius", circumference)
    print("Area", circumference)
button = customtkinter.CTkButton(app, text="ค้นหาคำตอบ", command=button_event)
button.pack(pady=(10, 0))

app.mainloop()