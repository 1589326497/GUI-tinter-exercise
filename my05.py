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
        '''计数器的界面'''
        btnText=(("MC","M+","M-","MR"),
                 ("C","±","÷","×"),
                 (4,8,9,"-"),
                 (4,5,6,"+"),
                 (1,2,3,"="),
                 (0,"."))
        Entry(self).grid(row=0,column=0,columnspan=4,pady=10)
        for rindex,r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c=="=":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex,rowspan=2, sticky=EW)
                elif c==0:
                    pass
                elif c==".":
                    pass
                else:
                    Button(self,text=c,width=2).grid(row=rindex+1,column=cindex,sticky=EW)

if __name__=='__main__':
    root = Tk()
    root.geometry("200x240+200+300")
    root.title("GUI程序实例")
    app = APPlication(master=root)
    root.mainloop()