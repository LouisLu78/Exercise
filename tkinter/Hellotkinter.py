from tkinter import *

# The codes below are all copied from textbook.
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

'''This is example 2
class App:
    def __init__(self, master):
        self.master=master
        self.initWidgets()

    def initWidgets(self):
        fm1=Frame(self.master)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        Button(fm1, text='A1').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='A2').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='A3').pack(side=TOP, fill=X, expand=YES)

        fm2=Frame(self.master)
        fm2.pack(side=LEFT, padx=10, expand=YES)
        Button(fm2, text='B1').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='B2').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='B3').pack(side=RIGHT, fill=Y, expand=YES)

        fm3 = Frame(self.master)
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        Button(fm3, text='C1').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='C2').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='C3').pack(side=BOTTOM, fill=Y, expand=YES)

root=Tk()
root.title('Pack configuration')
display=App(root)
root.mainloop()
'''

'''This is example 3
class App():
    def __init__(self, master):
        self.master=master
        self.initWidgets()

    def initWidgets(self):
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
        e.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "=")
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i//4, column=i%4)

root=Tk()
root.title('Calculator')
display=App(root)
root.mainloop()
'''
import random
'''
class App():
    def __init__(self, master):
        self.master=master
        self.initwidgets()

    def initwidgets(self):
        books = ('Phsical Chemistry', 'Organic Chemistry', 'Analytical Chemistry', \
                 'Inorganic Chmemistry', 'Polymer Chemistry')
        for i in range(len(books)):
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            bg_color = "#%02x%02x%02x" % tuple(ct)

            lb=Label(root, text=books[i],fg = 'White' if grayness < 120 else 'Black', bg = bg_color)
            lb.place(x=20, y=36 + i * 36, width=180, height=30)
root=Tk()
root.title('Place Configuration')
root.geometry("250x250+30+30")
display=App(root)
root.mainloop()
'''

class App():
    def __init__(self, master):
        self.master=master
        self.initwidgets()

    def initwidgets(self):
        self.label = Label(self.master, width=30, font=('Courier',20), bg='white')
        self.label.pack()

        okButton = Button(self.master, text="click me", command=self.change)
        okButton.pack()

    def change(self):
        self.label['text']='Welcome to world of Python'
        ct = [random.randrange(256) for x in range(3)]
        grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
        bg_color = "#%02x%02x%02x" % tuple(ct)
        self.label['bg']=bg_color
        self.label['fg']='White' if grayness < 120 else 'Black'

root=Tk()
root.title('Simple case reaction')
display=App(root)
root.mainloop()
