from tkinter import *

# root=Tk()
# root.title('GL\'s first GUI')
# w=Label(root, text='Hello tkinter')
# w.pack()
# root.mainloop()


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
