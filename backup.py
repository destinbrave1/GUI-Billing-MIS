from tkinter import messagebox
import tkinter as tk
from tkinter import *
import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfilename  # to help me save my work
from tkinter import ttk # to help me have a treeview

class Login:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        self.window.geometry('1200x700')
        self.window.configure(bg='#333333') # bg stands for background, and fg stands for for ground

        #create a frame (to help make our GUI more responsive
        self.frame=tk.LabelFrame(self.window, text='Login page',bg='#333333',fg='white', width=15, height=10, font=("Times new romman",13,'bold'), relief=GROOVE)
        #creating widgets

        self.login_label=tk.Label(self.frame, text='\nLOGIN', bg='#333333', fg='#ff0000', font=("Times new romman",13,'bold'), relief=GROOVE, padx=20)
        self.username_label=tk.Label(self.frame, text='Username', bg='#333333', fg='#FFFFFF',font=("Times new romman",13,'bold'), relief=GROOVE)
        self.username_entry=tk.Entry(self.frame, font=('Arial',16))
        self.password_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.password_label=tk.Label(self.frame, text='Password', bg='#333333', fg='#FFFFFF',font=("Times new romman",13,'bold'), relief=GROOVE)

        self.confirm_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.confirm_label=tk.Label(self.frame, text='Confirm', bg='#333333', fg='#FFFFFF',font=("Times new romman",13,'bold'), relief=GROOVE)

        self.Login_button=tk.Button(self.frame, text='Login', bg='#ff0000', fg='white', command=self.login)
        self.register_button=tk.Button(self.frame, text="Exit", bg='#ff0000', fg='white',command=self.window.destroy)

        #Placing widgets on the screen
        
        self.login_label.grid(row=0, column=0, columnspan=3, sticky='news', padx=30)
      
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.password_label.grid(row=2, column=0)

        self.confirm_label.grid(row=3, column=0)
        self.confirm_entry.grid(row=3, column=1, pady=20)
       
        self.register_button.grid(row=7, column=3, columnspan=1, padx= 10,pady=10)
        self.Login_button.grid(row=7, column=2, columnspan=1, padx= 1,pady=10)

        #packing a frame
        self.frame.pack(padx=150, pady=100)
        self.window.mainloop()
                
    #function to fetch data from database 
    def login(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CREDENTIALS",auth_plugin='mysql_native_password')
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()
        self.confirm=self.confirm_entry.get()
             
        while(True):
            self.cursor1=db.cursor()

            self.selectname ="select * from USERS where USERNAME=%s"
            self.cursor1.execute(self.selectname,[self.username])
            self.result1=self.cursor1.fetchall()

            #checking if they match

            if not self.result1:
                messagebox.showerror(title='Username!', message='Invalid Username')
                break
            
            self.cursor2=db.cursor()
            self.selectpassword="select * from USERS where PASSWORD=%s"
           
            self.cursor2.execute(self.selectpassword,[self.password])
            self.result2=self.cursor2.fetchall()

            if not (self.username_entry.get()):
                messagebox.showerror(title='Identification', message='Enter your username')
                break
            elif not (self.password_entry.get()):
                messagebox.showerror(title='Password', message='Enter your password')
                break
            elif not (self.confirm_entry.get()):
                messagebox.showerror(title='Password', message='Confirm your password')
                break

            elif not self.result2:
                messagebox.showerror(title='password!', message='Invalid Password')
                break        
               
            elif (self.confirm!=self.password):
                messagebox.showerror(title='Invalid', message='Passwords do not match')  
                break
            
            else:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)
                self.window.destroy()
                Facture()
                break

class Registration():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        self.window.geometry('800x620')
        self.window.configure(bg='#333333') # bg stands for background, and fg stands for for ground

        #create a frame (to help make our GUI more responsive
        self.frame=tk.Frame(self.window,bg='#333333', width=15, height=10)
        #creating widgets

        self.register_label=tk.Label(self.frame, text='\nVoulez vs avoir accès ?\n\n CREER UN COMPTE', bg='#333333', fg='white', font=('Bold',12))
        self.username_label=tk.Label(self.frame, text="nom de l'utilisateur", bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.username_entry=tk.Entry(self.frame, font=('Arial',16))
        self.password_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.password_label=tk.Label(self.frame, text='Mot de passe', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.confirm_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.confirm_label=tk.Label(self.frame, text='Confirmez', bg='#333333', fg='#FFFFFF',font=('Arial',12))

        self.email_label=tk.Label(self.frame, text='Email', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.email_entry=tk.Entry(self.frame, font=('Arial',16))

        self.phone_number_entry=tk.Entry(self.frame,font=('Arial',16))
        self.phone_number_label=tk.Label(self.frame, text='Téléphone ', bg='#333333', fg='#FFFFFF',font=('Arial',12))

        self.address_label=tk.Label(self.frame, text='Addresse', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.address_entry=tk.Entry(self.frame, font=('Arial',16))


        self.exit_button=tk.Button(self.frame, text='SE CONNECTER', bg='#FF3399', fg='white',command=Login)
        self.Login_button=tk.Button(self.frame, text="S'ENREGISTER", bg='#FF3399', fg='white', command=self.register)

        #Placing widgets on the screen
        
        self.register_label.grid(row=0, column=1, columnspan=1, padx=50)
      
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.password_label.grid(row=2, column=0)

        self.confirm_label.grid(row=3, column=0)
        self.confirm_entry.grid(row=3, column=1, pady=20)
        self.email_label.grid(row=4, column=0)
        self.email_entry.grid(row=4, column=1, pady=20)
        self.phone_number_label.grid(row=5, column=0)
        self.phone_number_entry.grid(row=5, column=1, pady=20)
        self.address_label.grid(row=6, column=0)
        self.address_entry.grid(row=6, column=1, pady=20)

        self.exit_button.grid(row=7, column=3, columnspan=1, padx= 10,pady=10)
        self.Login_button.grid(row=7, column=2, columnspan=1, padx= 1,pady=10)

        #packing a frame
        self.frame.pack()
        self.window.mainloop()

    #creating a register command
    def register(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CREDENTIALS",auth_plugin='mysql_native_password')
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()
        self.confirm=self.confirm_entry.get()
        self.email=self.email_entry.get()
        self.phone_number=self.phone_number_entry.get()
        self.address=self.address_entry.get()
        self.cursor=db.cursor()
        while(True):
            if (self.confirm!=self.password):
                messagebox.showinfo(title='Invalid', message='ces mots de passe sont différents !\n')  
                break
            if not (self.username_entry.get()):
                messagebox.showinfo(title='Identification', message='completer le nom')
                break
            if not (self.password_entry.get()):
                messagebox.showinfo(title='Password', message='Completer le mot de passe')
                break
            if not (self.confirm_entry.get()):
                messagebox.showinfo(title='Password', message='confirmez le mot de passe')
                break
            else:
                self.insert ="insert into USERS(USERNAME,PASSWORD,EMAIL,PHONE_NUMBER,Address) VALUES(%s,%s,%s,%s,%s)"
                self.UserInput=(self.username,self.password,self.email,self.phone_number,self.address)
                self.cursor.execute(self.insert,self.UserInput)
                db.commit()
                messagebox.showinfo(title='Enregistré', message='Vs vennez de créer un compte\nAllez vs connecter!')
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0 ,END)
                self.email_entry.delete(0, END)
                self.phone_number_entry.delete(0, END)
                self.address_entry.delete(0, END)
                self.window.destroy()
                Login()
                break    
       
#####configurations######
class Facture():
    global l 
    l=[]
    def __init__(self):
        #root configurations
        self.root=Tk()
        self.root.title("INVENTORY MANAGEMENT SYSTEM")
        self.root.geometry("1200x700")

        ###### Global Variables ########
        self.c_name=StringVar() 
        self.c_phone=StringVar() 
        self.bill_no=StringVar()
        self.x =random.randint(100, 9999)
        self.bill_no.set('DIM-'+str(self.x)+'-23')
        self.item=StringVar()
        self.prix_unit=IntVar()
        self.date_=StringVar()
        self.quantity=IntVar()
        self.file=('')

                #######Top section#########
        self.title=Label(self.root,text='DIMADO BILLING SOFTWARE', bg='#333333', fg='lightgreen', font=('Times new romman', 20,'bold'), bd='15', relief=GROOVE) # Relief plays a role in 3-D 
        self.title.pack(fill=X)
        ########customer's details ##########
        self.frame_1=LabelFrame(self.root, text="Information de l'acheteur",font=("Times new romman",11,'bold'), relief=GROOVE, bg='#333333', fg='#999999')
        self.frame_1.place(x=0, y=80, relwidth=1)

        self.name_label=Label(self.frame_1, text='Identité ',bg='#333333',fg='white', font=('Times new romman', 13,'bold'))
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry=Entry(self.frame_1, width=25, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.c_name)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label=Label(self.frame_1, text='Télephone',bg='#333333',fg='white', font=('Times new romman', 13,'bold'))
        self.phone_label.grid(row=0, column=3, padx=10, pady=5)
        self.phone=Entry(self.frame_1, width=13, font=('Arial 15 bold'), relief=SUNKEN,textvariable=self.c_phone)
        self.phone.grid(row=0, column=4, padx=10, pady=5)

        ### products details ####
        self.frame_2=LabelFrame(self.root, text="Marchandise ",font=("Times new romman",15,'bold'), relief=GROOVE, bg='#333333', fg='#999999')
        self.frame_2.place(x=19, y=170, width=627, height=500)

        self.item_label=Label(self.frame_2, text='Nom du produit ',fg='lightgreen',bg='#333333',font=('Times new romman', 13,'bold'), bd='15')
        self.item_label.grid(row=0, column=0, padx=20, pady=5)

        self.item_Entry=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.item)
        self.item_Entry.grid(row=0, column=1, padx=2,pady=5)

        self.qty=Label(self.frame_2, text='Quantité ',fg='lightgreen',bg='#333333',font=('Times new romman', 13,'bold'), bd='15')
        self.qty.grid(row=1, column=0, padx=10, pady=5)

        self.qty_Entry=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN,textvariable=self.quantity)
        self.qty_Entry.grid(row=1, column=1, padx=2,pady=5)

        self.unit=Label(self.frame_2, text='Prix Unitaire',fg='lightgreen',bg='#333333',font=('Times new romman', 13,'bold'), bd='15')
        self.unit.grid(row=2, column=0, padx=10, pady=5)

        self.unit_entry=Entry(self.frame_2, width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.prix_unit)
        self.unit_entry.grid(row=2, column=1, padx=10, pady=5)

        self.date=Label(self.frame_2, text="Date de l'Achat ",fg='lightgreen',bg='#333333',font=('Times new romman', 13,'bold'), bd='15')
        self.date.grid(row=4, column=0, padx=10, pady=5)

        self.date_Entry=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.date_)
        self.date_Entry.grid(row=4, column=1, padx=2,pady=5)

        ####### buttons ########

        self.btn1=Button(self.frame_2, text='AJOUTER',font=('Arial 12 bold'), padx=5, pady=5, bg='grey', width=15, command=self.ajouter)
        self.btn1.grid(row=5, column=0,padx=10, pady=20 )

        self.btn2=Button(self.frame_2, text='CREER FACTURE',font=('Arial 12 bold'), padx=5, pady=5, bg='grey',width=15, command=self.generate)
        self.btn2.grid(row=5, column=1,padx=10, pady=20)

        self.btn3=Button(self.frame_2, text='RECOMMENCER',font=('Arial 12 bold'), padx=5, pady=5, bg='grey',width=15, command=self.effacer)
        self.btn3.grid(row=6, column=0,padx=10, pady=20 )

        self.btn4=Button(self.frame_2, text='QUITTER',font=('Arial 12 bold'), padx=5, pady=5, bg='grey',width=15, command=self.quitter)
        self.btn4.grid(row=6, column=1,padx=10, pady=20 )
        self.save=Button(self.frame_1, text='ENREGISTRER', font=('Arial 12 bold'), padx=20, pady=5, bg='grey',width=15, command=self.savebill)
        self.save.grid(row=0,column=5,padx=10, pady=20)

        self.print=Button(self.frame_1,text='IMPRIMER', font=('Arial 12 bold'), padx=20, pady=5, bg='grey',width=15, command=self.print_hardcopy)    
        self.print.grid(row=0,column=6,padx=10, pady=20)

        self.report=Button(self.frame_1,text='REPORT',font=('Arial 12 bold'), padx=20, pady=5, bg='grey',width=15, command=Display)
        self.report.grid(row=0, column=7,padx=10,pady=20)

        self.moi=Label(self.frame_2,text='Developped by @Destin RIZIKI BULAMBO Phone: +250786144128 all rights reserved',fg='white',bg='#333333',font=('Times new romman', 6,'bold'), bd='1')
        self.moi.grid(row=10,column=1,padx=0,pady=50)

        ######## Bill Area ##########

        self.frame_3=Frame(self.root, relief=GROOVE, bd=10)
        self.frame_3.place(x=800, y=180, width=500, height=500)

        self.bill_title=Label(self.frame_3, text='Facturier', bg='grey',font=('Arial 15 bold'), relief=GROOVE, bd=9)
        self.bill_title.pack(fill=X)
        self.scroll_y=Scrollbar(self.frame_3, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.Textarea=Text(self.frame_3, yscrollcommand=self.scroll_y.set)
        self.Textarea.pack()
        self.scroll_y.config(command=self.Textarea.yview) 
        self.text()
        self.root.mainloop()

####### functions  ########

    def text(self):
        self.Textarea.delete(1.0, END)
        self.Textarea.insert(END, f"\tMAGASIN DIMADO FEU ROUGE")
        self.Textarea.insert(END, f"\n\t\t\t\tFacture no : {self.bill_no.get()}")        
        self.Textarea.insert(END, f'\n\t\t\t\tDate : \t{self.date_.get()}')
        self.Textarea.insert(END, f"\n___________________________________________________\n")
        self.Textarea.insert(END, f"\nNom de l'acheteur: Mr/Mme\t{self.c_name.get()}")
        self.Textarea.insert(END, f"\nNuméro de téléphone:\t{self.c_phone.get()}")
        self.Textarea.insert(END, f"\n___________________________________________________")
        self.Textarea.insert(END, f"\n\tMarchandise\t\tQuantité\t\tPrix\n\n")
        self.Textarea.config(font=("Arial 11 bold"))
    def ajouter(self):
        self.n=self.prix_unit.get()
        self.total=self.quantity.get()*self.n    
        sum_=+(self.total)
        l.append(sum_) 
        if self.item_Entry.get()=="":
            messagebox.showerror('error', 'Veillez Completer le nom du produit')
            self.text()
        elif self.unit_entry.get()=="":
            self.text()
            messagebox.showerror('error', 'Veillez le prix unitaire')
        else:
            self.savetodb()
            self.Textarea.insert(END,f"\t{self.item.get()}\t\t{self.quantity.get()}\t\t{self.total}$\n")
            

    def generate(self):
        self.space=self.Textarea.get(10.0,(10.0+(float(len(str(l))))))
        self.text()
        if not self.date_Entry.get():
            messagebox.showerror('error', 'Veillez completer la date ')
        if not self.name_entry.get():
            messagebox.showerror("error", "Veillez completer le nom de l'acheteur")           
        self.Textarea.insert(END, self.space)
        self.Textarea.insert(END,f'\n\n\t\t\tTotal net à payer : \t\t{sum(l)}$')
        self.Textarea.insert(END,f'\n___________________________________________________\n')   
        l.clear() 
    def savebill(self):
        self.op=messagebox.askyesno('save bill','Voulez-vous enregistrer la facture')
        if self.op> 0:
            self.bill_details=self.Textarea.get(1.0, END)
            self.file=filedialog.asksaveasfile(filetypes=[("Word Document",".txt"),
                                                           ("PDF Document",".pdf"),
                                                           ("Word Document",".txt")],
                                                            defaultextension='.docx',
                                                             initialdir="//home//destin//Documents",mode='a')                                                     
            try:
                self.file.write(self.bill_details)  
                self.file.flush() # to help me keep adding invoices as much as i wish
                messagebox.showinfo('Saved',f'Facture no {self.bill_no.get()} a été enregistré avec succès')
                self.effacer()                                        
            except:
                messagebox.showerror('Erreur',"la facture n'est pas enregistré !!!")
                                 

    def effacer(self):
        self.c_name.set('')
        self.c_phone.set('')
        self.date_.set('')
        self.item.set('')
        self.prix_unit.set(0)
        self.quantity.set(0)

        self.text() 
    def quitter(self):
        self.op=messagebox.askyesno('Quitter','Voulez-vs quitter')
        if self.op>0:
            self.root.destroy()
        else:
            pass

    def savetodb(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CREDENTIALS",auth_plugin='mysql_native_password')
        self.unit=self.prix_unit.get()
        self.tot=self.quantity.get()*self.unit
        self.dates=self.date_Entry.get()
        self.customer=self.name_entry.get()
        self.product=self.item_Entry.get()
        self.quantites=self.qty_Entry.get()
        self.total=self.tot
        phone_number=self.phone.get()
        self.cursor=db.cursor()
        self.inserts="INSERT INTO REPORT(DATES,CUSTOMER_NAMES,MARCHANDISES,QUANTITES,PRIX_UNITAIRE,PRIX_TOTAL,PHONE_NUMBERS) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        self.inputs=(self.dates,self.customer,self.product,self.quantites,self.unit,self.total,phone_number)
        self.cursor.execute(self.inserts,self.inputs)
        db.commit()

    def print_hardcopy(self):
        # Get the contents of the textarea
        self.print_text=self.Textarea.get('1.0', 'end')
        
        # Check if there is any text to print
        if len(self.print_text.strip()) == 0:
            messagebox.showwarning("No Text to Print", "There is no text to print!")
            return
        
        # Open a print dialog box to select the printer
        self.printer_file = filedialog.askopenfilename(title="Selectionnez le Format ", filetypes=[("Printer Files", "*.*"), ("All Files","*.prn" )])
        if self.printer_file == '':
            return
        
        # Send the text to the printer
        try:
            with open(self.printer_file, 'w') as printer:
                printer.write(self.print_text)
            messagebox.showinfo("Print Success", "The text was sent to the printer successfully!")
        except Exception as e:
            messagebox.showerror("Print Error", f"There was an error printing the text:\n{e}")

class Display():
    def __init__(self):
        #configuration part
        self.root =Tk()
        self.root.geometry('1000x650')
        self.root.title('')
        self.root.configure(bg="lightblue")
        self.tree=ttk.Treeview(self.root)
        self.tree.configure(height=30)

        #the scrollbar
        self.vscroll=ttk.Scrollbar(self.root, orient=VERTICAL)
        self.vscroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vscroll.set)
        self.vscroll.pack(fill=Y, side=RIGHT)

        self.tree['show']='headings'
        self.theme=ttk.Style()
        self.theme.theme_use('alt')
        self.theme.configure(".",font=("Arial",12,'bold'))
        self.theme.configure("Treeview.Heading", foreground="lightblue",background="#333333",font=("Arial",12,'bold') )

        #let me define number of columns :
        self.tree["columns"]=("ID","DATES","CUSTOMER_NAMES","MARCHANDISES","QUANTITES","PRIX_UNITAIRE","PRIX_TOTAL","PHONE_NUMBERS")
        self.tree.column("ID",width=100, minwidth=100, anchor=CENTER)
        self.tree.column("DATES",width=100, minwidth=100, anchor=CENTER)
        self.tree.column("CUSTOMER_NAMES",width=100, minwidth=100, anchor=CENTER)
        self.tree.column("MARCHANDISES",width=150, minwidth=100, anchor=CENTER)
        self.tree.column("QUANTITES",width=100, minwidth=100, anchor=CENTER)
        self.tree.column("PRIX_UNITAIRE",width=150, minwidth=100, anchor=CENTER)
        self.tree.column("PRIX_TOTAL",width=150, minwidth=100, anchor=CENTER)
        self.tree.column("PHONE_NUMBERS",width=110, minwidth=100, anchor=CENTER)

        #Next i'll give the head names the names of the columns
        self.tree.heading("ID",text='ID', anchor=CENTER)
        self.tree.heading("DATES",text='DATES', anchor=CENTER)
        self.tree.heading("CUSTOMER_NAMES",text='ACHETEURS', anchor=CENTER)
        self.tree.heading("MARCHANDISES",text='MARCHANDISE', anchor=CENTER)
        self.tree.heading("QUANTITES",text='QUANTITES', anchor=CENTER)
        self.tree.heading("PRIX_UNITAIRE",text='PRIX UNITAIRE', anchor=CENTER)
        self.tree.heading("PRIX_TOTAL",text='PRIX_TOTAL', anchor=CENTER)
        self.tree.heading("PHONE_NUMBERS",text='TELEPHONE', anchor=CENTER)
        
        self.buttonframe=Frame(self.root,bg='lightblue', width=20, height=10)

        self.searchframe=LabelFrame(self.root,text="Cherchez sur base de la date",bg='lightblue')
        self.searchframe.pack()

        self.entry = Entry(self.searchframe, width=30)
        self.entry.pack()

        self.chercher=Button(self.searchframe,text='RECHERCHER', command=self.SEARCH)
        self.chercher.config(font=("calibri",12,"bold"), bg="lightblue", fg="tomato", width=9, height=1)
        self.chercher.pack()
        #Let me now create buttons for some additional CRUD operations 

        self.buttonframe.pack(side=BOTTOM, fill="x")

        self.effacer=Button(self.buttonframe,text='EFFACER', command=self.EFFACER)
        self.effacer.config(font=("calibri",12,"bold"), bg="tomato", fg="white", width=15, height=1)
        self.effacer.pack(fill="y")

        # let me now pull data from the database :
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CREDENTIALS",auth_plugin='mysql_native_password')
        self.cursor=db.cursor()
        self.cursor.execute("select * from REPORT")

        i=0
        for row in self.cursor:
            self.tree.insert("",i, text="", values=(row[0],row[1],row[2],row[3],row[4],str(row[5])+"$",str(row[6])+"$",row[7]))
            i=i+1
        self.tree.pack()        
        self.root.mainloop() 

    def EFFACER(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CREDENTIALS",auth_plugin='mysql_native_password')
        self.del_cursor=db.cursor()
        self.selection = self.tree.selection()
        for item in self.selection:
            self.record_id = self.tree.item(item, "values")[0]
        try:
            self.query=("DELETE FROM REPORT WHERE ID =%s")

            # Execute SQL DELETE command
            self.value = (self.record_id,)
            self.del_cursor.execute(self.query, self.value)
            db.commit()
            # Remove selected record from tree
            self.tree.delete(item)
        except:
            messagebox.showerror('Erreur',"une erreur s'est produit !!!")

    def SEARCH(self):
        # Get the search query from the Entry widget
        self.query = self.entry.get()
        
        # Construct a SQL query to search for the item
        self.sql = "SELECT * FROM REPORT WHERE DATES LIKE %s"
        self.val = ("%" + self.query + "%", )
        
        # Execute the SQL query and fetch the result set
        self.cursor.execute(self.sql, self.val)
        self.results = self.cursor.fetchall()
        
        # Clear the Treeview widget and display the search results
        self.tree.delete(*self.tree.get_children())
        i=0
        for row in self.results:
            self.tree.insert("",i, text="", values=(row[0],row[1],row[2],row[3],row[4],str(row[5])+"$",str(row[6])+"$",row[7]))
            i=i+1
    
#Registration()
#Display()
#Facture()
Login()