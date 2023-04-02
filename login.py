from tkinter import messagebox
import tkinter as tk
from tkinter import *
import mysql.connector
import random
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
        self.register_button=tk.Button(self.frame, text='Exit', bg='#ff0000', fg='white',command=self.window.destroy)

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

            if not self.result2:
                messagebox.showerror(title='password!', message='Invalid Password')
                break        
               
            elif (self.confirm!=self.password):
                messagebox.showerror(title='Invalid', message='Passwords do not match')  
                break
            
            elif not (self.username_entry.get()):
                messagebox.showerror(title='Identification', message='Enter your username')
                break
            elif not (self.password_entry.get()):
                messagebox.showerror(title='Password', message='Enter your password')
                break
            elif not (self.confirm_entry.get()):
                messagebox.showerror(title='Password', message='Confirm your password')
                break
            else:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)
                self.window.destroy()
                #Facture()
                break
                
                  
Login()
