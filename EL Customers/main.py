# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:59:10 2022

@author: Admin
"""

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

class GUI:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Customer Management System")
        width = 700
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        self.root.config(bg="black")
        
        self.FIRSTNAME = StringVar()
        self.LASTNAME = StringVar()
        self.GENDER = StringVar()
        self.AGE = StringVar()
        self.ADDRESS = StringVar()
        self.CONTACT = StringVar()
        self.TRANSACTION = StringVar()
        self.AMOUNT = StringVar()
        self.STATUS = StringVar()
        
        
        self.Top = Frame(self.root, width=500, bd=1, relief=SOLID)
        self.Top.pack(side=TOP)
        self.Mid = Frame(self.root, width=500,  bg="black")
        self.Mid.pack(side=TOP)
        self.MidLeft = Frame(self.Mid, width=100)
        self.MidLeft.pack(side=LEFT, pady=10)
        self.MidLeftPadding = Frame(self.Mid, width=370, bg="black")
        self.MidLeftPadding.pack(side=LEFT)
        self.MidRight = Frame(self.Mid, width=100)
        self.MidRight.pack(side=RIGHT, pady=10)
        self.TableMargin = Frame(self.root, width=500)
        self.TableMargin.pack(side=TOP)
        #============================LABELS======================================
        self.lbl_title = Label(self.Top, text="Customer Management System", font=('arial', 16), width=500,bg="blue")
        self.lbl_title.pack(fill=X)

        #============================ENTRY=======================================

        #============================BUTTONS=====================================
        self.btn_add = Button(self.MidLeft, text="+ ADD NEW", bg="#66ff66", command=self.AddNewWindow)
        self.btn_add.pack()
        self.btn_delete = Button(self.MidRight, text="DELETE", bg="red", command=self.DeleteData)
        self.btn_delete.pack(side=RIGHT)

        #============================TABLES======================================
        self.scrollbarx = Scrollbar(self.TableMargin, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(self.TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Contact"), height=400, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('MemberID', text="MemberID", anchor=W)
        self.tree.heading('Firstname', text="First Name", anchor=W)
        self.tree.heading('Lastname', text="Last Name", anchor=W)
        self.tree.heading('Gender', text="Gender", anchor=W)
        self.tree.heading('Contact', text="Contact", anchor=W)
        #self.tree.heading('Address', text="Address", anchor=W)
        #self.tree.heading('Contact', text="Contact", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=180)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.OnSelected)
        
        self.root.mainloop()
        
    def AddNewWindow(self):
        NewWindow = Toplevel()
        NewWindow.title("Customer Management System")
        width = 400
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.resizable(0, 0)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        
        
        #===================FRAMES==============================
        FormTitle = Frame(NewWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(NewWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=self.GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=self.GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
        
        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Adding New Customer", font=('arial', 16), bg="#66ff66",  width = 300)
        lbl_title.pack(fill=X)
        lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
        lbl_firstname.grid(row=0, sticky=W)
        lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
        lbl_lastname.grid(row=1, sticky=W)
        lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
        lbl_gender.grid(row=2, sticky=W)
        lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
        lbl_age.grid(row=3, sticky=W)
        lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
        lbl_address.grid(row=4, sticky=W)
        lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
        lbl_contact.grid(row=5, sticky=W)
        lbl_transaction = Label(ContactForm, text="Transaction", font=('arial', 14), bd=5)
        lbl_transaction.grid(row=6, sticky=W)
        lbl_amount = Label(ContactForm, text="Amount", font=('arial', 14), bd=5)
        lbl_amount.grid(row=7, sticky=W)
        lbl_status = Label(ContactForm, text="Status", font=('arial', 14), bd=5)
        lbl_status.grid(row=8, sticky=W)
        

        #===================ENTRY===============================
        firstname = Entry(ContactForm, textvariable=self.FIRSTNAME, font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = Entry(ContactForm, textvariable=self.LASTNAME, font=('arial', 14))
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        age = Entry(ContactForm, textvariable=self.AGE,  font=('arial', 14))
        age.grid(row=3, column=1)
        address = Entry(ContactForm, textvariable=self.ADDRESS,  font=('arial', 14))
        address.grid(row=4, column=1)
        contact = Entry(ContactForm, textvariable=self.CONTACT,  font=('arial', 14))
        contact.grid(row=5, column=1)
        transaction = Entry(ContactForm, textvariable=self.TRANSACTION,  font=('arial', 14))
        transaction.grid(row=6, column=1)
        amount = Entry(ContactForm, textvariable=self.AMOUNT,  font=('arial', 14))
        amount.grid(row=7, column=1)
        status = Entry(ContactForm, textvariable=self.STATUS,  font=('arial', 14))
        status.grid(row=8, column=1)
        

        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save", width=50, command=self.SubmitData)
        btn_addcon.grid(row=9, columnspan=2, pady=10)
        
        
    def DeleteData(self):
        pass
    
    def OnSelected(self):
        pass
    
    def SubmitData(self):
        if  self.FIRSTNAME.get() == "" or self.LASTNAME.get() == "" or self.CONTACT.get() == "" or self.TRANSACTION.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            file = open("DB.csv", "a")
            
            file.write(self.FIRSTNAME.get() + "," + self.LASTNAME.get() + "," + self.GENDER.get() + "," + self.AGE.get() + "," + self.ADDRESS.get() + "," + self.CONTACT.get() + "," + self.TRANSACTION.get() + "," + self.AMOUNT.get() + "," + self.STATUS.get() + "\n")
            
            self.FIRSTNAME.set("")
            self.LASTNAME.set("")
            self.GENDER.set("")
            self.AGE.set("")
            self.ADDRESS.set("")
            self.CONTACT.set("")
            self.TRANSACTION.set("")
            self.AMOUNT.set("")
            self.STATUS.set("")
            
            
            file.close()
            
            
        
        
GUI()