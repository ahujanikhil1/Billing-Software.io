from tkinter import *
from tkinter import messagebox
from billingsystem import Bill_App


root=Tk()
root.title("LOGIN PAGE")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        new_win = Toplevel(root)  
        Bill_App(new_win) 

    elif username!="admin" and password!="1234":
        messagebox.showerror("Error","Invalid Username or Password")

    elif password!="1234":
        messagebox.showerror("Error","Invalid Password")
    elif username!="admin":
        messagebox.showerror("Error","Invalid Username ")
    

img=PhotoImage(file="C:/Users/abc/Desktop/billingsoftware/images/logiin.png")
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='#fff')
frame.place(x=480,y=70)


heading=Label(frame,text='Sign in',fg='#57a1f8',bg='#fff',font=('Microsoft YaHei UI Light',23,'bold')).place(x=100,y=5)
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user=Entry(frame,width=25,fg='black',bd=0,bg='#fff',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',bd=0,bg='#fff',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',bd=0,command=signin).place(x=35,y=204)
lbl=Label(frame,text="Dont Have an account?",fg='black',bg='#fff',font=('Microsoft YaHei UI Light',9))
lbl.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',bg='#fff',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)




              
