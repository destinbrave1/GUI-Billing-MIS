from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import random
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
        self.save=Button(self.frame_1, text='ENREGISTRER', font=('Arial 12 bold'), padx=20, pady=5, bg='grey',width=20, command=self.savebill)
        self.save.grid(row=0,column=5,padx=50, pady=20)

        self.print=Button(self.frame_1,text='IMPRIMER', font=('Arial 12 bold'), padx=20, pady=5, bg='grey',width=15, command=self.print_hardcopy)    
        self.print.grid(row=0,column=6,padx=10, pady=20)
        
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
        
Facture()

