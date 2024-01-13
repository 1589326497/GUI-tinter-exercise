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
        self.label01 = Label(self, text="你好世界", width=10, height=2, bg="black", fg="white")
        self.label01.pack()
        
        self.label02 = Label(self, text="hallow", width=10, height=2, bg="black", fg="white", font=("黑体", 30))
        self.label02.pack()
        # 显示图像
        # global photo         #全局变量
        # photo = PhotoImage(file="image/")
        # self.label03=Label(self,image=photo)
        # self.label03.pack()
        #显示多行的文本
        self.label04=Label(self,text="你好\n世界",borderwidth=4,relief="groove",justify="right")
        self.label04.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+300")
    root.title("GUI程序实例")
    app = APPlication(master=root)
    root.mainloop()
