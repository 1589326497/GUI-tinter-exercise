from tkinter import *
from tkinter import messagebox
'''创建登录界面  Entry'''

class APPlication(Frame):
    '''一个经典的GUI实例'''

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义，而不是代表父类的对象
        self.master = master
        self.pack()  # 布局管理器

        self.createWidget()

    def createWidget(self):
        '''创建登录界面'''
        self.labe01=Label(self,text="用户名")
        self.labe01.pack()
        #StringVar变量绑定带指定的组件 StringVar变量发生变化，组件内容发生变化
        v1=StringVar()
        self.entry01=Entry(self,textvariable=v1)
        self.entry01.pack()

        #创建密码
        self.labe02 = Label(self, text="密码")
        self.labe02.pack()
        # StringVar变量绑定带指定的组件 StringVar变量发生变化，组件内容发生变化
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show='*') #show属性，当你显示内容的时候显示的都是*
        self.entry02.pack()

        self.btn01=Button(self,text="登录",command=self.login)
        self.btn01.pack()
    def login(self):
        username=self.entry01.get()
        pwd=self.entry02.get()

        print("与数据库比对")
        print("用户名"+username)
        print("密码"+pwd)
        if username=="宁子希"and pwd=="2034140515":
            messagebox.showinfo("", "登录成功")
            print("信息正确")
        else:
            messagebox.showinfo("", "登录失败")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+300")
    root.title("GUI程序实例")
    app = APPlication(master=root)
    root.mainloop()