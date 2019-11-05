from tkinter import *


'''this is example 1:

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initWidgets()

    def initWidgets(self):
        w=Label(self)
        bm = PhotoImage(file='yuna.PNG')
        w.x=bm
        w['image']=bm
        w.pack()
        okButton = Button(self, text="confirm",background='red')
        # okButton['background'] = 'red'
        # okButton.configure(background='red')
        okButton.pack()
app=Application()
print(type(app.master))
app.master.title('GL\'s first GUI')
app.mainloop()
'''
# root=Tk()
# root.title('Pack configuration')
# for i in range(3):
#     w=Label(root, text='The No.{} Label'.format(i+1), bg='#eeeeee')
#     w.pack()
# root.mainloop()
class App:
    def __init__(self, master):
        self.master=master
        self.initWidgets()

    def initWidgets(self):
        fm1=Frame(self.master)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        Button(fm1, text='No.1').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='No.2').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='No.3').pack(side=TOP, fill=X, expand=YES)

        fm2=Frame(self.master)
        fm2.pack(side=LEFT, padx=10, expand=YES)
        Button(fm2, text='No.1').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='No.2').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='No.3').pack(side=RIGHT, fill=Y, expand=YES)

        fm3 = Frame(self.master)
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        Button(fm3, text='No.1').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='No.2').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='No.3').pack(side=BOTTOM, fill=Y, expand=YES)

root=Tk()
root.title('Pack configuration')
display=App(root)
root.mainloop()





