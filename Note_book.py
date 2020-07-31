from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Note_book")
root.geometry("500x500+50+50")
root.resizable(0,0)
#saving document
def save1():
     root2=Tk()
     root2.geometry("200x200+50+50")
     #entry bar for name of the file to be saved
     entry1=Entry(root2)
     entry1.pack()
    
     def save2():
          #saves the document to the same directory 
          file1=open(entry1.get(),"a")
          file1.writelines(frame1.get("1.0","end"))
          file1.close()
          label2=Label(root2,text="saved")
          label2.pack()
          
     btn3=Button(root2,text="Save",command=save2)
     btn3.pack()
     root2.mainloop()
#opening saved documents  
def open1():
      root1=Tk()
      root1.geometry("500x500+50+50")
      #creating entry bar for file_name to search
      entry_open=Entry(root1)
      entry_open.pack()
      root1.title(entry_open.get())
     
      def open2():
           file2=open(entry_open.get(),"r")
           readable=file2.readlines()
           file2.close()
           for i in readable:
               label1=Label(root1,text=str(i),padx=0,pady=0)
               label1.pack()
               label1.configure(justify=LEFT,background='white')
      btn4=Button(root1,text="open",command=open2)
      btn4.pack()
      root1.mainloop()
#exiting the window
def exit1():
     root3=Tk()
     root3.geometry("100x100+10+10")
     root3.title("Exit")
     def exit2():
          root.destroy()
          root3.destroy()
     def noexit():
          root3.destroy()
     btn5=Button(root3,text="No",command=noexit)
     btn5.pack()
     btn6=Button(root3,text="Yes",command=exit2)
     btn6.pack()
     root3.mainloop()
#creating menu bar   
menu_bar=Menu(root)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Save",command=save1)
file_menu.add_command(label="Open",command=open1)
file_menu.add_command(label="Exit",command=exit1)
menu_bar.add_cascade(label="File",menu=file_menu)
root.config(menu=menu_bar)
frame1=Text(root)
frame1.pack()
frame1.configure(font="arial")
root.mainloop()