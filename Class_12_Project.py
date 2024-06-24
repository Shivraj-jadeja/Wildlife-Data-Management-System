#Wildlife Sanctuary Data Management Project-------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as mb
from tkinter import ttk
import re
import mysql.connector as ms

#showdata------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def showtable():
        global s4
        s4=LabelFrame(top,text='Show Data',font=('Arial',15),relief=FLAT,width=580,height=650,bg='white')
        s4.place(x=600,y=20)

        label=Label(s4, text="Animal Details",font=('Arial',17,'bold'),fg="black",bg="magenta",padx=200,pady=10)
        label.grid(row=0,column=0,columnspan=20)


        pl=Label(s4, text='Sr No',font=('Arial',15,'bold'),bg="white",fg="blue")
        pl.grid(row=1,column=0,padx=10,pady=10)

        pl1=Label(s4, text='Animal Breed',font=('Arial',15,'bold'),bg="white",fg="blue")
        pl1.grid(row=1,column=1,padx=10,pady=10)

        pl2=Label(s4, text='Animal Code',font=('Arial',15,'bold'),bg="white",fg="blue")
        pl2.grid(row=1,column=2,padx=10,pady=10)

        pl3=Label(s4, text='Animal Habitat',font=('Arial',15,'bold'),bg="white",fg="blue")
        pl3.grid(row=1,column=3,padx=10,pady=10)

        mydb=ms.connect(host='localhost',user='root',password='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        sql1=("select * from animalinfo")
        cur.execute(sql1)
        b= cur.fetchall()

        num=2
        for i in b:
                srnost = Label(s4, text = i[0],font=('Arial',13,'bold'),fg = 'red',bg='white')
                srnost.grid(row = num,column= 0,padx=10,pady=10)

                breedst = Label(s4, text = i[1],font=('Arial',13,'bold'),fg = 'red',bg='white')
                breedst.grid(row = num,column= 1,padx=10,pady=10)

                codest = Label(s4, text = i[2],font=('Arial',13,'bold'),fg = 'red',bg='white')
                codest.grid(row = num,column= 2,padx=10,pady=10)

                habitatst = Label(s4, text = i[3],font=('Arial',13,'bold'),fg = 'red',bg='white')
                habitatst.grid(row = num,column= 3,padx=10,pady=10)
                
                num = num+1
        Button(s4,text='Back',font=('Arial',15),bg='magenta',command=lambda:[enable1(),s4.destroy()],relief='flat').place(x=470,y=5)        

def showind2():
        s5=LabelFrame(top,text='Show Data',font=('Arial',15),relief=FLAT,width=550,height=320,bg='white')
        s5.place(x=20,y=350)
        s3=LabelFrame(top,text='Show Data',font=('Arial',15),relief=FLAT,width=550,height=320,bg='white')
        s3.place(x=20,y=350)
        srnos2=srnos.get()

        label=Label(s3, text="Animal Details",font=('Arial',17,'bold'),fg="black",bg="magenta",padx=200,pady=10)
        label.grid(row=0,column=0,columnspan=20)


        p0=Label(s3, text='Sr No',font=('Arial',12,'bold'),bg="white",fg="blue")
        p0.grid(row=1,column=0,padx=10,pady=10)

        pl=Label(s3, text='Animal Breed',font=('Arial',12,'bold'),bg="white",fg="blue")
        pl.grid(row=1,column=1,padx=10,pady=10)

        p2=Label(s3, text='Animal Code',font=('Arial',12,'bold'),bg="white",fg="blue")
        p2.grid(row=1,column=2,padx=10,pady=10)

        p3=Label(s3, text='Animal Habitat',font=('Arial',12,'bold'),bg="white",fg="blue")
        p3.grid(row=1,column=3,padx=10,pady=10)

        mydb=ms.connect(host='localhost',user='root',password='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        cur.execute('select * from animalinfo where Sr_No=%s',(srnos2,))
        z= cur.fetchall()
        for i in z:
                srnosi = Label(s3, text = i[0],font=('Arial',11,'bold'),fg = 'red',bg='white')
                srnosi.grid(row = 2,column= 0,padx=10,pady=10)

                breedsi = Label(s3, text = i[1],font=('Arial',11,'bold'),fg = 'red',bg='white')
                breedsi.grid(row = 2,column= 1,padx=10,pady=10)

                codesi = Label(s3, text = i[2],font=('Arial',11,'bold'),fg = 'red',bg='white')
                codesi.grid(row = 2,column= 2,padx=10,pady=10)

                habitatsi = Label(s3, text = i[3],font=('Arial',11,'bold'),fg = 'red',bg='white')
                habitatsi.grid(row = 2,column= 3,padx=10,pady=10)
        Button(s3,text='Back',font=('Arial',17),bg='magenta',command=lambda:[s3.destroy(),s5.destroy()],relief='flat').place(x=410,y=5)
        
def showind1():
        srnos1=srnos.get()
        if srnos1=='':
                mb.showinfo('Error','Please Enter All Details',parent=s2)
        else:
                showind2()

def show_ind():
        global s2
        s2=LabelFrame(top,text='Show Data',font=('Arial',15),relief=FLAT,width=550,height=320,bg='white')
        s2.place(x=20,y=350)

        global srnos
        srnos=StringVar()
        
        Label(s2,text='Enter Sr No of Record You Want To See',font=("Arial",17),bg="orange").place(x=50,y=50)
        Entry(s2,textvariable=srnos ,font=("Arial",18),bg="grey").place(x=150,y=110)
        Button(s2,text="Show Data",font=('Arial',18),bg='Purple',command=showind1).place(x=100,y=180)
        Button(s2,text="Back ",font=("Arial",18),bg="lime",command=s2.destroy).place(x=350,y=180)

def enable1():
    b9.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    b11.configure(state=NORMAL)

def disable1():
        b9.configure(state=DISABLED)
        b10.configure(state=DISABLED)
        b11.configure(state=DISABLED)
        
def show_data():
        s1=LabelFrame(top,text='Show Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
        s1.place(x=20,y=350)
        global b9
        global b10
        global b11
        b9=Button(s1,text='Individual Data',font=('Arial',18),bg='Purple',command=show_ind)
        b9.place(x=150,y=50)
        b10=Button(s1,text='Group Data',font=('Arial',18),bg='Purple',command=lambda:[disable1(),showtable()])
        b10.place(x=170,y=130)
        b11=Button(s1,text='Back',font=('Arial',18),bg='lime',command=lambda:[s1.destroy(),enable()])
        b11.place(x=200,y=210)
    

def enable():
    b1.configure(state=NORMAL)
    b2.configure(state=NORMAL)
    b3.configure(state=NORMAL)
    b4.configure(state=NORMAL)
    b5.configure(state=NORMAL)

#deletedata--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def srdelete():
        srnod1=srnod.get()
        if srnod1=="" :
                mb.showinfo('Error',"Please Enter Sr. No.",parent=d1)
        else:
                srnod_info=srnod.get()
                mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
                cur=mydb.cursor()
                cur.execute('delete from animalinfo where Sr_No=%s',(srnod_info,))
                mydb.commit()
                mb.showinfo("Data Deleted","Record Deleted Successfully.",parent=d1)

def delete_data():
    global d1
    d1=LabelFrame(top,text='Update Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
    d1.place(x=20,y=350)

    global srnod
    srnod=StringVar()
    
    Label(d1,text="Enter Sr No of Record You Want To Delete",font=("Arial",17),bg="orange").place(x=40,y=50)
    Entry(d1,textvariable=srnod ,font=("Arial",18),bg="grey").place(x=140,y=110)
    Button(d1,text="Delete Data",font=('Arial',18),bg='Purple',command=srdelete).place(x=100,y=180)
    b8=Button(d1,text="Back ",font=("Arial",18),bg="lime",command=lambda:[d1.destroy(),enable()])
    b8.place(x=350,y=180)

#updatedata-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def habitatupdate1():
    habitatup_info=habitatup.get()
    srnoup_info=srnoup.get()
    
    if srnoup_info=="" or habitatup_info=="":
        mb.showinfo('Error',"Please Enter All Details.",parent=up3)
    else :
        mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        cur.execute('update animalinfo set Animal_Habitat= %s where Sr_No= %s',(habitatup_info,srnoup_info))
        mydb.commit()
        mb.showinfo("Data Updated","Record Updated Successfully.",parent=up4)

def habitatupdate():
    global up4
    up4=LabelFrame(top,text='Update Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
    up4.place(x=20,y=350)

    global habitatup
    global srnoup
    habitatup=StringVar()
    srnoup=StringVar()

    Label(up4,text="Sr. No",font=("Arial",17),bg="orange").place(x=50,y=50)
    Entry(up4,textvariable=srnoup ,font=("Arial",18),bg="grey").place(x=230,y=50)
    Label(up4,text="New Animal Habitat",font=("Arial",17),bg="orange").place(x=10,y=130)
    Entry(up4,textvariable=habitatup ,font=("Arial",18),bg="grey").place(x=230,y=130)
    Button(up4,text="Update Data",font=('Arial',18),bg='Purple',command=habitatupdate1).place(x=80,y=200)
    Button(up4,text="Back",font=('Arial',18),bg='Purple',command=up4.destroy).place(x=300,y=200)

def codeupdate1():
    codeup_info=codeup.get()
    srnoup_info=srnoup.get()
    
    if srnoup_info=="" or codeup_info=="":
        mb.showinfo('Error',"Please Enter All Details.",parent=up2)
    else :
        mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        cur.execute('update animalinfo set Animal_Code= %s where Sr_No= %s',(codeup_info,srnoup_info))
        mydb.commit()
        mb.showinfo("Data Updated","Record Updated Successfully.",parent=up3)

def codeupdate():
    global up3
    up3=LabelFrame(top,text='Update Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
    up3.place(x=20,y=350)

    global codeup
    global srnoup
    codeup=StringVar()
    srnoup=StringVar()

    Label(up3,text="Sr. No",font=("Arial",17),bg="orange").place(x=50,y=50)
    Entry(up3,textvariable=srnoup ,font=("Arial",18),bg="grey").place(x=230,y=50)
    Label(up3,text="New Animal Code",font=("Arial",17),bg="orange").place(x=10,y=130)
    Entry(up3,textvariable=codeup ,font=("Arial",18),bg="grey").place(x=230,y=130)
    Button(up3,text="Update Data",font=('Arial',18),bg='Purple',command=codeupdate1).place(x=80,y=200)
    Button(up3,text="Back",font=('Arial',18),bg='Purple',command=up3.destroy).place(x=300,y=200)
    
def breedupdate1():

    breedup_info=breedup.get()
    srnoup_info=srnoup.get()
    
    if srnoup_info=="" or breedup_info=="":
        mb.showinfo('Error',"Please Enter All Details.",parent=up1)
    else :
        mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        cur.execute('update animalinfo set Animal_Breed= %s where Sr_No= %s',(breedup_info,srnoup_info))
        mydb.commit()
        mb.showinfo("Data Updated","Record Updated Successfully.",parent=up2)

def breedupdate():
    global up2
    up2=LabelFrame(top,text='Update Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
    up2.place(x=20,y=350)

    global breedup
    global srnoup
    breedup=StringVar()
    srnoup=StringVar()

    Label(up2,text="Sr. No",font=("Arial",17),bg="orange").place(x=35,y=50)
    Entry(up2,textvariable=srnoup ,font=("Arial",18),bg="grey").place(x=230,y=50)
    Label(up2,text="New Animal Breed",font=("Arial",14),bg="orange").place(x=10,y=130)
    Entry(up2,textvariable=breedup ,font=("Arial",18),bg="grey").place(x=230,y=130)
    Button(up2,text="Update Data",font=('Arial',18),bg='Purple',command=breedupdate1).place(x=80,y=200)
    Button(up2,text="Back",font=('Arial',18),bg='Purple',command=up2.destroy).place(x=300,y=200)

def update_animal():
    global up1
    up1=LabelFrame(top,text='Update Data',font=('Arial',15),relief=FLAT,width =550,height=320,bg='white')
    up1.place(x=20,y=350)
    
    Button(up1,text="Upate Animal Breed",font=("Arial",17),bg="Purple",command=breedupdate).place(x=98,y=30)
    Button(up1,text="Upate Animal Code",font=("Arial",17),bg="Purple",command=codeupdate).place(x=100,y=110)
    Button(up1,text="Upate Animal Habitat",font=("Arial",17),bg="Purple",command=habitatupdate).place(x=97,y=190)
    b7=Button(up1,text="Back ",font=("Arial",17),bg="lime",command=lambda:[up1.destroy(),enable()])
    b7.place(x=350,y=110)

#adddata---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def add():

    global srno_info
    global breed_info
    global code_info
    global habitat_info

    srno_info=srno_add.get()
    breed_info=breed_add.get()
    code_info=code_add.get()
    habitat_info=habitat_add.get()
    
    if srno_info=="" or breed_info=="" or code_info=="":
        mb.showinfo('Error',"Please Enter All Details.",parent=ad)
    else:
            try:
                 mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
                 cur=mydb.cursor()
                 cur.execute('insert into animalinfo values(%s,%s,%s,%s)',(srno_info,breed_info,code_info,habitat_info))
                 mydb.commit()
                 mb.showinfo("Data Added","Record Added Successfully.",parent=top)
            except:
                    mb.showinfo('Error','Sr.No. already exists',parent=top)
        
def add_data():
    global ad 
    ad=LabelFrame(top,text="Add Data",font=("Arial",15),relief=FLAT,width=550,height=320,bg='white')
    ad.place(x=20,y=350)

    global srno_add
    global breed_add
    global code_add
    global habitat_add
        
    srno_add=StringVar()
    breed_add=StringVar()
    code_add=StringVar()
    habitat_add=StringVar()
    
    Label(ad,text="Sr. no.",font=("Arial",17),bg="orange").place(x=20,y=30)
    Entry(ad,textvariable= srno_add,font=("Arial",18),bg="grey").place(x=200,y=30)
    
    Label(ad,text="Animal Breed",font=("Arial",17),bg="orange").place(x=20,y=80)
    Entry(ad,textvariable= breed_add,font=("Arial",18),bg="grey").place(x=200,y=80)

    Label(ad,text="Animal Code",font=("Arial",17),bg="orange").place(x=20,y=130)
    Entry(ad,textvariable= code_add,font=("Arial",18),bg="grey").place(x=200,y=130)

    Label(ad,text="Animal Habitat",font=("Arial",17),bg="orange").place(x=20,y=180)
    Entry(ad,textvariable= habitat_add,font=("Arial",18),bg="grey").place(x=200,y=180)

    Button(ad,text="Add ",font=("Arial",18),bg="Purple",command=add).place(x=100,y=230)
    b6=Button(ad,text="Back ",font=("Arial",18),bg="Purple",command=lambda:[ad.destroy(),enable()])
    b6.place(x=300,y=230)
    
    
def disable():
    b1.configure(state=DISABLED,bg='black')
    b2.configure(state=DISABLED,background='yellow')
    b3.configure(state=DISABLED,background='yellow')
    b4.configure(state=DISABLED,background='yellow')
    b5.configure(state=DISABLED,background='yellow')

#loginwindow--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def loginwin():

    global top
    global b1
    global b2
    global b3
    global b4
    global b5
    
    top=Toplevel(root)
    canva=Canvas(top,width=1200,height=675)
    img1=ImageTk.PhotoImage(Image.open("C:\\Users\\Shivraj\\Documents\\Project_File\\Lion_Image1.jpg"),master=top)
    canva.create_image(0,0,anchor=NW,image=img1)
    canva.theimg=img1
    canva.pack()

    loginlabel=LabelFrame(top,text="Login Successfull",font=("Arial",15),relief=FLAT,width=550,height=320,bg='white').place(x=20,y=20)
    
    b1=Button(top,text='Log Out',font=('Arial',15),bg='black',fg='white',command=lambda:[top.destroy()])
    b1.place(x=225,y=170)
    b2=Button(top,text='Add Data',font=('Arial',15),bg='yellow',command=lambda:[disable(),add_data()])
    b2.place(x=120,y=90)
    b3=Button(top,text='Update Data',font=('Arial',15),bg='yellow',command=lambda:[disable(),update_animal()])
    b3.place(x=320,y=90)
    b4=Button(top,text='Delete Data',font=('Arial',15),bg='yellow',command=lambda:[disable(),delete_data()])
    b4.place(x=110,y=250)
    b5=Button(top,text='Show Data',font=('Arial',15),bg='yellow',command=lambda:[disable(),show_data()])
    b5.place(x=325,y=250)

def login_user():
    uname_info=username.get()
    passwd_info=password.get()
    if uname_info=='' or passwd_info=='':
        mb.showinfo('Error','Please Enter All Details.')
    else:
        mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
        cur=mydb.cursor()
        cur.execute('select username,password from userinfo where username=%s and password=%s',(uname_info,passwd_info))
        myrecords=cur.fetchall()
        count=cur.rowcount
        if count==0:
            mb.showinfo('Error','No User Found')
        else:
            for x in myrecords:
                Username=x[0]
                
                Password=x[1]
            if Username==uname_info and Password==passwd_info:
                loginwin()
            else:
                mb.showinfo('Error','Username or Password Is Invalid.')
    
#registrationwindow-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def register_user():

    username_info=username_reg.get()
    password_info=password_reg.get() 
    city_info=city.get()
    email_info=email.get()

    try:
            mydb=ms.connect(host='localhost',user='root',passwd='1234',database='wildlife_sanctuary')
            cur=mydb.cursor()
            sql="insert into userinfo values(%s,%s,%s,%s)"
            val=(username_info,password_info,email_info,city_info)
            cur.execute(sql,val)
            mydb.commit()
            mb.showinfo("Registration","Registration Successfull.",parent=reg)
    except:
            mb.showinfo("Error",'Username already exists.')

def check_email():

    username_info=username_reg.get()
    password_info=password_reg.get()
    city_info=city.get()
    email_info=email.get()
    
    email_info=email.get()
    checking='^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
    
    if  username_info=="" or password_info=="" or email_info=="" or city_info=="":
        mb.showinfo("Error","Please Enter All Details.",parent=reg)   
    
    elif(re.search(checking,email_info)):
        register_user()
    else:
        mb.showinfo("Error","Please Enter Valid Email",parent=reg)


def registration():

    global reg
    global username_reg
    global password_reg
    global email
    global city

    reg=LabelFrame(root,text="Registration",font=("Arial",15),width=800,height=350,bg="orange",borderwidth=7,relief='groove',labelanchor='n')
    reg.place(x=230,y=150)
    
    username_reg=StringVar()
    password_reg=StringVar()
    email=StringVar()
    city=StringVar()


    Label(reg,text="Username",font=("Arial",25),bg="orange").place(x=100,y=10)
    Entry(reg,textvariable= username_reg,font=("Arial",25),bg="cyan").place(x=380,y=10)

    Label(reg,text="Password",font=("Arial",25),bg="orange").place(x=100,y=70)
    Entry(reg,textvariable=password_reg,font=("Arial",25),bg="cyan").place(x=380,y=70)

    Label(reg,text="Email",font=("Arial",25),bg="orange").place(x=100,y=130)
    Entry(reg,textvariable=email,font=("Arial",25),bg="cyan").place(x=380,y=130)

    Label(reg,text="City",font=("Arial",25),bg="orange").place(x=100,y=190)
    Entry(reg,textvariable=city,font=("Arial",25),bg="cyan").place(x=380,y=190)

    Button(reg,text="Register",font=("Arial",17),bg="orange",command=check_email).place(x=270,y=250)
    Button(reg,text="Back",font=("Arial",17),bg="orange",command=reg.destroy).place(x=450,y=250)
    
#mainwindow------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def main_window():
    global root
    global canvas
    root=Tk()
    root.title("Wildlife Sanctuary Data Management")
    root.geometry("1200x680")
    
    canvas=Canvas(root,width=1200,height=680)
    img=ImageTk.PhotoImage(Image.open("C:\\Users\Shivraj\\Documents\\Project_File\\login_img1.jpg "),master=root)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack(fill=BOTH)
    global login
    global password
    global e2
    global username
    username=StringVar()
    password=StringVar()

    Entry(root,textvariable=username,font=("Arial",27),bg="sky blue").place(x=600,y=180)
    Entry(root,textvariable=password,show="*",font=("Arial",27),bg="sky blue").place(x=600,y=284)

    Button(root,text="Login",font=("Arial",28),bg="dark orange",fg='black',command=lambda:[login_user()]).place(x=410,y=400)
    Button(root,text="Register",font=("Arial",28),bg="dark orange",fg='black',command=lambda:[registration()]).place(x=580,y=400)


    root.mainloop()

main_window()

