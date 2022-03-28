from tkinter import *;
from PIL import Image, ImageTk;
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox;

class RoomDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Managment System")
        self.root.geometry("1040x435+225+210")

        # ======================Title ==============================
        lbl_title = Label(self.root, text="ADD ROOM DETAILS", font=(("times new roman"), 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1050, height=35)

        # =================  Hotel logo =========================

        img2 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg1.place(x=5, y=2, width=100, height=25)

        # ================== Label Frame =========================
        left_label_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                      font=(("arial"), 12, "bold"), padx=2)
        left_label_frame.place(x=5, y=40, width=330, height=270)

        #==== Floor Label ==========
        self.floor_var = StringVar()
        lebal_floor = Label(left_label_frame, text="Floor", font=(("arial"), 10, "bold"),
                                         padx=2, pady=6)
        lebal_floor.grid(row=0, column=0, sticky=W)

        entry_floor = ttk.Entry(left_label_frame, width=29,textvariable=self.floor_var, font=(("arial"), 10, "bold"))
        entry_floor.grid(row=0, column=1)

        # ==== Room No Label ==========
        self.room_number_var = StringVar()
        lebal_room_no = Label(left_label_frame, text="Room No", font=(("arial"), 10, "bold"),
                            padx=2, pady=6)
        lebal_room_no.grid(row=1, column=0, sticky=W)

        entry_room_no = ttk.Entry(left_label_frame, width=29, textvariable=self.room_number_var,font=(("arial"), 10, "bold"))
        entry_room_no.grid(row=1, column=1)


        # ==== Room Type Label ==========
        self.room_type_var = StringVar()
        lebal_room_type = Label(left_label_frame, text="Room Type", font=(("arial"), 10, "bold"),
                            padx=2, pady=6)
        lebal_room_type.grid(row=2, column=0, sticky=W)

        entry_room_type = ttk.Entry(left_label_frame, width=29, textvariable=self.room_type_var,font=(("arial"), 10, "bold"))
        entry_room_type.grid(row=2, column=1)

        # ================= Buttons ========================
        button_frame = Frame(left_label_frame, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=220, width=400, height=40)

        add_button = Button(button_frame, text="Add", command=self.add_data,font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        add_button.grid(row=0, column=0, padx=1)

        update_button = Button(button_frame, text="Update", command=self.update,font=(("arial"), 10, "bold"), bg="black", fg="gold",
                               width=9)
        update_button.grid(row=0, column=1, padx=1)

        delete_button = Button(button_frame, text="Delete", command=self.delete,font=(("arial"), 10, "bold"), bg="black", fg="gold",
                               width=9)
        delete_button.grid(row=0, column=2, padx=1)

        reset_button = Button(button_frame, text="Reset",command=self.reset, font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        reset_button.grid(row=0, column=3, padx=1)

        # ================== Table Frame =========================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",
                                 font=(("arial"), 12, "bold"), padx=2)
        table_frame.place(x=400, y=40, width=330, height=270)

        #======== Scroll Bar ========================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, columns=("floor", "roomNo", "roomType")
                                       , xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomNo", text="Room No")
        self.room_table.heading("roomType", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomNo", width=100)
        self.room_table.column("roomType", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.floor_var.get() == "" or self.room_number_var.get() == "" or self.room_type_var.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = mydb.cursor()
                my_cursor.execute("insert into roomdetails values(%s, %s, %s)",(
                    self.floor_var.get(),
                    self.room_number_var.get(),
                    self.room_type_var.get()
                ))
                mydb.commit()
                messagebox.showinfo("Success", "Room Details has been added successfully")
                self.fetch_data()
                self.reset()
                mydb.close()
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went worn {str(e)}", parent= self.root)


    def fetch_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = mydb.cursor()
        my_cursor.execute("select * from roomdetails")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                mydb.commit()
            mydb.close()

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.floor_var.set(row[0])
        self.room_number_var.set(row[1])
        self.room_type_var.set(row[2])

    def reset(self):
        self.floor_var.set("")
        self.room_number_var.set("")
        self.room_type_var.set("")


    def update(self):
        if self.room_number_var.get() == "":
            messagebox.showerror("Error", "Please Enter Room Number", parent=self.root)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = mydb.cursor()
            my_cursor.execute("update roomdetails set Floor=%s, RoomType = %s where RoomNumber=%s",(
                self.floor_var.get(),
                self.room_type_var.get(),
                self.room_number_var.get(),
            ))
            mydb.commit()
            self.fetch_data()
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)
            self.reset()
            mydb.close()


    def delete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room",parent=self.root)
        if mdelete > 0:
            mydb = mysql.connector.connect(host="localhost", user="root",password="", database="management")
            my_cursor = mydb.cursor()
            query = "delete from roomdetails where RoomNumber=%s"
            val = (self.room_number_var.get(),)
            my_cursor.execute(query,val)
            mydb.commit()
            self.fetch_data()
            self.reset()
            mydb.close()
            messagebox.showinfo("Succcess", "Room details has been deleted successfully", parent=self.root)

        else:
            if not mdelete:
                return




root = Tk()
obj = RoomDetails(root)
root.mainloop()
