#!/usr/bin/python3

from Tkinter import *
import ttk
import tkMessageBox as messagebox
import Chef

class Kitchen:
    def __init__(self,master):
        global Master
        Master = master
        master.title(" Central Steakhouse Kitchen")
        master.resizable(False,False)
        master.configure(background = 'Black')

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(fill = "both")
	ttk.Label(self.frame_content, text = "   Table : 9   ").grid(row = 0, column = 0 , rowspan = 1)
        #self.exitbutton = ttk.Button(self.frame_content, text =' EXIT ', command = self.exitall).grid(row = 1, column = 0 , rowspan = 1)
        master.after(1000, self.timeoutHandle)

    def exitall(self):
        master.destroy()
	Chef.closeAndExit()

    def timeoutHandle(self):
        aux = Chef.waitForOrderDetails()
        if(aux.numItems > 0):
            s1 = aux.item_1.spiceLevel
            c1 = aux.item_1.cookLevel
            q1 = aux.item_1.quantity
            n1 = aux.item_1.name
            ttk.Label(self.frame_content, text = "   Table : 10   ").grid(row = 0, column = 0 , rowspan = 1)
            ttk.Label(self.frame_content, text="    Spice Level    ").grid(row=0, column=1, padx=20, pady=25, sticky=E)
            ttk.Label(self.frame_content, text="    Cook Level    ").grid(row=0, column=2, padx=20, pady=25, sticky=E)
            ttk.Label(self.frame_content, text="    Quantity   ").grid(row=0, column=3, padx=20, pady=25, sticky=E)
            #self.logo1 = PhotoImage(file='d_1.gif')
            ttk.Label(self.frame_content, text="%s"%(n1)).grid(row=1, column=0, padx=20, pady=25, sticky = W)
            ttk.Label(self.frame_content, text="%s"%(s1)).grid(row=1, column=1, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(c1)).grid(row=1, column=2, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(q1)).grid(row=1, column=3, padx=20, pady=25)
        if(aux.numItems>1):
            s2 = aux.item_2.spiceLevel
            c2 = aux.item_2.cookLevel
            q2 = aux.item_2.quantity
            n2 = aux.item_2.name
            #self.logo2 = PhotoImage(file='d_2.gif')
            ttk.Label(self.frame_content, text="%s"%(n2)).grid(row=2, column=0, padx=20, pady=25, sticky=W)
            ttk.Label(self.frame_content, text="%s"%(s2)).grid(row=2, column=1, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(c2)).grid(row=2, column=2, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(q2)).grid(row=2, column=3, padx=20, pady=25)
        if(aux.numItems>2):
            s3 = aux.item_3.spiceLevel
            c3 = aux.item_3.cookLevel
            q3 = aux.item_3.quantity
            n3 = aux.item_3.name
            #self.logo3 = PhotoImage(file='d_3.gif')
            ttk.Label(self.frame_content, text="%s"%(n3)).grid(row=3, column=0, padx=20, pady=25, sticky=W)
            ttk.Label(self.frame_content, text="%s"%(s3)).grid(row=3, column=1, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(c3)).grid(row=3, column=2, padx=20, pady=25)
            ttk.Label(self.frame_content, text="%s"%(q3)).grid(row=3, column=3, padx=20, pady=25)

        self.button = ttk.Button(self.frame_content, text =' DONE ', command = self.waittodestroy)
        self.button.grid(row = 4 , column = 1, columnspan = 2,rowspan = 1, sticky = EW)


    def waittodestroy(self):
        global Master
        Chef.sendOrderComplete()
        Chef.waitForBillRequest()
        Master.destroy()
        startDisplay()

def startDisplay():
    root = Tk()
    feedback = Kitchen(root)
    root.geometry("720x540")
    root.mainloop()

if __name__ == "__main__": startDisplay()
