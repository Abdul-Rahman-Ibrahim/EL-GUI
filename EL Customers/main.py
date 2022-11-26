# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:59:10 2022

@author: Abdul-Rahman Ibrahim
"""
import os
import webbrowser

from datetime import datetime
#now = datetime.now()
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

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
        
        self.btn_sales = Button(self.root, text="  SALES  ", bg="white", command=self.SalesWindow)
        self.btn_sales.place(x=337, y=42)
        
        self.btn_delete = Button(self.MidRight, text="DELETE", bg="red", command=self.DeleteData)
        self.btn_delete.pack(side=RIGHT)

        #============================TABLES======================================
        self.scrollbarx = Scrollbar(self.TableMargin, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(self.TableMargin, columns=("MemberID", "Lastname", "Firstname", "Gender", "Contact"), height=400, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('MemberID', text="MemberID", anchor=W)
        self.tree.heading('Lastname', text="Last Name", anchor=W)
        self.tree.heading('Firstname', text="First Name", anchor=W)
        self.tree.heading('Gender', text="Gender", anchor=W)
        self.tree.heading('Contact', text="Contact", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=180)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.OnSelected)

        try:
            file = open("DB.csv", "r")
            db = file.readlines()
            db.sort()
            for line in db:
                line = line.strip().split(',')
                id, lastname, firstname, gender, contact = line[-1], line[0], line[1], line[2], line[5]
                tup = (id, lastname.title(), firstname.title(), gender, contact)
                self.tree.insert('', 'end', values=(tup))

            file.close()
        except:
            pass
        
        self.root.mainloop()
        
    def AddNewWindow(self):
        self.FIRSTNAME.set("")
        self.LASTNAME.set("")
        self.GENDER.set("")
        self.AGE.set("")
        self.ADDRESS.set("")
        self.CONTACT.set("")
        self.TRANSACTION.set("")
        self.AMOUNT.set("")
        self.STATUS.set("")
        self.NewWindow = Toplevel()
        self.NewWindow.title("Customer Management System")
        width = 400
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        self.NewWindow.resizable(0, 0)
        self.NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        
        
        #===================FRAMES==============================
        FormTitle = Frame(self.NewWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(self.NewWindow)
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
        

        #===================ENTRY================================
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
        if not self.tree.selection():
            tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = self.tree.focus()
                contents =(self.tree.item(curItem))
                selecteditem = contents['values']
                self.tree.delete(curItem)
                file = open('DB.csv')
                tmpfile = open('DB.tmp', 'w')
                for line in file:
                    if line.strip().split(',')[:3] != selecteditem[1:-1]:
                        tmpfile.write(line)
                file.close()
                tmpfile.close()
                os.remove('DB.csv')
                os.rename('DB.tmp', 'DB.csv')
                 
    def OnSelected(self, event):
        try:
            if self.NewWindow:
                self.NewWindow.destroy()
        except AttributeError:
            pass
        try:
            if self.UpdateWindow:
                self.UpdateWindow.destroy()
        except AttributeError:
            pass
                
        curItem = self.tree.focus()
        contents =(self.tree.item(curItem))
        self.selecteditem = contents['values']
        mem_id = self.selecteditem[0]
        self.FIRSTNAME.set("")
        self.LASTNAME.set("")
        self.GENDER.set("")
        self.AGE.set("")
        self.ADDRESS.set("")
        self.CONTACT.set("")
        self.FIRSTNAME.set(self.selecteditem[2])
        self.LASTNAME.set(self.selecteditem[1])
        self.GENDER.set(self.selecteditem[3])
        self.CONTACT.set(self.selecteditem[4])

        try:
            file = open('DB.csv')
            for line in file:
                if line.strip().split(',')[-1] == str(mem_id):
                    line = line.strip().split(',')
                    lastname, firstname, gender, age, address, contact, transaction, amount, status, id = line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[-1]
                    self.AGE.set(age)
                    self.ADDRESS.set(address)
                    break
            file.close()
        except AttributeError:
            pass
        
        ask = tkMessageBox.askyesno('', 'Make new Transaction for {0}'.format(self.LASTNAME.get()))
        if ask:
            self.UpdateWindow = Toplevel()
            self.UpdateWindow.title("Customer Management System")
            width = 400
            height = 400
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            x = ((screen_width/2) + 450) - (width/2)
            y = ((screen_height/2) + 20) - (height/2)
            self.UpdateWindow.resizable(0, 0)
            self.UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))


            #===================FRAMES==============================
            FormTitle = Frame(self.UpdateWindow)
            FormTitle.pack(side=TOP)
            ContactForm = Frame(self.UpdateWindow)
            ContactForm.pack(side=TOP, pady=10)
            RadioGroup = Frame(ContactForm)
            Male = Radiobutton(RadioGroup, text="Male", variable=self.GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
            Female = Radiobutton(RadioGroup, text="Female", variable=self.GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
            
            #===================LABELS==============================
            lbl_title = Label(FormTitle, text="Making New Transaction", font=('arial', 16), bg="#66ff66",  width = 300)
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
            btn_addcon = Button(ContactForm, text="Update", width=50, command=self.UpdateData)
            btn_addcon.grid(row=9, columnspan=2, pady=10)
            
            
            
        else:
            self.customerWindow = Toplevel()
            self.customerWindow.title(self.LASTNAME.get())
            width = 600
            height = 400
            screen_width = self.customerWindow.winfo_screenwidth()
            screen_height = self.customerWindow.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            self.customerWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
            self.customerWindow.resizable(0, 0)
            #self.customerWindow.config(bg="black")
            
            self.date = StringVar()
            self.time = StringVar()
            self.address = StringVar()
            self.age = StringVar()
            self.transaction = StringVar()
            self.amount = StringVar()
            self.status = StringVar()
            self.id = StringVar()

            
            
            self.CustomerTop = Frame(self.customerWindow, width=500, bd=1, relief=SOLID)
            self.CustomerTop.pack(side=TOP)
            self.CustomerMid = Frame(self.customerWindow, width=500,  bg="black")
            self.CustomerMid.pack(side=TOP)
            #self.CustomerMidLeft = Frame(self.CustomerMid, width=100)
            #self.CustomerMidLeft.pack(side=LEFT, pady=10)
            #elf.CustomerMidLeftPadding = Frame(self.CustomerMid, width=370, bg="black")
            #self.CustomerMidLeftPadding.pack(side=LEFT)
            #self.CustomerMidRight = Frame(self.CustomerMid, width=100)
            #self.CustomerMidRight.pack(side=RIGHT, pady=10)
            self.CustomerTableMargin = Frame(self.customerWindow, width=500)
            self.CustomerTableMargin.pack(side=TOP)
            #============================LABELS======================================
            self.Customerlbl_title = Label(self.CustomerTop, text=self.LASTNAME.get(), font=('arial', 16), width=500,bg="blue")
            self.Customerlbl_title.pack(fill=X)

            #============================ENTRY=======================================

            #============================BUTTONS=====================================
            #self.btn_add = Button(self.MidLeft, text="+ ADD NEW", bg="#66ff66", command=self.AddNewWindow)
            #self.btn_add.pack()
            #self.btn_delete = Button(self.MidRight, text="DELETE", bg="red", command=self.DeleteData)
            #self.btn_delete.pack(side=RIGHT)

            #============================TABLES======================================
            self.Customerscrollbarx = Scrollbar(self.CustomerTableMargin, orient=HORIZONTAL)
            self.Customerscrollbary = Scrollbar(self.CustomerTableMargin, orient=VERTICAL)
            self.Customertree = ttk.Treeview(self.CustomerTableMargin, columns=("MemberID", "Date", "Time", "Address", "Age", "Transaction", "Amount", "Status"), height=400, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.Customerscrollbary.config(command=self.Customertree.yview)
            self.Customerscrollbary.pack(side=RIGHT, fill=Y)
            self.Customerscrollbarx.config(command=self.Customertree.xview)
            self.Customerscrollbarx.pack(side=BOTTOM, fill=X)
            self.Customertree.heading('MemberID', text="MemberID", anchor=W)
            self.Customertree.heading('Date', text="Date", anchor=W)
            self.Customertree.heading('Time', text="Time", anchor=W)
            self.Customertree.heading('Address', text="Address", anchor=W)
            self.Customertree.heading('Age', text="Age", anchor=W)
            self.Customertree.heading('Transaction', text="Transaction", anchor=W)
            self.Customertree.heading('Amount', text="Amount", anchor=W)
            self.Customertree.heading('Status', text="Status", anchor=W)
            self.Customertree.column('#0', stretch=NO, minwidth=0, width=0)
            self.Customertree.column('#1', stretch=NO, minwidth=0, width=0)
            self.Customertree.column('#2', stretch=NO, minwidth=0, width=90)
            self.Customertree.column('#3', stretch=NO, minwidth=0, width=80)
            self.Customertree.column('#4', stretch=NO, minwidth=0, width=90)
            self.Customertree.column('#5', stretch=NO, minwidth=0, width=90)
            self.Customertree.column('#6', stretch=NO, minwidth=0, width=90)
            self.Customertree.column('#7', stretch=NO, minwidth=0, width=90)
            self.Customertree.pack()
            
            file = open('Customers/'+str(mem_id)+'.csv')
            content = file.readlines()
            content.reverse()
            for line in content:
                line = line.strip().split(',')
                id, (date, time), address, age, transaction, amount, status = line[-1], line[0].split(), line[1], line[2], line[3], line[4], line[5]
                tup = (id, date, time, address, age, transaction, amount, status)
                self.Customertree.insert('', 'end', values=(tup))
            file.close()
            
        
    
    def SubmitData(self):
        if  self.FIRSTNAME.get() == "" or self.LASTNAME.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            ids = open('ids.in')
            tmpids = open('ids.tmp', 'w')
            id = ids.readline().strip()
            id = int(id) + 1

            tmpids.write(str(id))
            ids.close()
            tmpids.close()

            os.remove('ids.in')
            os.rename('ids.tmp', 'ids.in')

            self.tree.delete(*self.tree.get_children())
            file = open("DB.csv", "a")
            
            file.write(self.LASTNAME.get().title() + "," + self.FIRSTNAME.get().title() + "," + self.GENDER.get() + "," + self.AGE.get() + "," + self.ADDRESS.get() + "," + self.CONTACT.get() + "," + self.TRANSACTION.get() + "," + self.AMOUNT.get() + "," + self.STATUS.get() + "," + str(id) + "\n")
            file.close()
            
            file = open('Customers/'+str(id)+'.csv', 'a')
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            file.write(dt_string + "," + self.ADDRESS.get() + "," + self.AGE.get() + "," + self.TRANSACTION.get()+ "," + self.AMOUNT.get() +  "," + self.STATUS.get() + "," + str(id) + "\n")
            
            file.close()
            
            
            self.AddSales()
            
            self.FIRSTNAME.set("")
            self.LASTNAME.set("")
            self.GENDER.set("")
            self.AGE.set("")
            self.ADDRESS.set("")
            self.CONTACT.set("")
            self.TRANSACTION.set("")
            self.AMOUNT.set("")
            self.STATUS.set("")

            file = open("DB.csv", "r")
            db = file.readlines()
            db.sort()
            for line in db:
                line = line.strip().split(',')
                id, lastname, firstname, gender, contact = str(id), line[0], line[1], line[2], line[5]
                tup = (id, lastname.title(), firstname.title(), gender, contact)
                self.tree.insert('', 'end', values=(tup))

            file.close()


    def UpdateData(self):
        mem_id = self.selecteditem[0]
        
        file = open('DB.csv')
        tmpfile = open('DB.tmp', 'w')
        for line in file:
            if line.strip().split(',')[-1] == str(mem_id):
                tmpfile.write(self.LASTNAME.get().title() + "," + self.FIRSTNAME.get().title() + "," + self.GENDER.get() + "," + self.AGE.get() + "," + self.ADDRESS.get() + "," + self.CONTACT.get() + "," + self.TRANSACTION.get() + "," + self.AMOUNT.get() + "," + self.STATUS.get() + "," + str(mem_id) + "\n")
            else:
                tmpfile.write(line)

        file.close()
        tmpfile.close()

        os.remove('DB.csv')
        os.rename('DB.tmp', 'DB.csv')

        self.tree.delete(*self.tree.get_children())
        file = open('DB.csv')
        db = file.readlines()
        db.sort()
        for line in db:
            line = line.strip().split(',')
            id, lastname, firstname, gender, contact = line[-1], line[0], line[1], line[2], line[5]
            tup = (id, lastname.title(), firstname.title(), gender, contact)
            self.tree.insert('', 'end', values=(tup))

        file.close()
        
        if self.AMOUNT.get() != '':
            file = open('Customers/'+str(mem_id)+'.csv', 'a')
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
            file.write(dt_string + "," + self.ADDRESS.get() + "," + self.AGE.get() + "," + self.TRANSACTION.get()+ "," + self.AMOUNT.get() +  "," + self.STATUS.get() + "," + str(id) + "\n")
        
            file.close()
            
            self.AddSales()
            
        self.TRANSACTION.set("")
        self.AMOUNT.set("")
        self.STATUS.set("")     
        
    def AddSales(self):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y")
        try:
            op = open('Sales/'+dt_string+'.in')
            Csale = float(op.readline().strip())
            Asale = float(op.readline().strip())
            op.close()
        except:
            Csale = 0
            Asale = 0

        file = open('Sales/'+dt_string+'.in', 'w')
        if self.LASTNAME.get().lower() != 'el':
            Csale += float(self.AMOUNT.get())
            Asale += 0
        else:
            Csale += 0
            Asale += float(self.AMOUNT.get())
        file.write(str(Csale)+'\n')
        file.write(str(Asale)+'\n')
        
        file.close()
        
        file = open('Sales/dates.in', 'a')
        file.write(dt_string +'\n')
        file.close()
        
    def SalesWindow(self):
            
        file = open('Sales/dates.in')
        to_write = open('Sales/sales.txt', 'w')
        to_write.write('Date                ' + 'Admin Sale         ' + 'Customer Sale          ' + 'Profit' + '\n')
        content = list(set(file.readlines()))
        for date in content:
            tmp = open('Sales/'+date.strip()+'.in')
            
            Csale = float(tmp.readline().strip())
            Asale = float(tmp.readline().strip())
            Profit = Csale - Asale
            to_write.write(date.strip() + '          ' + str(Asale) + '              ' + str(Csale)+'                 ' +str(Profit)+'\n')
            
            tmp.close()
        
        to_write.close()
            
        file.close()
        
        path = os.getcwd() + '/Sales/'
        print(path)
        webbrowser.open(path + 'sales.txt')
        
             
if __name__=='__main__':        
        
    GUI()
