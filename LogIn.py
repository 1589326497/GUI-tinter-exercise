from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x180")
root.title('登录')

username = StringVar()
password = StringVar()
def login():
    name = username.get()
    pwd = password.get()
    print("用户：", name)
    print("密码：", pwd)
    if name=="宁子希"and pwd=="666666":
        print("登录成功")
    else:
        messagebox.showwarning(title='警告',message='登录失败，请检查账号密码')


# 登录界面绘制
page = Frame(root)
page.pack()

Label(page).grid(row=0, column=0)
Label(page, text='账户：').grid(row=1, column=1)
Entry(page, textvariable=username).grid(row=1, column=2)
Label(page, text='密码：').grid(row=2, column=1, pady=10)
Entry(page, textvariable=password).grid(row=2, column=2)
Button(page, text='登录',command=login).grid(row=3, column=2, pady=10)
root.mainloop()










