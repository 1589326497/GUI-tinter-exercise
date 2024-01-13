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
        '''通过place布局器实现扑克的位置控制'''
        # self.photo=PhotoImage(file="")
        # self.puke1=Label(self,image=self.photo)
        # self.puke1.place(x=10,y=10)
        self.photos=[PhotoImage(file=""+str(i+1)+".gif")for i in range(10)]
        self.pukes=[Label(self.master,image=self.photos[i]) for i in range(10)]

        for i in range(10):
            self.pukes[i].place(x=10+1*40,y=50)
        #为所有的Lable创建事件对象

    def chupai(self,event):
        print()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+300")
    root.title("GUI程序实例")
    app = APPlication(master=root)
    root.mainloop()