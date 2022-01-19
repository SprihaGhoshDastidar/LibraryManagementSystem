from tkinter import*
from tkinter import ttk
import mysql.connector

from tkinter import messagebox
import datetime

class Library_management_system:
    def __init__(self,root,):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1550x1000")

        #variables
        self.memberv=StringVar()
        self.prnv=StringVar()
        self.titlev=StringVar()
        self.firstnamev=StringVar()
        self.lastnamev=StringVar()
        self.ad1v=StringVar()
        self.ad2v=StringVar()
        self.postcodev=StringVar()
        self.mobilev=StringVar()
        self.bookidv=StringVar()
        self.booktitlev=StringVar()
        self.authorv=StringVar()
        self.issuev=StringVar()
        self.dateduev=StringVar()
        self.daysv=StringVar()
        self.finev=StringVar()
        self.overduev=StringVar()
        self.pricev=StringVar()

        #setting label
        lbltitle=Label(self.root,text="CENTRAL LIBRARY DATABASE", bg="light yellow", fg="red",bd=20,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        #outer frame
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="pink")
        frame.place(x=0,y=98,width=1530,height=400)

        #Left Data Frame
        Data_frame_left=LabelFrame(frame,text="Membership Information", bg="light yellow", fg="red",bd=12,relief=RIDGE,font=("times new roman",18,"bold"))
        Data_frame_left.place(x=0,y=5,width=900,height=350)

        #Member label
        lblmember=Label(Data_frame_left, text="Member Type",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)

        commember=ttk.Combobox(Data_frame_left,textvar=self.memberv,state="readonly", font=("arial",8,"bold"),width=50)
        commember["value"]=("Admin","Lecturer","Student")
        commember.current(0)
        commember.grid(row=0,column=1)

        lblprn=Label(Data_frame_left, text="PRN No",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6)
        lblprn.grid(row=1,column=0,sticky=W)
        txtprn=Entry(Data_frame_left,textvar=self.prnv,font=("arial",8,"bold"),width=53)
        txtprn.grid(row=1,column=1)

        lbltitle=Label(Data_frame_left,text="ID no",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lbltitle.grid(row=2,column=0,sticky=W)
        txttitle=Entry(Data_frame_left,textvar=self.titlev,font=("arial",8,"bold"),width=53)
        txttitle.grid(row=2,column=1)

        lblfirstname=Label(Data_frame_left,text="First Name",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblfirstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(Data_frame_left,textvar=self.firstnamev,font=("arial",8,"bold"),width=53)
        txtfirstname.grid(row=3,column=1)

        lbllastname=Label(Data_frame_left,text="Last Name",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lbllastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(Data_frame_left,textvar=self.lastnamev,font=("arial",8,"bold"),width=53)
        txtlastname.grid(row=4,column=1)

        lblad1=Label(Data_frame_left,text="Present Address",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblad1.grid(row=5,column=0,sticky=W)
        txtad1=Entry(Data_frame_left,textvar=self.ad1v,font=("arial",8,"bold"),width=53)
        txtad1.grid(row=5,column=1)

        lblad2=Label(Data_frame_left,text="Permanent Address",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblad2.grid(row=6,column=0,sticky=W)
        txtad2=Entry(Data_frame_left,textvar=self.ad2v,font=("arial",8,"bold"),width=53)
        txtad2.grid(row=6,column=1)

        lblpostalcode=Label(Data_frame_left,text="Postal Code",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblpostalcode.grid(row=7,column=0,sticky=W)
        txtpostalcode=Entry(Data_frame_left,textvar=self.postcodev,font=("arial",8,"bold"),width=53)
        txtpostalcode.grid(row=7,column=1)

        lblphone=Label(Data_frame_left,text="Phone No",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblphone.grid(row=8,column=0,sticky=W)
        txtphone=Entry(Data_frame_left,textvar=self.mobilev,font=("arial",8,"bold"),width=53)
        txtphone.grid(row=8,column=1)

        lblbookid=Label(Data_frame_left,text="Book ID",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblbookid.grid(row=0,column=2,sticky=W)
        txtbookid=Entry(Data_frame_left,textvar=self.bookidv,font=("arial",8,"bold"),width=35)
        txtbookid.grid(row=0,column=3)

        lblbooktitle=Label(Data_frame_left,text="Book Title",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblbooktitle.grid(row=1,column=2,sticky=W)
        txtbooktitle=Entry(Data_frame_left,textvar=self.booktitlev,font=("arial",8,"bold"),width=35)
        txtbooktitle.grid(row=1,column=3)

        lblauthname=Label(Data_frame_left,text="Author Name",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblauthname.grid(row=2,column=2,sticky=W)
        txtauthname=Entry(Data_frame_left,textvar=self.authorv,font=("arial",8,"bold"),width=35)
        txtauthname.grid(row=2,column=3)

        lbldateborrowed=Label(Data_frame_left,text="Date of Issue",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lbldateborrowed.grid(row=3,column=2,sticky=W)
        txtdateborrowed=Entry(Data_frame_left,textvar=self.issuev,font=("arial",8,"bold"),width=35)
        txtdateborrowed.grid(row=3,column=3)

        lblpdue=Label(Data_frame_left,text="Date Due",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblpdue.grid(row=4,column=2,sticky=W)
        txtdue=Entry(Data_frame_left,textvar=self.dateduev,font=("arial",8,"bold"),width=35)
        txtdue.grid(row=4,column=3)

        lbldays=Label(Data_frame_left,text="Days on Book",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lbldays.grid(row=5,column=2,sticky=W)
        txtdays=Entry(Data_frame_left,textvar=self.daysv,font=("arial",8,"bold"),width=35)
        txtdays.grid(row=5,column=3)


        lblfine=Label(Data_frame_left,text="Late Return Fine(Rs.)",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblfine.grid(row=6,column=2,sticky=W)
        txtfine=Entry(Data_frame_left,textvar=self.finev,font=("arial",8,"bold"),width=35)
        txtfine.grid(row=6,column=3)

        lbloverdue=Label(Data_frame_left,text="Date Overdue",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lbloverdue.grid(row=7,column=2,sticky=W)
        txtoverdue=Entry(Data_frame_left,textvar=self.overduev,font=("arial",8,"bold"),width=35)
        txtoverdue.grid(row=7,column=3)

        lblprice=Label(Data_frame_left,text="Actual Price",bg="light yellow",font=("times new roman",12,"bold"),padx=8,pady=6 )
        lblprice.grid(row=8,column=2,sticky=W)
        txtprice=Entry(Data_frame_left,textvar=self.pricev,font=("arial",8,"bold"),width=35)
        txtprice.grid(row=8,column=3)

        #Right Data frame
        Data_frame_right=LabelFrame(frame,text="Book Details", bg="light yellow", fg="red",bd=12,relief=RIDGE,font=("times new roman",18,"bold"),padx=2,pady=6)
        Data_frame_right.place(x=910,y=5,width=540,height=350)

        self.txtbox=Text(Data_frame_right, font=("times new roman",12,"bold"),width=39,height=15, padx=2, pady=6)
        self.txtbox.grid(row=0,column=2)

        listscrollbar=Scrollbar(Data_frame_right)
        listscrollbar.grid(row=0,column=1,sticky=NS)
        booklist=['Python Programming', 'Advanced Coding with python',"Basics of C++","Compiler Design", "Science in Mathematics", "Introduction to Philosophy", "Basics of coding", "Top 10 Project ideas",'Starting to code','Introduction to C++','Data Structures with C',"ML with python","MySQL database","Object Oriented Programming","Python Cookbook","Artificial Intelligence","Introduction to Arduino","Netwotking","Ethical Hacking complete course","Basic HTML"]

        def select_book(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="Python Programming"):
                self.bookidv.set("BKID5454")
                self.booktitlev.set("Python Programming")
                self.authorv.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(699)

            elif(x=="Advanced Coding with python"):
                self.bookidv.set("BKID5450")
                self.booktitlev.set("Advanced Coding with python")
                self.authorv.set("Rob Steve")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(788)

            elif(x=="Basics of C++"):
                self.bookidv.set("BKID5451")
                self.booktitlev.set("Basics of C++")
                self.authorv.set("Sunita Arora")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(485)

            elif(x=="Compiler Design"):
                self.bookidv.set("BKID5452")
                self.booktitlev.set("Compiler Design")
                self.authorv.set("Ravi Sethi")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(599)

            elif(x=="Science in Mathematics"):
                self.bookidv.set("BKID5453")
                self.booktitlev.set("Science in Mathematics")
                self.authorv.set("R.D.Sharma")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(813)

            elif(x=="Introduction to Philosophy"):
                self.bookidv.set("BKID4040")
                self.booktitlev.set("Introduction to Philosophy")
                self.authorv.set("Simon Blackburn")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(235)

            elif(x=="Basics of coding"):
                self.bookidv.set("BKID3031")
                self.booktitlev.set("Basics of coding")
                self.authorv.set("Vinita Jha")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(788)

            elif(x=="Top 10 Project ideas"):
                self.bookidv.set("BKID2022")
                self.booktitlev.set("Top 10 Project ideas")
                self.authorv.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(1099)

            elif(x=="Starting to code"):
                self.bookidv.set("BKID5455")
                self.booktitlev.set("Starting to code")
                self.authorv.set("A.K.Das")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(499)

            elif(x=="Introduction to C++"):
                self.bookidv.set("BKID6069")
                self.booktitlev.set("Introduction to C++")
                self.authorv.set("S.Arora")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(600)

            elif(x=="Data Structures with C"):
                self.bookidv.set("BKID6454")
                self.booktitlev.set("Data Structures with C")
                self.authorv.set("Kuashik Kendra")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(715)

            elif(x=="ML with python"):
                self.bookidv.set("BKID5456")
                self.booktitlev.set("ML with python")
                self.authorv.set("D.Jules")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(699)

            elif(x=="MySQL database"):
                self.bookidv.set("BKID5457")
                self.booktitlev.set("MySQL database")
                self.authorv.set("S.D.Kishore")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(285)

            if(x=="Object Oriented Programming"):
                self.bookidv.set("BKID5458")
                self.booktitlev.set("Object Oriented Programming")
                self.authorv.set("Pearson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(999)

            elif(x=="Python Cookbook"):
                self.bookidv.set("BKID5854")
                self.booktitlev.set("Python Cookbook")
                self.authorv.set("S.K.Das")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(199)

            elif(x=="Artificial Intelligence"):
                self.bookidv.set("BKID5459")
                self.booktitlev.set("Artificial Intelligence")
                self.authorv.set("Narita Sharma")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(566)

            elif(x=="Introduction to Arduino"):
                self.bookidv.set("BKID5410")
                self.booktitlev.set("Introduction to Arduino")
                self.authorv.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(499)

            elif(x=="Netwotking"):
                self.bookidv.set("BKID5414")
                self.booktitlev.set("Netwotking")
                self.authorv.set("Rahul Bose")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(788)

            elif(x=="Ethical Hacking complete course"):
                self.bookidv.set("BKID5415")
                self.booktitlev.set("Ethical Hacking complete course")
                self.authorv.set("Berry Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(1788)

            elif(x=="Basic HTML"):
                self.bookidv.set("BKID5254")
                self.booktitlev.set("Basic HTML")
                self.authorv.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.issuev.set(d1)
                self.dateduev.set(d3)
                self.daysv.set(15)
                self.finev.set(25)
                self.overduev.set("NO")
                self.pricev.set(455)




        listbox=Listbox(Data_frame_right,font=("times new roman",12,"bold"),width=20,height=15)
        listbox.bind("<<ListboxSelect>>",select_book)
        listbox.grid(row=0,column=0)
        listscrollbar.config(command=listbox.yview)

        for item in booklist:
            listbox.insert(END,item)


        #Button frame
        frame_button=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="light yellow")
        frame_button.place(x=0,y=500,width=1530,height=53)


        btndata=Button(frame_button,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=27,bg="red",fg="white")
        btndata.grid(row=0,column=0)

        btndata=Button(frame_button,command=self.show_data,text="Show Data",font=("times new roman",12,"bold"),width=27,bg="red",fg="white")
        btndata.grid(row=0,column=1)

        btndata=Button(frame_button,command=self.update,text="Update Data",font=("times new roman",12,"bold"),width=27,bg="red",fg="white")
        btndata.grid(row=0,column=2)

        btndata=Button(frame_button,command=self.reset,text="Reset Data",font=("times new roman",12,"bold"),width=27,bg="red",fg="white")
        btndata.grid(row=0,column=3)

        btndata=Button(frame_button,command=self.delete,text="Delete Data",font=("times new roman",12,"bold"),width=27,bg="red",fg="white")
        btndata.grid(row=0,column=4)

        btndata=Button(frame_button,command=self.exit,text="Exit",font=("times new roman",12,"bold"),width=26,bg="red",fg="white")
        btndata.grid(row=0,column=5)

        #information frame
        frame_details=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="pink")
        frame_details.place(x=0,y=555,width=1530,height=230)

        Table_frame=Frame(frame_details, bd=6,relief=RIDGE,bg="light yellow")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.librarytable=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","ad1","ad2","postid","mobile","bookid","booktitle","author","dateofissue","datedue","days","fine","dateoverdue","price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.librarytable.xview)
        yscroll.config(command=self.librarytable.yview)

        self.librarytable.heading("membertype",text="Member Type")
        self.librarytable.heading("prnno",text="PRN no")
        self.librarytable.heading("title",text="ID no")
        self.librarytable.heading("firstname",text="FirstName")
        self.librarytable.heading("lastname",text="LastName")
        self.librarytable.heading("ad1",text="Present Address")
        self.librarytable.heading("ad2",text="Permanent Address")
        self.librarytable.heading("postid",text="Postal code")
        self.librarytable.heading("mobile",text="Mobile no")
        self.librarytable.heading("bookid",text="Book id")
        self.librarytable.heading("booktitle",text="Book title")
        self.librarytable.heading("author",text="Author Name")
        self.librarytable.heading("dateofissue",text="Date Of Issue")
        self.librarytable.heading("datedue",text="Date due")
        self.librarytable.heading("days",text="Days on Book")
        self.librarytable.heading("fine",text="Late return fine")
        self.librarytable.heading("dateoverdue",text="Date overdue")
        self.librarytable.heading("price",text="Price")

        self.librarytable["show"]="headings"
        self.librarytable.pack(fill=BOTH,expand=1)

        self.librarytable.column("membertype",width=100)
        self.librarytable.column("prnno",width=90)
        self.librarytable.column("title",width=90)
        self.librarytable.column("firstname",width=100)
        self.librarytable.column("lastname",width=100)
        self.librarytable.column("ad1",width=130)
        self.librarytable.column("ad2",width=130)
        self.librarytable.column("postid",width=100)
        self.librarytable.column("mobile",width=100)
        self.librarytable.column("bookid",width=130)
        self.librarytable.column("booktitle",width=120)
        self.librarytable.column("author",width=100)
        self.librarytable.column("dateofissue",width=100)
        self.librarytable.column("datedue",width=100)
        self.librarytable.column("days",width=100)
        self.librarytable.column("fine",width=100)
        self.librarytable.column("dateoverdue",width=100)
        self.librarytable.column("price",width=100)

        self.fetch_data()
        self.librarytable.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):

        con=mysql.connector.connect(host="localhost",username="root",password="password",database="library_management")
        cr=con.cursor()
        cr.execute("insert into librarym values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.memberv.get(),
                                                                                                          self.prnv.get(),
                                                                                                          self.titlev.get(),
                                                                                                          self.firstnamev.get(),
                                                                                                          self.lastnamev.get(),
                                                                                                          self.ad1v.get(),
                                                                                                          self.ad2v.get(),
                                                                                                          self.postcodev.get(),
                                                                                                          self.mobilev.get(),
                                                                                                          self.bookidv.get(),
                                                                                                          self.booktitlev.get(),
                                                                                                          self.authorv.get(),
                                                                                                          self.issuev.get(),
                                                                                                          self.dateduev.get(),
                                                                                                          self.daysv.get(),
                                                                                                          self.finev.get(),
                                                                                                          self.overduev.get(),
                                                                                                          self.pricev.get()));
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo(title="Success",message="member added successfully")


    def update(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="library_management")
        cr=con.cursor()
        cr.execute("update librarym set Member=%s,ID_no=%s,FirstName=%s,LastName=%s,PresentAddress=%s,PermanentAddress=%s,PostalCode=%s,PhoneNumber=%s,Bookid=%s,BookTitle=%s,AuthorName=%s,DateOfIssue=%s,DateDue=%s,DaysonBook=%s,LateReturnFine=%s,DateOverdue=%s,Price=%s where PRN=%s",
                   (self.memberv.get(),
                    self.titlev.get(),
                    self.firstnamev.get(),
                    self.lastnamev.get(),
                    self.ad1v.get(),
                    self.ad2v.get(),
                    self.postcodev.get(),
                    self.mobilev.get(),
                    self.bookidv.get(),
                    self.booktitlev.get(),
                    self.authorv.get(),
                    self.issuev.get(),
                    self.dateduev.get(),
                    self.daysv.get(),
                    self.finev.get(),
                    self.overduev.get(),
                    self.pricev.get(),
                    self.prnv.get()));

        con.commit()
        self.fetch_data()
        self.reset()
        con.close()

        messagebox.showinfo("Success","Member updated successfully")
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="library_management")
        cr=con.cursor()
        cr.execute("select * from librarym")
        rows=cr.fetchall()
        if len(rows)!=0:
            self.librarytable.delete(*self.librarytable.get_children())
            for i in rows:
                self.librarytable.insert("",END,values=i)

            con.commit()
        con.close()
    def get_cursor(self,event=""):
        cursor_row=self.librarytable.focus()
        content=self.librarytable.item(cursor_row)
        row=content['values']

        self.memberv.set(row[0]),
        self.prnv.set(row[1]),
        self.titlev.set(row[2]),
        self.firstnamev.set(row[3]),
        self.lastnamev.set(row[4]),
        self.ad1v.set(row[5]),
        self.ad2v.set(row[6]),
        self.postcodev.set(row[7]),
        self.mobilev.set(row[8]),
        self.bookidv.set(row[9]),
        self.booktitlev.set(row[10]),
        self.authorv.set(row[11]),
        self.issuev.set(row[12]),
        self.dateduev.set(row[13]),
        self.daysv.set(row[14]),
        self.finev.set(row[15]),
        self.overduev.set(row[16]),
        self.pricev.set(row[17])

    def show_data(self):
        self.txtbox.insert(END,"Member Type:\t"+self.memberv.get() + "\n")
        self.txtbox.insert(END,"PRN:\t"+self.prnv.get() + "\n")
        self.txtbox.insert(END,"ID:\t"+self.titlev.get() + "\n")
        self.txtbox.insert(END,"FirstName: \t"+self.firstnamev.get() + "\n")
        self.txtbox.insert(END,"LastName:  \t"+self.lastnamev.get() + "\n")
        self.txtbox.insert(END,"Pr. Addr:  \t"+self.ad1v.get() + "\n")
        self.txtbox.insert(END,"Perm Addr: \t"+self.ad2v.get() + "\n")
        self.txtbox.insert(END,"PostalCode:\t"+self.postcodev.get() + "\n")
        self.txtbox.insert(END,"Mobile:    \t"+self.mobilev.get() + "\n")
        self.txtbox.insert(END,"Bookid:    \t"+self.bookidv.get() + "\n")
        self.txtbox.insert(END,"BookTitle: \t"+self.booktitlev.get() + "\n")
        self.txtbox.insert(END,"Author:    \t"+self.authorv.get() + "\n")
        self.txtbox.insert(END,"IssueDate: \t"+self.issuev.get() + "\n")
        self.txtbox.insert(END,"DueDate:   \t"+self.dateduev.get() + "\n")
        self.txtbox.insert(END,"DaysonBook:\t"+self.daysv.get() + "\n")
        self.txtbox.insert(END,"Fine:      \t"+self.finev.get() + "\n")
        self.txtbox.insert(END,"DateOverdue:\t"+self.overduev.get() + "\n")
        self.txtbox.insert(END,"Price:      \t"+self.pricev.get() + "\n")

    def reset(self):
        self.memberv.set(""),
        self.prnv.set(""),
        self.titlev.set(""),
        self.firstnamev.set(""),
        self.lastnamev.set(""),
        self.ad1v.set(""),
        self.ad2v.set(""),
        self.postcodev.set(""),
        self.mobilev.set(""),
        self.bookidv.set(""),
        self.booktitlev.set(""),
        self.authorv.set(""),
        self.issuev.set(""),
        self.dateduev.set(""),
        self.daysv.set(""),
        self.finev.set(""),
        self.overduev.set(""),
        self.pricev.set("")
        self.txtbox.delete("1.0",END)

    def exit(self):
        exit=messagebox.askyesno("Library System","Do you want to exit?")
        if exit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prnv.get()=="" or self.titlev.get()=="":
            messagebox.showerror("Error","First select the member")
        else:

            con=mysql.connector.connect(host="localhost",username="root",password="password",database="library_management")
            cr=con.cursor()
            query="delete from librarym where PRN=%s"
            value=(self.prnv.get(),)
            cr.execute(query,value)
            con.commit()
            self.fetch_data()
            self.reset()
            con.close()

            messagebox.showinfo("Success","Member deleted successfully")





























if __name__=="__main__":
    root=Tk()
    obj=Library_management_system(root)
    root.mainloop()