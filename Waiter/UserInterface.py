#!/usr/bin/python3

from Tkinter import *
import ttk
import tkMessageBox as messagebox
import Waiter
import time

class App:

    def __init__(self, master):
        global Master
        Master = master
        master.title(" Central Steakhouse ")
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        self.bttn_clicks1 = 0
        self.bttn_clicks2 = 0
        self.bttn_clicks3 = 0

        self.bttn_clicks4 = 0
        self.bttn_clicks5 = 0
        self.bttn_clicks6 = 0


        self.style = ttk.Style()
        self.style.configure('TFrame', background='#E5A26E')
        self.style.configure('TButton', background='#E5A26E',  font=('Garamond', 15))
        self.style.configure('TLabel', background='#E5A26E', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack(side = LEFT, fill = 'both')

        self.logo = PhotoImage(file = 'dd.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row=0, column=0, padx=6,pady=12)
        ttk.Button(self.frame_header, text='DRINKS', command=self.drinks).grid(row=1, column=0, padx=6, pady=12)
        ttk.Button(self.frame_header, text='FOOD', command=self.food).grid(row=2, column=0, padx=6, pady=12)
        ttk.Button(self.frame_header, text='EXIT', command=self.exit).grid(row=3, column=0, padx=6, pady=12)
        ttk.Button(self.frame_header, text='PAY NOW', command=self.pay).grid(row=4, column=0, padx=6, pady=12)
        ttk.Label(self.frame_header, text = 'Table 10').grid(row = 5, column =0, padx=6,pady=12, sticky = NW)
        #ttk.Label(self.frame_header, text = 'Total:').grid(row = 6, column =0, padx=6,pady=12, sticky = W)
# **************************************** Frame 1 **************************************************************
        self.frame_image = ttk.Frame(master)
        self.frame_image.pack(side="right", fill="both")

        self.restimage = PhotoImage(file = 'spin-a-yarn.png')
        ttk.Label(self.frame_image, image = self.restimage).grid(row = 0 , column = 1, rowspan = 7)

# **************************************** Frame 2 **************************************************************
        self.frame_drinks = ttk.Frame(master)
        self.frame_drinks.pack(side="right", fill="both")

        ttk.Label(self.frame_drinks, text=' Drinks ').grid(row=0, column=1, sticky=W)
        self.style.configure('TLabel', font=('Garamond', 18, 'italic'), side='Center')

        self.buttn4 = ttk.Button(self.frame_drinks, text='d_item1', command=self.d_item1).grid(row=1, column=0, padx=12,
                                                                                               pady=25)
        self.entry4 = ttk.Entry(self.frame_drinks, text="entry1")
        self.entry4.grid(row=1, column=1, padx=12, pady=25, columnspan=1)
        self.add4 = ttk.Button(self.frame_drinks, text='+', command=self.f_quant1)
        self.add4.grid(row=1, column=2, padx=12, pady=25)

        self.buttn5 = ttk.Button(self.frame_drinks, text='d_item2', command=self.d_item2).grid(row=3, column=0, padx=12,
                                                                                               pady=25)
        self.entry5 = ttk.Entry(self.frame_drinks, text="entry2")
        self.entry5.grid(row=3, column=1, padx=12, pady=25, columnspan=1)
        self.add5 = ttk.Button(self.frame_drinks, text='+', command=self.f_quant2)
        self.add5.grid(row=3, column=2, padx=12, pady=25)

        self.buttn6 = ttk.Button(self.frame_drinks, text='d_item3', compound=CENTER, command=self.d_item3).grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=12,
                                                                                                                pady=25)
        self.entry6 = ttk.Entry(self.frame_drinks, text="entry3")
        self.entry6.grid(row=5, column=1, padx=12, pady=25, columnspan=1)
        self.add6 = ttk.Button(self.frame_drinks, text='+', command=self.f_quant3)
        self.add6.grid(row=5, column=2, padx=12, pady=25)
        # data = (self.bttn_clicks1,,self.bttn_clicks2,self.spicy,self.bttn_clicks3)
        ttk.Button(self.frame_drinks, text='Order Now', command=self.submit_order).grid(row=6, column=1, padx=12,
                                                                                        pady=25)
# **************************************** Frame 3 **************************************************************
        self.frame_food = ttk.Frame(master)
        self.frame_food.pack(side = "right",fill = "both")

        ttk.Label(self.frame_food, text = ' Food ').grid(row = 0 , column = 1, sticky = W)
        self.style.configure('TLabel', font=('Garamond',18, 'italic'),side = 'Center')

        self.buttn1 = ttk.Button(self.frame_food, text='f_item1', command=self.d_item1).grid(row=1, column=0, padx=12, pady=25)
        self.e1 = ttk.Entry(self.frame_food,text = "entry1")
        self.e1.grid(row = 1, column = 1, padx =12, pady=25, columnspan = 1)
        self.add1 = ttk.Button(self.frame_food, text='+', command = self.d_quant1)
        self.add1.grid(row=1, column=2, padx=12, pady=25)

        self.v = IntVar()
        self.v.set(2)
        Radiobutton(self.frame_food, text="Rare", variable= self.v, value=1).grid(row = 2, column  = 0)
        Radiobutton(self.frame_food, text="Medium", variable=self.v, value=2).grid(row = 2, column = 1)
        Radiobutton(self.frame_food, text="Well Done", variable=self.v, value=3).grid(row = 2, column = 2)
        # self.cook = v

        self.buttn2 = ttk.Button(self.frame_food, text='f_item2', command=self.d_item2).grid(row=3, column=0, padx=12, pady=25)
        self.entry2 = ttk.Entry(self.frame_food, text="entry2")
        self.entry2.grid(row=3, column=1, padx=12, pady=25, columnspan = 1)
        self.add2 = ttk.Button(self.frame_food, text='+', command=self.d_quant2)
        self.add2.grid(row=3, column=2, padx=12, pady=25)

        self.k = IntVar()
        self.k.set(2)
        Radiobutton(self.frame_food, text="Mild", variable=self.k, value=1).grid(row=4, column=0)
        Radiobutton(self.frame_food, text="Medium", variable=self.k, value=2).grid(row=4, column=1)
        Radiobutton(self.frame_food, text="Hot", variable=self.k, value=3).grid(row=4, column=2)
        # self.cook = self.k.get()
        # print("%s" %(self.k.get()))

        self.buttn3 = ttk.Button(self.frame_food, text='f_item3', compound= CENTER, command=self.d_item3).grid(row=5, column=0, padx=12, pady=25)
        self.entry3 = ttk.Entry(self.frame_food, text="entry3")
        self.entry3.grid(row=5, column=1, padx=12, pady=25, columnspan = 1)
        self.add3 = ttk.Button(self.frame_food, text='+', command=self.d_quant3)
        self.add3.grid(row=5, column=2, padx=12, pady=25)
        # data = (self.bttn_clicks1,,self.bttn_clicks2,self.spicy,self.bttn_clicks3)
        ttk.Button(self.frame_food, text='Order Now', command=self.submit_order).grid(row=6, column=1, padx=12, pady=25)



    def drinks(self):

        self.frame_image.destroy()
	self.frame_food.destroy()
        # self.frame_food.show()
        # self.frame_image.grid.forget()
        # self.frame_food = ttk.Frame(master)
        # self.frame_food.pack(side = "right",fill = "both")
        # self.restimage = PhotoImage(file = 'spin-a-yarn.png')
        # ttk.Label(self.frame_header, image = self.restimage).grid(row = 0 , column = 1, rowspan = 7)
        print('drinks')

    def food(self):
        # self.frame_food.pack_forget()
        self.frame_image.destroy()
        self.frame_drinks.destroy()
        print('food')

    def exit(self):
	global Master
        Master.destroy()
        Waiter.closeAndExit()

    def pay(self):
        print('pay')
	#messagebox.showinfo(title = 'Central Steakhouse', message = 'Successfully paid!')

    def d_item1(self):
        print('d_item1:')

    def d_item2(self):
        print('d_item2:')

    def d_item3(self):
        print('d_item3:')

    def f_item1(self):
        print('f_item1:')

    def f_item2(self):
        print('f_item2:')

    def f_item3(self):
        print('f_item3:')

    def d_quant1(self):
        self.clear1()
        self.bttn_clicks1 += 1
        self.e1.insert("end", "%s" % (self.bttn_clicks1))
        return self.bttn_clicks1

    def d_quant2(self):
        self.clear2()
        self.bttn_clicks2 += 1
        self.entry2.insert("end", "%s" % (self.bttn_clicks2))
        return self.bttn_clicks2

    def d_quant3(self):
        self.clear3()
        self.bttn_clicks3 += 1
        self.entry3.insert("end", "%s" % (self.bttn_clicks3))
        return self.bttn_clicks3

    def f_quant1(self):
        self.clear4()
        self.bttn_clicks4 += 1
        self.entry4.insert("end", "%s" % (self.bttn_clicks4))
        return self.bttn_clicks4

    def f_quant2(self):
        self.clear5()
        self.bttn_clicks5 += 1
        self.entry5.insert("end", "%s" % (self.bttn_clicks5))
        return self.bttn_clicks5

    def f_quant3(self):
        self.clear6()
        self.bttn_clicks6 += 1
        self.entry6.insert("end", "%s" % (self.bttn_clicks6))
        return self.bttn_clicks6

    def clear1(self):
        self.e1.delete(0,'end')

    def clear2(self):
        self.entry2.delete(0, 'end')

    def clear3(self):
        self.entry3.delete(0, 'end')

    def clear4(self):
        self.entry4.delete(0, 'end')
    def clear5(self):
        self.entry5.delete(0, 'end')
    def clear6(self):
        self.entry6.delete(0, 'end')

    def submit_order(self):
        global Master
        data = (self.bttn_clicks1, self.v.get(),self.bttn_clicks2, self.k.get(), self.bttn_clicks3, self.bttn_clicks4, self.bttn_clicks5, self.bttn_clicks6)# tuple to send to DB
        # print("%s %s %s %s %s %s %s %s" % (self.bttn_clicks1, self.v.get(),self.bttn_clicks2, self.k.get(), self.bttn_clicks3,self.bttn_clicks4, self.bttn_clicks5, self.bttn_clicks6))
        Waiter.orderDetails(data)
        # order_data = (a,b,c,d,e) # tuple to send to DB
        #messagebox.showinfo(title='Order status', message='Your order has been placed!')
        self.frame_image.destroy()
        self.frame_drinks.destroy()
        self.frame_food.destroy()
	# master.destroy()

        self.frame_order = ttk.Frame(Master)
        self.frame_order.pack(side = "right",fill = "both")

	orderStr = Waiter.getOrderDetailsStr()
	
	self.a=ttk.Label(self.frame_order, text="%s"%(orderStr), font=("Helvetica",12))
	self.a.pack(side = "top", expand=True)

        self.bill = ttk.Button(self.frame_order, text="Generate Bill", command=self.bill_step)
        self.bill.pack(side = "bottom")

        #Waiter.waitForOrderComplete()

        #messagebox.showinfo(title='Order status', message='Your order is ready!')

    def bill_step(self):

        Waiter.sendBillRequest()

	billStr = Waiter.getBillDetailsStr()

        self.frame_order.destroy()

        self.frame_bill = ttk.Frame(Master)
        self.frame_bill.pack(side = "right",fill = "both")

	self.a=ttk.Label(self.frame_bill, text="%s"%(billStr), font=("Helvetica",12))
	self.a.pack(side = "top", expand=True)

	self.bill = ttk.Button(self.frame_bill, text="Close", command=newOrder)
        self.bill.pack()


def newOrder():
	global Master

	Master.destroy()

	startDisplay()


def startDisplay():

    root = Tk()
    feedback = App(root)
    root.geometry("720x540")
    root.mainloop()


