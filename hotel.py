from tkinter import *;

from PIL import Image, ImageTk;
from customer import CustomerWindow;

class HotelManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Managment System")
        self.root.geometry("1550x800+0+0")

        #================= First Image ===========================
        img1 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd = 4, relief=RIDGE)
        lblimg.place(x =0, y = 0, width=1550, height=140)

        #=================  Hotel logo =========================

        img2 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=230, height=140)

        #======================Title ==============================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(("times new roman"), 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        #==================== main fram ===========================
        main_fram = Frame(self.root, bd=4, relief=RIDGE)
        main_fram.place(x=0, y=190, width=1550, height=620)

        #===================== menu ========================
        lbl_menu = Label(main_fram, text="Menu", font=(("times new roman"), 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ==================== button fram ===========================
        button_fram = Frame(main_fram, bd=4, relief=RIDGE)
        button_fram.place(x=0, y=35, width=228, height=190)


        customer_button = Button(button_fram,width=22, text="CUSTOMER",command=self.cutomer_details,font=(("times new roman"), 14, "bold"), bg="black",
                          fg="gold", bd=0)
        customer_button.grid(row=0,column=0,pady=1)
        room_button = Button(button_fram, width=22, text="ROOM", font=(("times new roman"), 14, "bold"),
                                 bg="black",
                                 fg="gold", bd=0)
        room_button.grid(row=1, column=0, pady=1)
        details_button = Button(button_fram, width=22, text="DETAILS", font=(("times new roman"), 14, "bold"),
                                 bg="black",
                                 fg="gold", bd=0)
        details_button.grid(row=2, column=0, pady=1)
        report_button = Button(button_fram, width=22, text="REPORT", font=(("times new roman"), 14, "bold"),
                                 bg="black",
                                 fg="gold", bd=0)
        report_button.grid(row=3, column=0, pady=1)
        logout_button = Button(button_fram, width=22, text="LOGOUT", font=(("times new roman"), 14, "bold"),
                                 bg="black",
                                 fg="gold", bd=0)
        logout_button.grid(row=4, column=0,pady=1)

        #==================== right side image ================
        img3 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg2 = Label(main_fram, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg2.place(x=225, y=0, width=1310, height=590)

        #============= Down images =====================
        img4 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\myh.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg3 = Label(main_fram, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=225, width=230, height=180)


        img5 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg4 = Label(main_fram, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=390, width=230, height=190)

    def cutomer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CustomerWindow(self.new_window)


root = Tk()
obj = HotelManagmentSystem(root)
root.mainloop()
