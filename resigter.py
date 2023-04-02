from tkinter import messagebox
import tkinter as tk
import mysql.connector
class Registration:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("DESTIN")
        self.window.geometry('800x620')
        self.window.configure(bg='#333333') # bg stands for background, and fg stands for for ground

        #create a frame (to help make our GUI more responsive
        self.frame=tk.Frame(self.window,bg='#333333', width=15, height=10)
        #creating widgets

        self.register_label=tk.Label(self.frame, text='\nAre you new ?\n\nCREATE ACCOUNT', bg='#333333', fg='white', font=('Bold',12))
        self.username_label=tk.Label(self.frame, text='Username', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.username_entry=tk.Entry(self.frame, font=('Arial',16))
        self.password_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.password_label=tk.Label(self.frame, text='Password', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.confirm_entry=tk.Entry(self.frame, show='*',font=('Arial',16))
        self.confirm_label=tk.Label(self.frame, text='Confirm', bg='#333333', fg='#FFFFFF',font=('Arial',12))

        self.email_label=tk.Label(self.frame, text='Email', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.email_entry=tk.Entry(self.frame, font=('Arial',16))

        self.phone_number_entry=tk.Entry(self.frame,font=('Arial',16))
        self.phone_number_label=tk.Label(self.frame, text='Phone ', bg='#333333', fg='#FFFFFF',font=('Arial',12))

        self.address_label=tk.Label(self.frame, text='Address', bg='#333333', fg='#FFFFFF',font=('Arial',12))
        self.address_entry=tk.Entry(self.frame, font=('Arial',16))


        self.exit_button=tk.Button(self.frame, text='Exit', bg='#FF3399', fg='white',command=self.window.destroy)
        self.Login_button=tk.Button(self.frame, text='Register', bg='#FF3399', fg='white', command=self.register)

        #Placing widgets on the screen
        
        self.register_label.grid(row=0, column=0, columnspan=1, sticky='news', padx=15)
      
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
        db =mysql.connector.connect(host="localhost",username ="destin",password= "Destin378464.",database ="CREDENTIALS")
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()
        self.confirm=self.confirm_entry.get()
        self.email=self.email_entry.get()
        self.phone_number=self.phone_number_entry.get()
        self.address=self.address_entry.get()
        self.cursor=db.cursor()
        while(True):
            if (self.confirm!=self.password):
                messagebox.showinfo(title='Invalid', message='Passwords do not match')  
                break
            if not (self.username_entry.get()):
                messagebox.showinfo(title='Identification', message='Enter your username')
                break
            if not (self.password_entry.get()):
                messagebox.showinfo(title='Password', message='Enter your password')
                break
            if not (self.confirm_entry.get()):
                messagebox.showinfo(title='Password', message='Confirm your password')
                break
            else:
                self.insert ="insert into INVENTORY(USERNAME,PASSWORD,EMAIL,PHONE_NUMBER,Address) VALUES(%s,%s,%s,%s,%s)"
                self.UserInput=(self.username,self.password,self.email,self.phone_number,self.address)
                self.cursor.execute(self.insert,self.UserInput)
                messagebox.showinfo(title='Registered', message='You are registered successfully\nPlease Login')
                db.commit()
                break   
Registration()