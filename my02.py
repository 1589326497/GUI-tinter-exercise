'''
测试GUI 面向对象的方法
'''
from tkinter import *
from tkinter import messagebox


class APPlication(Frame):
    '''一个经典的GUI实例'''

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义，而不是代表父类的对象
        self.master = master
        self.pack()  # 布局管理器

        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.btn01 = Button(self)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建一个退出按钮

        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花")

if __name__=='__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("GUI程序实例")
    app = APPlication(master=root)
    root.mainloop()
