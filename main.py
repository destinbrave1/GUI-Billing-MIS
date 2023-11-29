from datetime import datetime
import datetime as dt
from tkinter import ttk
from tkinter import messagebox
import subprocess
import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from datetime import datetime 
from dateutil.relativedelta import relativedelta

invoice_number = 1                               
maximum =101

class CHUKAS():
    global l                                  
    l=[]
    def __init__(self):
        #root configurations
        self.root=Tk()
        self.root.title("STOCK MANAGEMENT SYSTEM")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg="#BCC6CC")
        self.root.resizable(False, True)
        ###### Global Variables ########
        self.c_name=StringVar() 
        self.c_phone=StringVar()     
        self.bill_no=StringVar()
        self.item=StringVar()
        self.prix_unit=DoubleVar()
        self.date_=dt.datetime.now()
        self.quantity=IntVar()
        self.Codeqr=StringVar()
        self.file=('')
                #######Top section#########          
        self.title=Label(self.root,text="SYSTEM DE GESTION DE STOCK ", bg='#BCC6CC', fg='black', font=('Times new romman', 20,'bold'), bd='15', relief=RIDGE) # Relief plays a role in 3-D 
        self.title.pack(fill=X)
        ########customer's details ##########
        self.frame_1=LabelFrame(self.root, text="Information de l'acheteur",font=("Times new romman",11,'bold'), relief=GROOVE, bg='#999999', fg='black')
        self.frame_1.pack(fill=X, padx=10, pady=10, anchor='n')

        self.name_label=Label(self.frame_1, text='Identité ',bg='#999999',fg='#333333', font=('Times new romman', 13,'bold'))
        self.name_label.grid(row=0, column=0, padx=10, pady=5,sticky="e")
        self.name_entry=Entry(self.frame_1, width=25, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.c_name)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label=Label(self.frame_1, text='Télephone',bg='#999999',fg='#333333', font=('Times new romman', 13,'bold'))
        self.phone_label.grid(row=0, column=3, padx=10, pady=5,sticky="e")
        self.phone=Entry(self.frame_1, width=13, font=('Arial 15 bold'), relief=SUNKEN,textvariable=self.c_phone)
        self.phone.grid(row=0, column=4, padx=10, pady=5)

        self.calculator=Button(self.frame_1, text='CALCULATRICE',bg="lightgrey", fg="#333333", font=('Times new romman', 12,'bold'),relief=RAISED,bd=7,width=10, command=self.Calculatrice)
        self.calculator.grid(row=0, column=6, padx=250, pady=5)

        ### products details ####
        self.frame_2=LabelFrame(self.root, text="Marchandise ",font=("Times new romman",13,'bold'), relief=FLAT, bg='#999999', fg='#333333')
        self.frame_2.place(x=50, y=183, width=627, height=400)

        self.item_label=Label(self.frame_2, text='Nom du produit ',fg='white',bg='#999999',font=('Times new romman', 13,'bold'), bd='15')
        self.item_label.grid(row=0, column=0, padx=20, pady=5)

        self.item_Entry=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.item)
        self.item_Entry.grid(row=0, column=1, padx=2,pady=5)

        self.MarchandCode=Label(self.frame_2, text='Code QR ',fg='white',bg='#999999',font=('Times new romman', 13,'bold'), bd='15')
        self.MarchandCode.grid(row=1, column=0, padx=20, pady=5)

        self.MarchandCode=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.Codeqr)
        self.MarchandCode.grid(row=1, column=1, padx=2,pady=5)

        self.qty=Label(self.frame_2, text='Quantité ',fg='white',bg='#999999',font=('Times new romman', 13,'bold'), bd='15')
        self.qty.grid(row=2, column=0, padx=10, pady=5)

        self.qty_Entry=Entry(self.frame_2,width=20, font=('Arial 15 bold'), relief=SUNKEN,textvariable=self.quantity)
        self.qty_Entry.grid(row=2, column=1, padx=2,pady=5)

        self.unit=Label(self.frame_2, text='Prix Unitaire',fg='white',bg='#999999',font=('Times new romman', 13,'bold'), bd='15')
        self.unit.grid(row=3, column=0, padx=10, pady=5)

        self.unit_entry=Entry(self.frame_2, width=20, font=('Arial 15 bold'), relief=SUNKEN, textvariable=self.prix_unit)
        self.unit_entry.grid(row=3, column=1, padx=10, pady=5)

        ####### buttons ########

        self.btn1=Button(self.frame_2, text='RECOMMENCER',font=('Times New Roman',12,'bold'), padx=5, pady=5, bg="lightgrey", fg="black", width=16,relief=RIDGE,bd=7,command=self.effacer)
        self.btn1.grid(row=5, column=0,padx=10, pady=20 )

        self.btn2=Button(self.frame_2, text='STOCK-OUT',font=('Arial 12 bold'), padx=5, pady=5, bg="lightgrey", fg="black",width=14,relief=RIDGE,bd=7, command=self.ajouter)
        self.btn2.grid(row=5, column=1,padx=10, pady=20)

        self.opentext = tk.Text(self.root)

        self.moi=Label(self.frame_2,text='copyright juin 2023 all rights reserved. App owner- email: destinbrave1@gmail.com',fg='lightgrey',bg='#999999',font=('Times new romman', 6,'bold'), bd='1')
        self.moi.grid(row=9,column=1,padx=5,pady=20)
        ######## Bill Area ##########
        self.frame_3=Frame(self.root, relief=GROOVE, bd=10)
        self.frame_3.place(x=800, y=180, width=490, height=490)

        self.bill_title=Label(self.frame_3, text='Facturier', bg='lightgrey',font=('Arial 15 bold'), relief=GROOVE, bd=9)
        self.bill_title.pack(fill=X)
        self.btn2=Button(self.frame_3, text='FACTURE NET',font=('Arial 10 bold'), padx=5, pady=5, bg="lightgrey", fg="black",width=14,relief=RIDGE,bd=7, command=self.generate)
        self.btn2.pack(side=BOTTOM)

        self.scroll_y=Scrollbar(self.frame_3, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.Textarea=Text(self.frame_3, yscrollcommand=self.scroll_y.set)
        self.Textarea.pack()
        self.scroll_y.config(command=self.Textarea.yview) 
        self.text()
        ##### creation of a menu #####
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        ######### Menu################
        self.actionmenu = tk.Menu(menu, tearoff=False)
        self.actionmenu.configure(relief=tk.FLAT,border=3, borderwidth=20)
        
        self.gestion = tk.Menu(menu, tearoff=False)
        self.gestion.configure(relief=tk.FLAT,border=3, borderwidth=20)

        self.adminmenu = tk.Menu(menu, tearoff=False)
        self.adminmenu.configure(relief=tk.FLAT, borderwidth=20)
                                               
        self.helpmenu = tk.Menu(menu, tearoff=False)
        self.helpmenu.configure(relief=tk.FLAT, borderwidth=18)

        self.poubelle = tk.Menu(menu, tearoff=False)
        self.poubelle.configure(relief=tk.FLAT, borderwidth=18)
        
        self.poubelle = tk.Menu(menu, tearoff=False)
        self.poubelle.configure(relief=tk.FLAT, borderwidth=18)

        menu.add_cascade(label="Admin",font="Arial 14",menu=self.adminmenu)

        self.adminmenu.add_command(label="Ajouter un admin  ",font="Arial 12", command=self.Admin)
        self.adminmenu.add_separator()
        self.adminmenu.add_command(label="se deconnecter",font="Arial 12", command=self.logout)
        
        menu.add_cascade(label="factures",font="Arial 14",menu=self.actionmenu)

        self.actionmenu.add_command(label="Ouvrir -> facture ",font="Arial 12", command=self.View_file)
        self.actionmenu.add_separator()
    
        self.actionmenu.add_command(label="Enregistrer -> facture",font="Arial 12", command=self.savebill)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Imprimer -> facture",font="Arial 12", command=self.print_hardcopy)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Quitter",font="Arial 12", command=self.quitter)
        self.actionmenu.add_separator()

        menu.add_cascade(label="Inventaires",font="Arial 14",menu=self.gestion)
        self.gestion.add_command(label="Gestion ventes ", font="Arial 12",command=self.Display_Report)
        self.gestion.add_separator()
        self.gestion.add_command(label="Gestion Stock", font="Arial 12",command=self.Stock_movement)
        self.gestion.add_separator()
        self.gestion.add_command(label="Backup -> disk ",font="Arial 12", command=self.backup_local)
        self.gestion.add_separator()

        menu.add_cascade(label="Lis-moi",font="Arial 14",menu=self.helpmenu)
        
        self.helpmenu.add_command(label="read-me",font="Arial 12", command=self.functions)
        self.helpmenu.add_separator()
        

        self.root.mainloop()
    ####### functions  ########
    def backup_local(self):
        try:
            # Retrieve the MySQL connection details from the input fields
            self.username = "destin"
            self.password = "Destin378464."
            self.database_name = "FAMILLE"
            self.hostname = "localhost"
            # Prompt the user to select the flash disk to save the backup
            self.flashdisk_path = filedialog.askdirectory(title="Select Flash Disk")
            if self.flashdisk_path:
                # Generate the backup file name
                self.backup_file = f"{self.database_name}_backup.sql"

                # Execute the backup command using mysqldump
                self.command = f"mysqldump -u {self.username} -p{self.password} -h {self.hostname} {self.database_name} > '{self.flashdisk_path}/{self.backup_file}'"
                subprocess.call(self.command, shell=True)
                self.root = tk.Tk()
                self.root.title("MySQL Database Backup")
                self.root.geometry("400x250")
                # Create the result label
                self.result_label = tk.Label(self.root, text="")
                self.result_label.pack()
                self.result_label.config(text="Backup completed successfully!")
                self.root.mainloop()
            else:
                messagebox.showerror("Failed","Le backup a echoué")

        except KeyboardInterrupt:
            pass  # Do nothing if the process is interrupted by the user
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {str(e)}")
       

    def generate_invoice(self):
        global invoice_number
        if invoice_number <= maximum + 1:
            invoice_text = f" {str(invoice_number).zfill(3)}"
            self.bill_no.set(invoice_text)
            invoice_number += 1
            if invoice_number == maximum:
                invoice_number = 1
                self.generate_invoice()
   
    def text(self):
        self.Textarea.delete(1.0, END)
        self.Textarea.insert(END, f"VENTE DES APPAREILS ELECTRO-MENAGERS\nET DIVERS\nTel : +243844551940\n")
        self.Textarea.insert(END, f"\n\t\tFacture no : {self.bill_no.get()}")        
        self.Textarea.insert(END, f'\n\t\tBukavu, \t{self.date_}')
        self.Textarea.insert(END, f"\n________________________________________________________\n")
        self.Textarea.insert(END, f"\nMr/Mme : \t{self.c_name.get()}")
        self.Textarea.insert(END, f"\nTéléphone :\t{self.c_phone.get()}")
        self.Textarea.insert(END, f"\n_______________________________________________________")
        self.Textarea.insert(END, f"\nQuantité\t\tMarchandise\t\tPrix-unit\t\tPrix-tot\n\n")

    def ajouter(self):
        self.new_date=dt.datetime.now()  
        self.n=(self.prix_unit.get())
        self.total=(self.quantity.get()*self.n)
        sum_=+float(self.total)
        l.append(sum_) 
        if self.item_Entry.get()=="":
            messagebox.showerror('error', 'Veillez Completer le nom du produit')
            self.text()
            
        elif self.Codeqr.get()=="":
            messagebox.showerror('error', 'Veillez Completer le Code_Qr')
            self.text()
            
        elif self.unit_entry.get()=="":
            messagebox.showerror('error', 'ajoutez le prix unitaire')
            self.text()
        else:
            self.restes_stock, self.stock_out, self.total_stock =self.UpdateStock(self.Codeqr.get(),self.quantity.get())    
    
    def UpdateStock(self,code_qr, quantity):
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
                                    database="CHUSI", auth_plugin='mysql_native_password')
        cursor = db.cursor()
        # Retrieve the current RESTES, STOCK_OUT, and TOTAL_STOCK values from the database
        query = "SELECT RESTES, STOCK_OUT, STOCK_IN FROM STOCK WHERE CODE_QR = %s"
        values = (code_qr,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            current_restes = int(result[0])
            current_stock_out = int(result[1])
            total_stock = int(result[2])   

            # Perform calculation on RESTES and STOCK_OUT columns
            updated_restes = current_restes - quantity
            updated_stock_out = current_stock_out + quantity
            
            if updated_restes >= 0 and updated_stock_out <= total_stock:
                self.Textarea.insert(END,f"{self.quantity.get()}\t\t{self.item.get()}\t\t{'{:.2f}'.format(self.n)}\t\t{'{:.2f}'.format(self.total)}$\n")
                query = "UPDATE STOCK SET RESTES = %s, STOCK_OUT = %s WHERE CODE_QR = %s"
                values = (updated_restes, updated_stock_out, code_qr)
                cursor.execute(query, values)
                db.commit()
                self.vente_to_db()
                return updated_restes, updated_stock_out, total_stock 
            
            elif updated_restes == 0 and updated_stock_out == total_stock:
                self.c_name.set("")
                self.c_phone.set("")
                messagebox.showwarning("Empty stock","Cet article est déjà epouisé\nveillez informer l'acheteur")
                return None, None, None
                    
            else:
                self.c_name.set("")
                self.c_phone.set("")
                messagebox.showwarning("insuffisance","Insufissance de stock\nveillez informer l'acheteur")
                return None, None, None
        else:
            self.c_name.set("")
            self.c_phone.set("")
            messagebox.showerror("Code_Qr","code marchand incorrecte\nveillez reverifier le code")
            return None, None, None
          
        
    def generate(self):
        self.generate_invoice()
        self.space=self.Textarea.get(13.0,(13.0+(float(len(str(l))))))
        self.text()
        if not self.name_entry.get():
            messagebox.showerror("error", "Veillez completer le nom de l'acheteur")           
        self.Textarea.insert(END, self.space)
        self.Textarea.insert(END,f"\n\n\t\t\t\tTotal Net  : \t\t{'{:.2f}'.format(sum(l))}$")
        self.Textarea.insert(END,f'\n________________________________________________________\n')  
        l.clear() 

    def savebill(self):
        self.op=messagebox.askyesno('save bill','Voulez-vous enregistrer la facture')
        if self.op> 0:
            self.bill_details=self.Textarea.get(1.0, END)
            self.file=filedialog.asksaveasfile(filetypes=[("Word Document",".txt"),
                                                           ("PDF Document",".pdf"),
                                                           ("Word Document",".docx")],
                                                            defaultextension='.txt',
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
        self.date_ = dt.date.today()
        self.item.set('')
        self.prix_unit.set(0.0)
        self.quantity.set(0)
        self.Codeqr.set('')

        self.text() 
    def quitter(self):
        self.op=messagebox.askyesno('Quitter','Voulez-vs arrêter ce programme?')
        if self.op>0:
            self.root.destroy()
        else:
            pass

    def vente_to_db(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CHUSI",auth_plugin='mysql_native_password')
        self.unit=self.prix_unit.get()
        self.tot=self.quantity.get()*self.unit
        self.dates=dt.date.today()
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
    def functions(self):
        root=Tk()
        root.title("FONCTIONNEMENT")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        root.configure(bg="#BCC6CC")
        root.resizable(False, True)

        scroll_y=Scrollbar(root, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        Textarea=Text(root,width=100, height=150, yscrollcommand=scroll_y.set)
        Textarea.pack()
        scroll_y.config(command=Textarea.yview)

        Textarea.delete(1.0, END)
        Textarea.insert(END, f"\n\tHISTORIQUE\n\t----------\n")
        Textarea.insert(END, f"\nPour commencer,moi, BULAMBO RIZIKI DESTIN, Software engineer (ingénier en informatique)\nnous sommes le 1 juillet 2023. pour le moment je suis en vacance de summer à Bukavu,\nje profitais pour travailler sur un projet J'étais encore à Kigali le temps que j'avais\ncommencé ")
        Textarea.insert(END, f"à développer cette application en premier lieu,tout seul dans ma chambre,\nembrouillé avec l'Université, ayant beaucoups des assignments,c'était en Avril,je me disais toujours\nde revenir dans mon pays(la RDC)")
        Textarea.insert(END, f"pour pouvoir aider nos parents pour promouvoir un business efficace en utilisant un petit programme GUI (utilisant TKINTER) avec PYTHON et une base de données locale\nsans internet (qui est maintenant un produit finis), qui peut beaucoups mieux effectuer les inventaires régulièrement dans les magasins en tenant compte du mouvement de stocks specifiquement dans nos\nmagazins ")
        Textarea.insert(END, f"familiaux, ayant sous ses yeux les statistiques concernant les ventes, et la fréquence des marchandises les plus mouvementées dans le stock, pour ne pas avoir des décisions médiocres mais\nplutôt pour mieux avancer son business et éviter toute sorte de perte dans son stock.\n")
        Textarea.insert(END, f"C'est dans ce même ordre d'idée que j'avais commencé avec le projet, deux mois après, j'étais rentré\nau pays alors que mon grand frère MUSAMBYA MAKISANGA (Entrepreneur), qui, lui m'avait soutenu et m'a poussé de l'avant, de 350 lignes de codes à plus de 1300 lignes de codes, qui fut mon premier\nprojet avec toutes ses lignes de codes dans un seul fichier")
        Textarea.insert(END, f" Cependant MUSAMBYA MAKISANGA\n(Entrepreneur) m'a ajouté l'algorithme de STOCK-IN et STOCK-OUT tout en utilisant un code marchand\t (CODE QR) pour tenir compte de nombre d'articles restants dans le magazin et ceux-la vendus.\n")
        Textarea.insert(END, f"Premièrement je remercie mon Dieu qui a rendu ceci possible, de deux mon grand frère l'Entrepreneur MUSAMBYA MAKISANGA qui m'a poussé de l'avant en me procurant des challenges qui semblaient au début impossible à réaliser mais par après boum gloire à Dieu ç'a marché.\n")
        Textarea.insert(END, f"\n\tContributions\n\t---------------\n")
        Textarea.insert(END, f"\n->>> MUSAMBYA MAKISANGA (Entrepreneur) \n\t\t\t\taddresse email : musambyamakisanga94@gmail.com\n")
        Textarea.insert(END, f"\n->>> BULAMBO RIZIKI DESTIN(Software engineer)\n\t\t\t\taddresse email : destinbrave1@gmail.com\n")
        Textarea.insert(END, f"\n\n\t#Comment utiliser cette application\n\t ----------------------------------\n ")
        Textarea.insert(END, f"\n#Cet programme est Offline cad pas d'internet pour l'utilisation\n\nPrerequisites : \n ->> mysql database\n ->> Python \n\t#Bibliothèque: Tkinter \n")        
        Textarea.insert(END, "\n# En ajoutant quelque chôse sur la facture,critiquement ça influence le stock\ndonc avant de faire quoi que ce soit,rassurez vs que l'acheteur a completé son payement\n\t")
        Textarea.insert(END, f"\ncar vs avez la possibilité de tout observer surtout quand vs êtes considéré comme admin.\n#cet programme n'est pas public mais privé.\n")
        Textarea.insert(END, f"\nETAPES A SUIVRE POUR L'UTILISATION\n")
        Textarea.insert(END, f"\n1. FACTURIER\n------------\n")
        Textarea.insert(END, f"1. Ajouter les informations de l'acheteur\n")
        Textarea.insert(END, f"2. Ajouter les informations de la marchandise en ajoutant le code marchand de l'article\n")
        Textarea.insert(END, f"3. Commencer avec le bouton 'STOCK-OUT ' pour retirer du stock  autant d'article que l'acheteur veut acheter\t->>>Ne cliquez pas sur ce bouton si l'acheteur n'a pas encore payé\n\t ->>>s'il vient de payer, mentionnez 'STOCK-OUT'\n\t->>s'il a términé avec le payment : suivez la quatrième étape\n")
        Textarea.insert(END, f"4. Cliquer sur 'FACTURE NET' pour avoir le total general\n")
        Textarea.insert(END, f"5. Cliquer sur recommencer pour ajouter les nouvelles insformations du nouveau acheteur\n")
        Textarea.insert(END, f"\n2. GESTION DE STOCK (RESERVE A L'ADMIN)\n------------\n")
        Textarea.insert(END, f"\n->>Vs avez la possibilité d'observer le mouvement de stock quand vs avez accès\nà la base de donnée en se connectant comme admin, sans internet mais en ayant comme admin \nen utilisant Mysql database.")
        Textarea.insert(END, f"\n1. Vs pouvez ajouter le nouveau stock dans le magazin.\n")
        Textarea.insert(END, f"\n2. Vs pouvez aussi effacer ce stock en cas d'erreur.\n")
        Textarea.insert(END, f"\n3. Vs pouvez vérifier la durée de stock dans le magazin en utilisation les boutons concernés.\n")
        Textarea.insert(END, f"\n\nBACKUP ->> disk\n------------\n")
        Textarea.insert(END, f"# Il s'agit de sauvegarder les données sur un port USB ou un disk dur pour éviter la perte \nde données si l'ordinateur est endomagé.\n")
        Textarea.insert(END, f"\nDETAILS VENTES\n--------\n")
        Textarea.insert(END, f"Il s'agit d'un tableau où tout ce qui est enregistré sur la facture, se présente comme achat du jour, etc\n")
        Textarea.insert(END, f"\nVs pouvez effacer aussi un element et observer toutes les ventes réalisées au courrant de l'année,\netc\n")
        Textarea.insert(END, f"\nENREGISTER \n--------\nOUVRIR\n--------\nIMPRIMER\n----------")
        Textarea.insert(END, f"\n->>La facture peut être enregistrê, l'imprimer et l'ouvir pour vêrification\n")
        Textarea.insert(END, f"\nAJOUTER ADMIN\n")
        Textarea.insert(END, f"\n->>l'actuel utilisateur peut aussi ajouter un nouveau utilisateur comme admin\ncar cette application est privée\n")
        Textarea.insert(END, f"\nSE DECONNECTER\n")
        Textarea.insert(END, f"\n->>Pour éviter de se faire arnaqué dans son business, il est conseillé de se déconnecter\nen cas de deplacement au lieu de fermer la session.\n")
        root.mainloop()

    def Display_Report(self):
        Ventes()
    def View_file(self):
        File()
    def logout(self):
        self.root.destroy()
        Login()
    def Calculatrice(self):
        Calculator()
  
    def Stock_movement(self):
        DisplayStock()
    def Admin(self):
        AjouterAdmin()
  
class Login:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.configure(bg='black') # bg stands for background, and fg stands for for ground

        #create a frame (to help make our GUI more responsive
        self.frame=tk.LabelFrame(self.window, text=' se connecter',bg='#333333',fg='white', width=15, height=10, font=("Times new romman",13,'bold'), relief=GROOVE)
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
       
        self.register_button.grid(row=7, column=3, columnspan=1, padx= 10,pady=10)
        self.Login_button.grid(row=7, column=2, columnspan=1, padx= 1,pady=10)

        #packing a frame
        self.frame.pack(padx=150, pady=100)
        self.window.mainloop()
                
    #function to fetch data from database     
    def login(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CHUSI",auth_plugin='mysql_native_password')
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()     
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
         
            elif not self.result2:
                messagebox.showerror(title='password!', message='Invalid Password')
                break        
            
            else:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)
                self.window.destroy()
                CHUKAS()
                break
class AjouterAdmin:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.configure(bg='black') # bg stands for background, and fg stands for for ground

        #create a frame (to help make our GUI more responsive
        self.frame=tk.LabelFrame(self.window, text=' se connecter',bg='#333333',fg='white', width=15, height=10, font=("Times new romman",13,'bold'), relief=GROOVE)
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
       
        self.register_button.grid(row=7, column=3, columnspan=1, padx= 10,pady=10)
        self.Login_button.grid(row=7, column=2, columnspan=1, padx= 1,pady=10)

        #packing a frame
        self.frame.pack(padx=150, pady=100)
        self.window.mainloop()
                
    #function to fetch data from database     
    def login(self):
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CHUSI",auth_plugin='mysql_native_password')
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()
       
             
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
         
            elif not self.result2:
                messagebox.showerror(title='password!', message='Invalid Password')
                break        
            
            else:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)
                self.window.destroy()
                Registration()
                break

class Registration():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
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
        db =mysql.connector.connect(host="localhost",user ="destin",password= "Destin378464.",database ="CHUSI",auth_plugin='mysql_native_password')
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
                self.window.destroy()
                messagebox.showinfo(title='Enregistré', message='Vs vennez de créer un compte\nBienvenue nouveau')
                break    

class Ventes():
    def __init__(self):
        # Configuration part
        self.root = Tk()
        self.root.geometry('1200x700')
        self.root.minsize(600, 400) # Set minimum size for the root window
        self.root.title('TOUTES LES VENTES REALISEES')
        self.root.configure(bg="#BCC6CC")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

        self.tree = ttk.Treeview(self.root)
        self.tree.configure(height=30)
        # The scrollbar
        self.vscroll = ttk.Scrollbar(self.root, orient=VERTICAL)
        self.vscroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vscroll.set)
        self.vscroll.grid(row=4, column=8, sticky=N+S)
        self.tree['show'] = 'headings'
        self.theme = ttk.Style()
        self.theme.theme_use('alt')
        self.theme.configure(".", font=("Arial", 12, 'bold'))
        self.theme.configure("Treeview.Heading", foreground="#BCC6CC", background="#333333",
        font=("Arial", 12, 'bold'))
        # Let me define number of columns:
        self.tree["columns"] = ("ID", "DATES", "CUSTOMER_NAMES", "MARCHANDISES",
        "QUANTITES", "PRIX_UNITAIRE", "PRIX_TOTAL", "PHONE_NUMBERS")
        self.tree.column("ID", width=10, minwidth=100, anchor=CENTER)
        self.tree.column("DATES", width=150, minwidth=100, anchor=CENTER)
        self.tree.column("CUSTOMER_NAMES", width=150, minwidth=100, anchor=CENTER)
        self.tree.column("MARCHANDISES", width=150, minwidth=100, anchor=CENTER)
        self.tree.column("QUANTITES", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("PRIX_UNITAIRE", width=150, minwidth=100, anchor=CENTER)
        self.tree.column("PRIX_TOTAL", width=150, minwidth=100, anchor=CENTER)
        self.tree.column("PHONE_NUMBERS", width=110, minwidth=100, anchor=CENTER)
        # Next, give the headings the names of the columns
        self.tree.heading("ID", text='ID', anchor=CENTER)
        self.tree.heading("DATES", text='DATES', anchor=CENTER)
        self.tree.heading("CUSTOMER_NAMES", text='ACHETEURS', anchor=CENTER)
        self.tree.heading("MARCHANDISES", text='MARCHANDISE', anchor=CENTER)
        self.tree.heading("QUANTITES", text='QUANTITES', anchor=CENTER)
        self.tree.heading("PRIX_UNITAIRE", text='PRIX UNITAIRE', anchor=CENTER)
        self.tree.heading("PRIX_TOTAL", text='PRIX_TOTAL', anchor=CENTER)
        self.tree.heading("PHONE_NUMBERS", text='TELEPHONE', anchor=CENTER)
        self.searchframe = LabelFrame(self.root, text="Recherchez un element", bg='#BCC6CC')
        self.searchframe.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")
        self.today = Button(self.searchframe, text="Aujourd'hui", bg="tomato", fg="white",
        height="2", font=("Arial 9"), command=self.handle_day)
        self.today.grid(row=0, column=1, padx=2, pady=1)

        self.hier = Button(self.searchframe, text="hier", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_hier)
        self.hier.grid(row=0, column=2, padx=2, pady=1)
        self.moins_3 = Button(self.searchframe, text="<= 3 jours", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_3days)
        self.moins_3.grid(row=0, column=3, padx=1, pady=1)
        self.week = Button(self.searchframe, text="<= semaine", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_week)
        self.week.grid(row=0, column=4, padx=1, pady=1)
        self.mois = Button(self.searchframe, text="<= mois", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_month)
        self.mois.grid(row=0, column=5, padx=1, pady=1)
        self.trimestre = Button(self.searchframe, text="<= trimestre", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_trimestre)
        self.trimestre.grid(row=0, column=6, padx=1, pady=1)

        self.semestre = Button(self.searchframe, text="<= semestre", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_semestre)
        self.semestre.grid(row=0, column=7, padx=1, pady=1)

        self.annuel = Button(self.searchframe, text="<= Annuel", bg="black", fg="lightblue",
        font=("Arial 9"), command=self.handle_annuel)
        self.annuel.grid(row=0, column=8, padx=1, pady=1)

        self.MorethanYear = Button(self.searchframe, text="Année +>>", bg="black", fg="lightblue",
        font=("Arial 9"), command=None)
        self.MorethanYear.grid(row=0, column=9, padx=1, pady=1)

        self.entry = Entry(self.searchframe, width=30)
        self.entry.grid(row=1, column=0, columnspan=7, padx=5, pady=5)
        self.chercher = Button(self.searchframe, text='RECHERCHER', command=self.SEARCH)
        self.chercher.config(font=("calibri", 12, "bold"), bg="#BCC6CC", fg="tomato", width=11, height=1)
        self.chercher.grid(row=2, column=0, columnspan=8, padx=5, pady=5)
        # Additional CRUD operations buttons
        self.buttonframe = Frame(self.root, bg='#BCC6CC', width=20, height=10)
        self.buttonframe.grid(row=3, column=0, columnspan=8, pady=10)
        self.effacer = Button(self.buttonframe, text='EFFACER', command=self.EFFACER)
        self.effacer.config(font=("calibri", 12, "bold"), bg="tomato", fg="white", width=15, height=1)
        self.effacer.pack(fill="y")
        # Pull data from the database
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
        database="CHUSI", auth_plugin='mysql_native_password')
        self.cursor = db.cursor()
        self.cursor.execute("SELECT * FROM REPORT")
        i = 0
        for row in self.cursor:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4],
            str(row[5]) + "$", str(row[6]) + "$", row[7]))
            i += 1

        self.tree.grid(row=4, column=0, columnspan=8, padx=20, pady=10, sticky="nsew")
        ttk.Sizegrip(self.root).grid(row=5, column=8, sticky="se") # Add Sizegrip widget for resizing
        self.root.mainloop()

    def EFFACER(self):
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
        database="CHUSI", auth_plugin='mysql_native_password')
        self.del_cursor = db.cursor()
        self.selection = self.tree.selection()
        for item in self.selection:
            self.record_id = self.tree.item(item, "values")[0]
            try:
                self.query = ("DELETE FROM REPORT WHERE ID =%s")
                # Execute SQL DELETE command
                self.value = (self.record_id,)
                self.del_cursor.execute(self.query, self.value)
                db.commit()
                self.tree.delete(item)
            except:
                messagebox.showerror('Erreur', "une erreur s'est produit !!!")


    def SEARCH(self):
        # Get the search query from the Entry widget
        query = self.entry.get()
        try:
            db = mysql.connector.connect(
            host="localhost",
            user="destin",
            password="Destin378464.",
            database="CHUSI",
            auth_plugin='mysql_native_password'
            )
            cursor = db.cursor()
            # Construct a SQL query to search for the item
            sql = "SELECT * FROM REPORT WHERE DATES LIKE %s"
            val = ("%" + query + "%",)
            # Execute the SQL query and fetch the result set
            cursor.execute(sql, val)
            results = cursor.fetchall()
            # Clear the Treeview widget and display the search results
            self.tree.delete(*self.tree.get_children())
            for row in results:
                self.tree.insert("", "end", values=row)
            cursor.close()
            db.close()
        except mysql.connector.Error as error:
            messagebox.showerror('Erreur', f"Une erreur s'est produite lors de la recherche : {error}")

    def SEARCH(self):
        # Get the search query from the Entry widget
        query = self.entry.get()

        # Construct a SQL query to search for the item
        sql = "SELECT * FROM REPORT WHERE DATES LIKE %s OR CUSTOMER_NAMES LIKE %s OR MARCHANDISES LIKE %s"
        val = ("%" + query + "%", "%" + query + "%", "%" + query + "%")

        # Execute the SQL query and fetch the result set
        self.cursor.execute(sql, val)
        results = self.cursor.fetchall()

        # Clear the Treeview widget and display the search results
        self.tree.delete(*self.tree.get_children())
        i = 0
        for row in results:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], str(row[4]) + "$", row[5], row[6], row[7]))
            i += 1

    def handle_day(self):
        # Calculate the start and end dates for the day interval
        start_date = dt.date.today()
        end_date = dt.date.today()

        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_3days(self):
        # Calculate the start and end dates for the interval
        end_date = dt.date.today()
        start_date = end_date - dt.timedelta(days=2)

        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_hier(self):
        # Calculate the start and end dates for the interval
        end_date = dt.date.today() - dt.timedelta(days=1)
        start_date = end_date 

        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_week(self):
        # Calculate the start and end dates for the week interval
        start_date = dt.date.today() - dt.timedelta(weeks=1)
        end_date = dt.date.today()
        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_month(self):
        start_date = dt.date.today() - relativedelta(months=1)
        end_date = dt.date.today()
        self.fetch_items_within_interval(start_date, end_date)
    def handle_trimestre(self):
        start_date = (datetime.now() - relativedelta(months=3)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_semestre(self):
        start_date = (datetime.now() - relativedelta(months=6)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_annuel(self):
        start_date = (datetime.now() - relativedelta(years=1)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_more_than_year(self):
        start_date = (datetime.now() - relativedelta(years=2)).date()
        self.fetch_items_within_interval(start_date, None)

    def fetch_items_within_interval(self,start_date, end_date):
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
                                    database="CHUSI", auth_plugin='mysql_native_password')
        cursor = db.cursor()
        # Construct the SQL query to fetch items within the interval
        if end_date:
            query = "SELECT * FROM REPORT WHERE DATES BETWEEN %s AND %s"
            values = (start_date, end_date)
        else:
            query = "SELECT * FROM REPORT WHERE DATES <= %s"
            values = (start_date,)

        cursor.execute(query, values)
        results = cursor.fetchall()
        
        self.tree.delete(*self.tree.get_children())
        i = 0
        for row in results:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], str(row[4])+"$", row[5], row[6], row[7]))
            i = i + 1

class DisplayStock:
    def __init__(self):
        # configuration part
        self.root = Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.title('STOCKS ENTRES')
        self.root.configure(bg="#BCC6CC")
        self.tree = ttk.Treeview(self.root)
        self.tree.configure(height=30)

        self.buttonframe = Frame(self.root, bg='#BCC6CC', width=20, height=10)
        self.buttonframe.pack(side=BOTTOM, fill="x")
        
        self.vscroll = ttk.Scrollbar(self.root, orient=VERTICAL)
        self.vscroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vscroll.set)
        self.vscroll.pack(fill=Y, side=RIGHT)

        self.xscroll = ttk.Scrollbar(self.root, orient=HORIZONTAL)
        self.xscroll.configure(command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.xscroll.set)
        self.xscroll.pack(fill=X, side=BOTTOM)

        self.tree['show'] = 'headings'
        self.theme = ttk.Style()
        self.theme.theme_use('alt')
        self.theme.configure(".", font=("Arial", 12, 'bold'))
        self.theme.configure("Treeview.Heading", foreground="#BCC6CC", background="#333333",
                             font=("Arial", 12, 'bold'))

        # let me define number of columns:
        self.tree["columns"] = ("ID", "DATES", "CODE_QR", "PRODUCT_NAME","PRIX_UNITAIRE", "STOCK_IN","STOCK_OUT","RESTES")
        self.tree.column("ID", width=50, minwidth=100, anchor=CENTER)
        self.tree.column("DATES", width=160, minwidth=100, anchor=CENTER)
        self.tree.column("CODE_QR", width=170, minwidth=100, anchor=CENTER)
        self.tree.column("PRODUCT_NAME", width=300, minwidth=200, anchor=CENTER)
        self.tree.column("PRIX_UNITAIRE", width=170, minwidth=100, anchor=CENTER)
        self.tree.column("STOCK_IN", width=170, minwidth=100, anchor=CENTER)
        self.tree.column("STOCK_OUT", width=170, minwidth=100, anchor=CENTER)
        self.tree.column("RESTES", width=170, minwidth=100, anchor=CENTER)

        # Next i'll give the head names the names of the columns
        self.tree.heading("ID", text='ID', anchor=CENTER)
        self.tree.heading("DATES", text="DATE D'ENTREE->>", anchor=CENTER)
        self.tree.heading("CODE_QR", text='CODE_QR', anchor=CENTER)
        self.tree.heading("PRODUCT_NAME", text='MARCHANDISE', anchor=CENTER)
        self.tree.heading("PRIX_UNITAIRE", text='PRIX UNITAIRE', anchor=CENTER)
        self.tree.heading("STOCK_IN", text='STOCK IN', anchor=CENTER)
        self.tree.heading("STOCK_OUT", text='STOCK OUT', anchor=CENTER)
        self.tree.heading("RESTES", text='RESTE STOCK', anchor=CENTER)

        self.buttonframe = Frame(self.root, bg='#BCC6CC', width=20, height=10)

        self.searchframe = LabelFrame(self.root, text="Recherchez un element", bg='#BCC6CC')
        self.searchframe.pack(fill="x", padx=10, pady=10, expand=True)
        self.searchframe.config(width=600) 
        
        self.week = Button(self.searchframe, text="Semaine", bg="black", fg="lightblue", font=("Arial 9"), command=self.handle_week)
        self.week.pack(side="left", padx=1, pady=1)

        self.month = Button(self.searchframe, text="Mois", bg="black", fg="lightblue", font=("Arial 9"), command=self.handle_month)
        self.month.pack(side="left", padx=1, pady=1)

        self.trimestre = Button(self.searchframe, text="<<- trimestre", bg="black", fg="lightblue",
                        font=("Arial 9"), command=self.handle_trimestre)
        self.trimestre.pack(side="left", padx=1, pady=1)

        self.semestre = Button(self.searchframe, text="<<- semestre", bg="black", fg="lightblue",
                            font=("Arial 9"), command=self.handle_semestre)
        self.semestre.pack(side="left", padx=1, pady=1)

        self.annuel = Button(self.searchframe, text="<<- Année", bg="black", fg="lightblue",
                            font=("Arial 9"), command=self.handle_annuel)
        self.annuel.pack(side="left", padx=1, pady=1)

        self.MoreThanYear = Button(self.searchframe, text="Année +>>", bg="black", fg="lightblue",
                                font=("Arial 9"), command=self.handle_more_than_year)
        self.MoreThanYear.pack(side="left", padx=1, pady=1)

        self.entry = Entry(self.searchframe, width=30)
        self.entry.pack(side="left", padx=1, pady=1)

        self.chercher = Button(self.searchframe, text='RECHERCHER', command=self.SEARCH)
        self.chercher.config(font=("calibri", 12, "bold"), bg="#BCC6CC", fg="tomato", width=11, height=1)
        self.chercher.pack(side="left", padx=1, pady=1)
        self.buttonframe.pack(side=BOTTOM, fill="x")

        self.add_button = Button(self.buttonframe, text='NOUVEAU STOCK', command=self.open_add_data_window)
        self.add_button.config(font=("calibri", 10, "bold"), bg="BLACK", fg="lightblue", width=15, height=1)
        self.add_button.pack(side="left", padx=1, pady=1)

        self.effacer = Button(self.buttonframe, text='EFFACER', command=self.EFFACER)
        self.effacer.config(font=("calibri", 10, "bold"), bg="tomato", fg="white", width=15, height=1)
        self.effacer.pack(side="left", padx=1, pady=1)

        self.budget = Button(self.buttonframe, text='BUDGET STOCK', command=self.calculate_budget)
        self.budget.config(font=("calibri", 10, "bold"), bg="#333333", fg="tomato", width=15, height=1)
        self.budget.pack(side="right", padx=1, pady=1)

        # let me now pull data from the database:
        self.db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
                                     database="CHUSI", auth_plugin='mysql_native_password')
        self.cursor = self.db.cursor()
        self.cursor.execute("select * from STOCK")

        i = 0
        for row in self.cursor:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3],str(row[4])+"$", row[5], row[6], row[7]))
            i = i + 1
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        self.root.mainloop()

    def calculate_budget(self):
        cursor = self.db.cursor()
        query = "SELECT SUM(STOCK_IN * PRIX_UNITAIRE) FROM STOCK"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        self.display_result(str(result) + "$")

    def display_result(self, result):
        budget_window = tk.Toplevel(self.root)
        budget_window.title("Budget")
        budget_window.geometry("400x100")
        budget_window.configure(bg="#333333")
        label_budget = tk.Label(budget_window, text="\nStock courant estimé à " + str(result), bg='#333333', fg='tomato', font=("Arial black ",15))
        label_budget.pack(fill=Y)
    def open_add_data_window(self):
        # Create a new window for adding data
        self.add_window = Toplevel(self.root)
        self.add_window.title("Ajouter des données")
        self.add_window.geometry("400x200")

        # Create entry labels and fields
        code_qr_label = Label(self.add_window, text="Code QR:")
        code_qr_label.pack()
        code_qr_entry = Entry(self.add_window, width=30)
        code_qr_entry.pack()

        product_name_label = Label(self.add_window, text="Nom du produit:")
        product_name_label.pack()
        product_name_entry = Entry(self.add_window, width=30)
        product_name_entry.pack()

        prix_unitaire_label = Label(self.add_window, text="Prix unitaire:")
        prix_unitaire_label.pack()
        prix_unitaire_entry = Entry(self.add_window, width=30)
        prix_unitaire_entry.pack()

        stock_in_label = Label(self.add_window, text="Stock in:")
        stock_in_label.pack()
        stock_in_entry = Entry(self.add_window, width=30)
        stock_in_entry.pack()

        # Create button to add data
        add_data_button = Button(self.add_window, text="Ajouter", command=lambda: self.add_data(code_qr_entry.get(), product_name_entry.get(), float(prix_unitaire_entry.get()), int(stock_in_entry.get())))
        add_data_button.pack()

    def add_data(self, code_qr, product_name, prix_unitaire, stock_in):
        # Check if the code_qr already exists in the STOCK table
        query = "SELECT * FROM STOCK WHERE CODE_QR = %s"
        values = (code_qr,)
        self.cursor.execute(query, values)
        existing_stock = self.cursor.fetchone()

        if existing_stock:
            # Code QR already exists, ask user if they want to add to the existing stock
            add_existing_stock = messagebox.askyesno('Stock existant', 'Le code QR existe déjà. Voulez-vous ajouter à la quantité existante ?')
            if add_existing_stock:
                # User wants to add to existing stock
                existing_stock_in = existing_stock[5]
                new_stock_in = existing_stock_in + stock_in

                existing_restes_stock = int(existing_stock[7])  # Convert existing_restes_stock to an integer
                new_restes_stock = existing_restes_stock + stock_in

                update_query = "UPDATE STOCK SET STOCK_IN = %s, RESTES = %s, PRODUCT_NAME = %s, PRIX_UNITAIRE = %s WHERE CODE_QR = %s"
                update_values = (new_stock_in, new_restes_stock, product_name, prix_unitaire, code_qr)
                self.cursor.execute(update_query, update_values)

                self.db.commit()

                messagebox.showinfo('Succès', 'Données mises à jour avec succès.')
            else:
                # User wants to change the code_qr and insert a new data
                messagebox.showinfo('Changement de code QR', 'Veuillez changer le code QR pour insérer de nouvelles données.')
        else:
            # Code QR doesn't exist, insert a new record
            restes = stock_in
            stock_out = 0
            current_datetime = datetime.now()
            insert_query = "INSERT INTO STOCK (DATES, CODE_QR, PRODUCT_NAME, PRIX_UNITAIRE, STOCK_IN, STOCK_OUT, RESTES) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_values = (current_datetime, code_qr, product_name, prix_unitaire, stock_in, stock_out, restes)

            try:
                self.cursor.execute(insert_query, insert_values)
                self.db.commit()
                messagebox.showinfo('Succès', 'Données ajoutées avec succès.')
                self.add_window.destroy()
                self.display_existing_data()
            except Exception as e:
                messagebox.showerror('Erreur', 'Une erreur s\'est produite lors de l\'ajout des données:\n' + str(e))
        
    def EFFACER(self):
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
                                     database="CHUSI", auth_plugin='mysql_native_password')
        self.del_cursor = db.cursor()
        self.selection = self.tree.selection()

        for item in self.selection:
            self.record_id = self.tree.item(item, "values")[0]
        try:
            self.query = ("DELETE FROM STOCK WHERE ID =%s")
            # Execute SQL DELETE command
            self.value = (self.record_id,)
            self.del_cursor.execute(self.query, self.value)
            db.commit()
            self.tree.delete(item)
        except:
            messagebox.showerror('Erreur', "une erreur s'est produit !!!")

    def SEARCH(self):
        # Get the search query from the Entry widget
        query = self.entry.get()
        
        # Construct a SQL query to search for the item
        sql = "SELECT * FROM STOCK WHERE DATES LIKE %s OR CODE_QR LIKE %s OR PRODUCT_NAME LIKE %s"
        val = ("%" + query + "%", "%" + query + "%", "%" + query + "%")

        # Execute the SQL query and fetch the result set
        self.cursor.execute(sql, val)
        results = self.cursor.fetchall()

        # Clear the Treeview widget and display the search results
        self.tree.delete(*self.tree.get_children())
        i = 0
        for row in results:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], str(row[4]) + "$", row[5], row[6], row[7]))
            i += 1
    def display_existing_data(self):
        # Clear the Treeview widget
        self.tree.delete(*self.tree.get_children())

        # Fetch data from the database
        self.cursor.execute("SELECT * FROM STOCK")
        rows = self.cursor.fetchall()

        # Insert fetched data into the Treeview widget
        for row in rows:
            self.tree.insert("", "end", values=row)

    def handle_day(self):
        # Calculate the start and end dates for the day interval
        start_date = dt.date.today()
        end_date = dt.date.today()

        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_week(self):
        # Calculate the start and end dates for the week interval
        start_date = dt.date.today() - dt.timedelta(weeks=1)
        end_date = dt.date.today()

        # Call the function to fetch items within the interval
        self.fetch_items_within_interval(start_date, end_date)

    def handle_month(self):
        start_date = dt.date.today() - relativedelta(months=1)
        end_date = dt.date.today()
        self.fetch_items_within_interval(start_date, end_date)
    def handle_trimestre(self):
        start_date = (datetime.now() - relativedelta(months=3)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_semestre(self):
        start_date = (datetime.now() - relativedelta(months=6)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_annuel(self):
        start_date = (datetime.now() - relativedelta(years=1)).date()
        end_date = datetime.now().date()
        self.fetch_items_within_interval(start_date, end_date)

    def handle_more_than_year(self):
        start_date = (datetime.now() - relativedelta(years=2)).date()
        self.fetch_items_within_interval(start_date, None)

    def fetch_items_within_interval(self,start_date, end_date):
        db = mysql.connector.connect(host="localhost", user="destin", password="Destin378464.",
                                    database="CHUSI", auth_plugin='mysql_native_password')
        cursor = db.cursor()

        # Construct the SQL query to fetch items within the interval
        if end_date:
            query = "SELECT * FROM STOCK WHERE DATES BETWEEN %s AND %s"
            values = (start_date, end_date)
        else:
            query = "SELECT * FROM STOCK WHERE DATES <= %s"
            values = (start_date,)

        cursor.execute(query, values)
        results = cursor.fetchall()
        
        self.tree.delete(*self.tree.get_children())
        i = 0
        for row in results:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], str(row[4])+"$", row[5], row[6], row[7]))
            i = i + 1
            
class Calculator:
    def __init__(self):      
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.display = tk.Entry(self.root, width=25, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        # Create number buttons
        for i in range(1, 10):
            self.btn = tk.Button(self.root, text=str(i), width=5, font=("Arial", 14),
                            command=lambda num=i: self.btn_click(num))
            self.btn.grid(row=(9 - i) // 3 + 1, column=(i - 1) % 3)
            
        # Create zero button
        self.btn_zero = tk.Button(self.root, text="0", width=5, font=("Arial", 14),
                            command=lambda: self.btn_click(0))
        self.btn_zero.grid(row=4, column=0)

        # Create operator buttons
        self.operators = ['+', '-', '*', '/']
        self.row = 1
        self.col = 3
        for operator in self.operators:
            btn_operator = tk.Button(self.root, text=operator, width=5, font=("Arial", 14),
                                    command=lambda op=operator: self.btn_click(op))
            btn_operator.grid(row=self.row, column=self.col)
            self.row += 1

        # Create equal button
        self.btn_equal = tk.Button(self.root, text="=", width=12, font=("Arial", 14),
                            command=self.btn_equal)
        self.btn_equal.grid(row=4, column=1, columnspan=2)

        # Create clear button
        self.btn_clear = tk.Button(self.root, text="Clear", width=12, font=("Arial", 14),
                            command=self.btn_clear)
        self.btn_clear.grid(row=5, column=1, columnspan=2)

        self.root.mainloop()

    def btn_click(self,number):
        self.current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current + str(number))

    def btn_clear(self):
        self.display.delete(0, tk.END)

    def btn_equal(self):
        try:
            self.expression = self.display.get()
            self.result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

class File():
    def __init__(self):
        self.content = ""  # Initialize the content attribute
        self.filepath = ""
        self.open_file()

        if self.filepath:
            self.root = tk.Tk()
            self.root.geometry("1000x650")
            self.root.title("Facture enregistrée")
            self.root.configure(bg="#BCC6CC")

            self.scroll_y = Scrollbar(self.root, orient=VERTICAL, bg="white", relief=GROOVE, bd=2)
            self.scroll_y.pack(side=RIGHT, fill=Y)

            self.opentext = tk.Text(self.root, width="60", height="34", yscrollcommand=self.scroll_y.set)

            self.scroll_y.config(command=self.opentext.yview)

            self.opentext.delete("1.0", tk.END)
            self.opentext.insert(tk.END, self.content)
            self.opentext.pack()

            self.root.mainloop()

    def open_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        try:
            if self.filepath:
                with open(self.filepath, "r") as file:
                    self.content = file.read()
        except KeyboardInterrupt:
            pass  # Do nothing if the process is interrupted by the user
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "No document found.")
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {str(e)}")
CHUKAS()

