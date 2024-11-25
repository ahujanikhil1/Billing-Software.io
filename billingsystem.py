from tkinter import *
from tkinter import ttk #stylish krne k lie
from PIL import Image,ImageTk  #pillow se
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import win32api
import win32print
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="nikhil",auth_plugin="mysql_native_password")



class Bill_App:
    def __init__(self,nik):
        self.nik=nik
        self.nik.geometry("1550x800+0+0")
        self.nik.title("BILLING SOFTWARE")

        #variables
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        a=random.randint(1000,9999)
        self.bill_no.set(a)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.bill_data=StringVar()
        self.cat=StringVar()
        self.s_cat=StringVar()
        


        #product categories list
        self.category=["Select Option","Clothing","Lifestyle","Mobiles"]
        #clothing
        self.subcatClothing=['Pant','T-Shirt','Shirt','Kurta Pyjama','Blazzers','Jeans']
        self.pant=['Levis','Mufti','RareRabbit','RedTape','Spykar']
        self.price_levis=2000
        self.price_mufti=1250
        self.price_rarerabbit=2100
        self.price_Redtape=1000
        self.price_spykar=1500

        self.tshirt=['TOMMY HILFIGER','POLO','HRX','LEVIS']
        self.price_tommy=2000
        self.price_polo1=1500
        self.price_hrx1=1000
        self.price_Levis1=2000

        self.shirt=['Cantabil','POLO','HRX','LEVIS']
        self.price_cantabil1=3000
        self.price_polo2=2000
        self.price_hrx2=1900
        self.price_Levis2=2500

        self.kurtapyjama=['Redtape','montee','RayBan']
        self.price_redtape1=4500
        self.price_montee=4000
        self.price_rayban=5000

        self.blazzers=['Cantabil','Ray Ban']
        self.price_cantabil=15000
        self.price_Rayban=20000

        self.jeans=['LV','Mufti']
        self.price_lv=5500
        self.price_mufti1=1200


        #lifestyle
        
        self.subcatLifestyle=['Soap','Oil','Cream']
        self.Bath_soap=['Life Boy','LUX','Dettol','Pears']
        self.price_life=20
        self.price_lux=30
        self.price_dettol=40
        self.price_pears=25

        self.cream=['Fair $ Lovely','Boroplus','Mamas Earth','Beardo']
        self.price_fandl=30
        self.price_boroplus=40
        self.price_mama=90
        self.price_beardo=125

        self.oil=['Bajaj','Dabur Amla','Parachute']
        self.price_bajaj=55
        self.price_amla=90
        self.price_para=65
        
        
        #mobiles
        self.subcatMobiles=['Iphone','Samsung','One+']
        self.iphone=['iphone13','iphone14','iphone13 pro','iphone 15','iphone16']
        self.price_13=39000
        self.price_14=50000
        self.price_13pro=93000
        self.price_15=60000
        self.price_16=70000

        self.samsung=['a23','A50','S20','S20 ultra']
        self.price_23=19000
        self.price_50=23000
        self.price_29=65000
        self.price_20=90000

        self.oneplus=['12 R','Nord ce3','CE4','8T']
        self.price_12=37998
        self.price_ce3=17999
        self.price_ce4=21999
        self.price_8t=25469
        

        
        
        
        
        
        



    
        
#image1
        img=Image.open("C:/Users/abc/Desktop/billingsoftware/images/1.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS) #high level img ko low level
        self.photoimg=ImageTk.PhotoImage(img)
        l_image=Label(self.nik,image=self.photoimg)
        l_image.place(x=0,y=0,width=500,height=130)
#image2
        img1=Image.open("C:/Users/abc/Desktop/billingsoftware/images/2.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS) #high level img ko low level
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        l_image1=Label(self.nik,image=self.photoimg1)
        l_image1.place(x=500,y=0,width=500,height=130)
#image3
        img2=Image.open("C:/Users/abc/Desktop/billingsoftware/images/3.jpg")
        img2=img2.resize((530,130),Image.Resampling.LANCZOS) #high level img ko low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        l_image2=Label(self.nik,image=self.photoimg2)
        l_image2.place(x=1000,y=0,width=530,height=130)

        #label title
        lbltitle=Label(self.nik,text="BILLING SOFTWARE",font=("times new romman",35,"bold"),bg='white',fg='black')
        lbltitle.place(x=0,y=130,width=1530,height=40)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(lbltitle,font=("times new romman",18,"bold"),bg='white',fg='black')
        lbl.place(x=0,y=2,width=150,height=45)
        time()


        f1=Frame(self.nik,bd=5,relief=GROOVE,bg='white')
        f1.place(x=0,y=175,width=1530,height=620)


        #customer label frame
        cust_frame=LabelFrame(f1,text="CUSTOMER DETAIL",font=("times new romman",12,"bold"),bg='white',fg='black',bd=5,relief=GROOVE)
        cust_frame.place(x=10,y=5,width=350,height=140)

        lbl_mobile=Label(cust_frame,text="Mobile NO.",font=("arial",11,"bold"),bg='white')
        lbl_mobile.grid(row=0,column=0,stick=W,padx=5,pady=2)

        entry_mobile=ttk.Entry(cust_frame,textvariable=self.c_phone,font=("arial",11,"bold"),width=24)
        entry_mobile.grid(row=0,column=1)


        cust_name=Label(cust_frame,text="NAME",font=("arial",11,"bold"),bg='white',bd=4)
        cust_name.grid(row=1,column=0,stick=W,padx=5,pady=2)
        entry_name=ttk.Entry(cust_frame,textvariable=self.c_name,font=("arial",11,"bold"),width=24)
        entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        cust_mail=Label(cust_frame,text="E-MAIL:",font=("arial",11,"bold"),bg='white',bd=4)
        cust_mail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        entry_mail=ttk.Entry(cust_frame,textvariable=self.c_email,font=("arial",11,"bold"),width=24)
        entry_mail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


#product frame

        prod_frame=LabelFrame(f1,text="PRODUCT DETAIL",font=("times new romman",12,"bold"),bg='white',fg='black',bd=5,relief=GROOVE)
        prod_frame.place(x=370,y=5,width=650,height=140)

        categories=Label(prod_frame,text="Select categories:",font=("arial",11,"bold"),bg='white',bd=4)
        categories.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_categories=ttk.Combobox(prod_frame,value=self.category,font=("arial",10,"bold"),width=24,state='readonly')
        self.Combo_categories.current(0)
        self.Combo_categories.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_categories.bind("<<ComboboxSelected>>",self.categories)

        
        subcategories=Label(prod_frame,text="Subcategories:",font=("arial",11,"bold"),bg='white',bd=4)
        subcategories.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.Combo_subcategories=ttk.Combobox(prod_frame,value=[''],font=("arial",10,"bold"),width=24,state='readonly')
        self.Combo_subcategories.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_subcategories.bind("<<ComboboxSelected>>",self.productadd)
        

        p_name=Label(prod_frame,text="Product Name",font=("arial",11,"bold"),bg='white',bd=4)
        p_name.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.Combo_p_name=ttk.Combobox(prod_frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state='readonly')
        self.Combo_p_name.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combo_p_name.bind("<<ComboboxSelected>>",self.price)
        

        price=Label(prod_frame,text="Price",font=("arial",11,"bold"),bg='white',bd=4)
        price.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.Combo_price=ttk.Combobox(prod_frame,font=("arial",10,"bold"),textvariable=self.prices,width=24,state='readonly')
        self.Combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        qty=Label(prod_frame,text="Quantity",font=("arial",11,"bold"),bg='white',bd=4)
        qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.entry_qty=ttk.Entry(prod_frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.entry_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        #searching

        search_frame=Frame(f1,bd=2,bg='white')
        search_frame.place(x=1030,y=15,width=480,height=40)

        self.lblbill=Label(search_frame,font=('arial',12,'bold'),fg='black',bg='white',text='Bill Number')
        self.lblbill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_entry_search=ttk.Entry(search_frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=20)
        self.txt_entry_search.grid(row=0,column=1,sticky=W,padx=2)


        self.btn7=Button(search_frame,command=self.searchh,text='SEARCH',font=("arial",10,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn7.grid(row=0,column=2)

        


        #rightframe bill area

        rightlblframe=LabelFrame(f1,text="BILL AREA",font=("times new romman",12,"bold"),bg='white',fg='black',bd=5,relief=GROOVE)
        rightlblframe.place(x=1030,y=45,width=480,height=440)

        scroll_y=Scrollbar(rightlblframe,orient=VERTICAL)
        self.textarea=Text(rightlblframe,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=("times new romman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
#billing label frame

        bill_frame=LabelFrame(f1,text="BILLING DETAIL",font=("times new romman",12,"bold"),bg='white',fg='black',bd=5,relief=GROOVE)
        bill_frame.place(x=0,y=485,width=1520,height=125)

        subtotal=Label(bill_frame,text="SubTotal:",font=("arial",11,"bold"),bg='white',bd=4)
        subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_subtotal=ttk.Entry(bill_frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=26)
        self.entry_subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        tax=Label(bill_frame,text="TAX:",font=("arial",11,"bold"),bg='white',bd=4)
        tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_tax=ttk.Entry(bill_frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=26)
        self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        total=Label(bill_frame,text="TOTAL:",font=("arial",11,"bold"),bg='white',bd=4)
        total.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.entry_total=ttk.Entry(bill_frame,textvariable=self.total,font=("arial",10,"bold"),width=26)
        self.entry_total.grid(row=3,column=1,sticky=W,padx=5,pady=2)



        #buttonframe
        button_frame=Frame(bill_frame,bd=3,bg='white')
        button_frame.place(x=320,y=0)

        self.btnaddtocart=Button(button_frame,height=2,text='ADD TO CART',command=self.Additem,font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btnaddtocart.grid(row=0,column=0)

        self.btn2=Button(button_frame,height=2,command=self.g_bill,text='GENERATE BILL',font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn2.grid(row=0,column=1)

        self.btn3=Button(button_frame,height=2,command=self.s_bill,text='SAVE BILL',font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn3.grid(row=0,column=2)

        self.btn4=Button(button_frame,height=2,command=self.printer,text='PRINT',font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn4.grid(row=0,column=3)

        self.btn5=Button(button_frame,height=2,command=self.cleear,text='CLEAR',font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn5.grid(row=0,column=4)

        self.btn6=Button(button_frame,height=2,command=self.nik.destroy,text='EXIT',font=("arial",15,"bold"),bg='red',fg='white',width=15,cursor="hand2")
        self.btn6.grid(row=0,column=5)

        

        self.welcome()

        self.l=[]

        #middle frame

        midle_frame=Frame(f1,bd=10,relief=GROOVE)
        midle_frame.place(x=10,y=150,width=1000,height=310)


        img4=Image.open("C:/Users/abc/Desktop/billingsoftware/images/3.jpg")
        img4=img4.resize((490,340),Image.Resampling.LANCZOS) #high level img ko low level
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        l_image4=Label(midle_frame,image=self.photoimg4)
        l_image4.place(x=0,y=0,width=490,height=310)

        
        img5=Image.open("C:/Users/abc/Desktop/billingsoftware/images/3.jpg")
        img5=img5.resize((490,340),Image.Resampling.LANCZOS) #high level img ko low level
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        l_image5=Label(midle_frame,image=self.photoimg5)
        l_image5.place(x=490,y=0,width=500,height=340)


    #function

    def Additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("ERROR","PLEASE SELECT THE PRODUCT NAME")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def g_bill(self):
        if self.product.get()=="":
            messagebox.showerror("ERROR","PLEASE ADD TO CART PRODUCT")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=================================================\n")
            self.textarea.insert(END,f"\n SUB AMOUNT:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n TAX AMAOUNT:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n TOTAL AMOUNT:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=================================================")

    def s_bill(self):
        
        '''op=messagebox.askyesno("SAVE BILL","DO YOU WANT TO SAVE THE BILL")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            g1=open('C:/Users/abc/Desktop/billingsoftware/slip/'+str(self.bill_no.get())+".txt",'w')
            g1.write(self.bill_data)
            d=messagebox.showinfo("SAVED",f"BILL NO.{self.bill_no.get()}SAVED SUCCESSFULLY")
            g1.close()'''
            
        con=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="nikhil",auth_plugin="mysql_native_password")
        if(con.is_connected):
                                cursor=con.cursor()
                                name=self.c_name.get()
                                mobile_no=self.c_phone.get()
                                e_mail=self.c_email.get()
                                category=self.cat.get()
                                sub_cat=self.s_cat.get()
                                product=self.product.get()
                                price=self.prices.get()
                                quantity=self.qty.get()
                                bill_no=self.bill_no.get()
                                sub_t=self.sub_total.get()
                                taxx=self.tax_input.get()
                                totall=self.total.get()
                                sql=f"INSERT INTO retail VALUES('{name}','{mobile_no}','{e_mail}','{product}',{price},{quantity},{bill_no},'{sub_t}','{taxx}','{totall}')"
                                cursor.execute(sql)
                                con.commit()
                                print("one record is inserted")
                                    
        

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t WELCOME IN MINI SHOP")
        self.textarea.insert(END,f"\n BILL NUMBER:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME:{self.c_name.get()}")
        self.textarea.insert(END,f"\n PHONE NUMBER:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n E-mail:{self.c_email.get()}")

        self.textarea.insert(END,"\n=================================================\n")
        self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\tPRICE")
        self.textarea.insert(END,"\n=================================================")

    def printer(self):
        
        k=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(k)
        os.startfile(filename,"print")
    '''def printer(self):
        
        try:
        
            k = self.textarea.get(1.0, "end-1c")
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
                
                tmp_file.write(k.encode('utf-8'))  # Write the text to the file
                tmp_file_name = tmp_file.name

        # Open the print dialog and send the file to the chosen printer
            win32api.ShellExecute(0,    "printto",  # Command to open the print dialog
            tmp_file_name,
            '"%s"' % win32print.GetDefaultPrinter(),  # Set to the default printer
            ".",
            0
        )

        except Exception as e:
            
            print(f"An error occurred while trying to print: {e}")'''

    def searchh(self):
        found="no"
        for i in os.listdir('C:/Users/abc/Desktop/billingsoftware/slip/'):
            if i.split('.')[0]==self.search_bill.get():
                g1=open(f'C:/Users/abc/Desktop/billingsoftware/slip/{i}','r')
                self.textarea.delete(1.0,END)
                for d in g1:
                    self.textarea.insert(END,d)
                g1.close()
                found='yes'
        if found=='no':
            messagebox.showerror("Error","INVALID BILL NUMBER")

    def cleear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set('')
        self.c_phone.set('')
        self.c_email.set('')
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.product.set('')
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set('')
        self.sub_total.set('')
        self.tax_input.set('')
        self.welcome()

        

    
        




    def categories(self,e=' '):
        if self.Combo_categories.get()=="Clothing":
            self.Combo_subcategories.config(value=self.subcatClothing)
            self.Combo_subcategories.current(0)
            
        if self.Combo_categories.get()=="Lifestyle":
            self.Combo_subcategories.config(value=self.subcatLifestyle)
            self.Combo_subcategories.current(0)
            
        if self.Combo_categories.get()=="Mobiles":
            self.Combo_subcategories.config(value=self.subcatMobiles)
            self.Combo_subcategories.current(0)

    def productadd(self,v=""):
        if self.Combo_subcategories.get()=="Pant":
            self.Combo_p_name.config(value=self.pant)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="T-Shirt":
            self.Combo_p_name.config(value=self.tshirt)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="Shirt":
            self.Combo_p_name.config(value=self.shirt)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="Kurta Pyjama":
            self.Combo_p_name.config(value=self.kurtapyjama)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="Blazzers":
            self.Combo_p_name.config(value=self.blazzers)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="Jeans":
            self.Combo_p_name.config(value=self.jeans)
            self.Combo_p_name.current(0)

        #lifestyle

        if self.Combo_subcategories.get()=="Soap":
            self.Combo_p_name.config(value=self.Bath_soap)
            self.Combo_p_name.current(0)
            
        if self.Combo_subcategories.get()=="Oil":
            self.Combo_p_name.config(value=self.oil)
            self.Combo_p_name.current(0)
            
        if self.Combo_subcategories.get()=="Cream":
            self.Combo_p_name.config(value=self.cream)
            self.Combo_p_name.current(0)

        # mobiles
            
        if self.Combo_subcategories.get()=="One+":
            self.Combo_p_name.config(value=self.oneplus)
            self.Combo_p_name.current(0)
            
        if self.Combo_subcategories.get()=="Iphone":
            self.Combo_p_name.config(value=self.iphone)
            self.Combo_p_name.current(0)

        if self.Combo_subcategories.get()=="Samsung":
            self.Combo_p_name.config(value=self.samsung)
            self.Combo_p_name.current(0)



    def price(self,e=''):
        #pant 
        if self.Combo_p_name.get()=="Levis":
            self.Combo_price.config(value=self.price_levis)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="Mufti":
            self.Combo_price.config(value=self.price_mufti)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="RareRabbit":
            self.Combo_price.config(value=self.price_rarerabbit)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="RedTape":
            self.Combo_price.config(value=self.price_Redtape)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="Spykar":
            self.Combo_price.config(value=self.price_spykar)
            self.Combo_price.current(0)
            self.qty.set(1)
        #tshirt
        if self.Combo_p_name.get()=="TOMMY HILFIGER":
            self.Combo_price.config(value=self.price_tommy)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="POLO":
            self.Combo_price.config(value=self.price_polo1)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="HRX":
            self.Combo_price.config(value=self.price_hrx1)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="LEVIS":
            self.Combo_price.config(value=self.price_Levis1)
            self.Combo_price.current(0)
            self.qty.set(1)

        # shirt
        if self.Combo_p_name.get()=="Cantabil":
            self.Combo_price.config(value=self.price_cantabil1)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="POLO":
            self.Combo_price.config(value=self.price_polo2)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="HRX":
            self.Combo_price.config(value=self.price_hrx2)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="LEVIS":
            self.Combo_price.config(value=self.price_Levis2)
            self.Combo_price.current(0)
            self.qty.set(1)

        
        #kurta

        if self.Combo_p_name.get()=="Redtape":
            self.Combo_price.config(value=self.price_redtape1)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="montee":
            self.Combo_price.config(value=self.price_montee)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="RayBan":
            self.Combo_price.config(value=self.price_rayban)
            self.Combo_price.current(0)
            self.qty.set(1)

        #blazzers

        if self.Combo_p_name.get()=="Cantabil":
            self.Combo_price.config(value=self.price_cantabil)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="Rat Ban":
            self.Combo_price.config(value=self.price_Rayban)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="LV":
            self.Combo_price.config(value=self.price_lv)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="Mufti":
            self.Combo_price.config(value=self.price_mufti1)
            self.Combo_price.current(0)
            self.qty.set(1)
        #lifestyle
        #soap
        if self.Combo_p_name.get()=="Life Boy":
            self.Combo_price.config(value=self.price_life)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="LUX":
            self.Combo_price.config(value=self.price_lux)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Dettol":
            self.Combo_price.config(value=self.price_dettol)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Pears":
            self.Combo_price.config(value=self.price_pears)
            self.Combo_price.current(0)
            self.qty.set(1)

    # cream

        if self.Combo_p_name.get()=="Fair $ Lovely":
            self.Combo_price.config(value=self.price_fandl)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Boroplus":
            self.Combo_price.config(value=self.price_boroplus)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Mamas Earth":
            self.Combo_price.config(value=self.price_mama)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Beardo":
            self.Combo_price.config(value=self.price_beardo)
            self.Combo_price.current(0)
            self.qty.set(1)
            
        #oil
        if self.Combo_p_name.get()=="Bajaj":
            self.Combo_price.config(value=self.price_bajaj)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Dabur Amla":
            self.Combo_price.config(value=self.price_amla)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="Parachute":
            self.Combo_price.config(value=self.price_para)
            self.Combo_price.current(0)
            self.qty.set(1)
        #mobiles

        if self.Combo_p_name.get()=="iphone13":
            self.Combo_price.config(value=self.price_13)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="iphone14":
            self.Combo_price.config(value=self.price_14)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="iphone13 pro":
            self.Combo_price.config(value=self.price_13pro)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="iphone15":
            self.Combo_price.config(value=self.price_15)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="iphone16":
            self.Combo_price.config(value=self.price_16)
            self.Combo_price.current(0)
            self.qty.set(1)

       

        if self.Combo_p_name.get()=="a23":
            self.Combo_price.config(value=self.price_23)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="A50":
            self.Combo_price.config(value=self.price_50)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="S20":
            self.Combo_price.config(value=self.price_29)
            self.Combo_price.current(0)
            self.qty.set(1)
        if self.Combo_p_name.get()=="S20 ultra":
            self.Combo_price.config(value=self.price_20)
            self.Combo_price.current(0)
            self.qty.set(1)
            

        if self.Combo_p_name.get()=="12 R":
            self.Combo_price.config(value=self.price_12)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="Nord ce3":
            self.Combo_price.config(value=self.price_ce3)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="CE4":
            self.Combo_price.config(value=self.price_ce4)
            self.Combo_price.current(0)
            self.qty.set(1)

        if self.Combo_p_name.get()=="8T":
            self.Combo_price.config(value=self.price_8t)
            self.Combo_price.current(0)
            self.qty.set(1)



   
    '''def insert(self):
                con=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="nikhil",auth_plugin="mysql_native_password")
                if(con.is_connected):
                    
                    cursor=con.cursor()
                    name=self.c_name.get()
                    mobile_no=self.c_phone.get()
                    e_mail=self.c_email.get()
                    category=self.cat.get()
                    sub_cat=self.s_cat.get()
                    product=self.product.get()
                    price=self.prices.get()
                    quantity=self.qty.get()
                    bill_no=self.bill_no.get()
                    sub_t=self.sub_total.get()
                    taxx=self.tax_input.get()
                    totall=self.total.get()
                    sql=f"INSERT INTO retail VALUES('{name}',{mobile_no},'{e_mail}','{product}',{price},{quantity},{bill_no},'{sub_t}','{taxx}','{totall}')"
                    cursor.execute(sql)
                    con.commit()
                    print("one record is inserted")'''
                                    
                        
                        
                        

                 
                    
                    
                





        
        
             

             
             
             
             

        
            
            


        


            
            
        


        
        
        



        
                



if __name__=='__main__':
    nik=Tk()
    objeect=Bill_App(nik)
    nik.mainloop()
    
