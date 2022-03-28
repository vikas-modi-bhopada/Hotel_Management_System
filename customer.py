from tkinter import *;
from PIL import Image, ImageTk;
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox;

class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Managment System")
        self.root.geometry("1040x435+225+210")


        #=============== Variables ======================
        self.var_ref = IntVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(int(x))
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idProof = StringVar()
        self.var_idNumber = StringVar()




        # ======================Title ==============================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=(("times new roman"), 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1050, height=35)

        # =================  Hotel logo =========================

        img2 = Image.open(r"C:\Users\VIKAS MODI\Desktop\CoreCard Project\Hotel Images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg1.place(x=5, y=2, width=100, height=25)

        # ================== Label Frame =========================
        left_label_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                      font=(("arial"), 12, "bold"), padx=2)
        left_label_frame.place(x=5, y=40, width=330, height=392)

        # ================= lABELS AND ENTRIES ======================
        # ==== Customer Reference
        lebal_customer_reference = Label(left_label_frame, text="Customer Ref", font=(("arial"), 10, "bold"),
                                         padx=2, pady=6)
        lebal_customer_reference.grid(row=0, column=0, sticky=W)

        entry_customer_reference = ttk.Entry(left_label_frame, width=29,textvariable=self.var_ref ,font=(("arial"), 10, "bold"), state="readonly")
        entry_customer_reference.grid(row=0, column=1)

        # ===== Customer name
        lebal_customer_name = Label(left_label_frame, text="Customer Name", font=(("arial"), 10, "bold"),
                                    padx=2, pady=6)
        lebal_customer_name.grid(row=1, column=0, sticky=W)

        entry_customer_name = ttk.Entry(left_label_frame, width=29,textvariable=self.var_cust_name, font=(("arial"), 10, "bold"))
        entry_customer_name.grid(row=1, column=1)

        # ===== Customer Mother name
        lebal_customer_mother_name = Label(left_label_frame, text="Mother Name" ,font=(("arial"), 10, "bold"), padx=2,
                                     pady=6)
        lebal_customer_mother_name.grid(row=2, column=0, sticky=W)

        entry_customer_mother_name = ttk.Entry(left_label_frame, width=29, textvariable=self.var_mother,font=(("arial"), 10, "bold"))
        entry_customer_mother_name.grid(row=2, column=1)

        #====== Gernder Bombobox
        lebal_customer_gender = Label(left_label_frame, text="Gender", font=(("arial"), 10, "bold"), padx=2,
                                           pady=6)
        lebal_customer_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(left_label_frame, textvariable=self.var_gender,font=(("arial"), 10, "bold"), width=27, state= "readonly")
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #====== post code
        lebal_customer_PostCode = Label(left_label_frame, text="PostCode", font=(("arial"), 10, "bold"), padx=2,
                                           pady=6)
        lebal_customer_PostCode.grid(row=4, column=0, sticky=W)

        entry_customer_PostCode = ttk.Entry(left_label_frame, width=29, textvariable=self.var_post,font=(("arial"), 10, "bold"))
        entry_customer_PostCode.grid(row=4, column=1)

        #======= Mobile Number
        lebal_customer_mobile_number= Label(left_label_frame, text="Mobile", font=(("arial"), 10, "bold"), padx=2,
                                           pady=6)
        lebal_customer_mobile_number.grid(row=5, column=0, sticky=W)

        entry_customer_mobile_number = ttk.Entry(left_label_frame, width=29,textvariable=self.var_mobile, font=(("arial"), 10, "bold"))
        entry_customer_mobile_number.grid(row=5, column=1)

        # ======= Email
        lebal_customer_email = Label(left_label_frame, text="Email", font=(("arial"), 10, "bold"), padx=2,
                                             pady=6)
        lebal_customer_email.grid(row=6, column=0, sticky=W)

        entry_customer_email = ttk.Entry(left_label_frame, width=29, textvariable=self.var_email,font=(("arial"), 10, "bold"))
        entry_customer_email.grid(row=6, column=1)

        #======== NATIONALITY
        lebal_customer_nationality = Label(left_label_frame, text="Nationality", font=(("arial"), 10, "bold"), padx=2,
                                     pady=6)
        lebal_customer_nationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(left_label_frame,textvariable=self.var_nationality, font=(("arial"), 10, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("Indian", "American", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)


        #======= Id PRoff type combobox
        lebal_customer_idType = Label(left_label_frame, text="ID Proof Type", font=(("arial"), 10, "bold"), padx=2,
                                     pady=6)
        lebal_customer_idType.grid(row=8, column=0, sticky=W)

        combo_idType = ttk.Combobox(left_label_frame, textvariable=self.var_idProof,font=(("arial"), 10, "bold"), width=27, state="readonly")
        combo_idType["value"] = ("Adhar Card", "Driving Licence", "Passport")
        combo_idType.current(0)
        combo_idType.grid(row=8, column=1)

        #======= Id number
        lebal_customer_Id_number = Label(left_label_frame, text="Id Number", font=(("arial"), 10, "bold"), padx=2,
                                     pady=6)
        lebal_customer_Id_number.grid(row=9, column=0, sticky=W)

        entry_customer_Id_number = ttk.Entry(left_label_frame, width=29, textvariable=self.var_idNumber,font=(("arial"), 10, "bold"))
        entry_customer_Id_number.grid(row=9, column=1)

        #======= Address
        lebal_customer_address = Label(left_label_frame, text="Address", font=(("arial"), 10, "bold"), padx=2,
                                     pady=6)
        lebal_customer_address.grid(row=10, column=0, sticky=W)

        entry_customer_address = ttk.Entry(left_label_frame, width=29,textvariable=self.var_address, font=(("arial"), 10, "bold"))
        entry_customer_address.grid(row=10, column=1)


        #================= Buttons ========================
        button_frame = Frame(left_label_frame, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=350, width=400, height=40)

        add_button = Button(button_frame,text= "Add",command=self.add_data, font=(("arial"), 10, "bold"), bg="black", fg="gold",width=9)
        add_button.grid(row=0, column=0, padx=1)

        update_button = Button(button_frame, text="Update",command=self.update, font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        update_button.grid(row=0, column=1, padx=1)

        delete_button = Button(button_frame, text="Delete",command=self.delete, font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        delete_button.grid(row=0, column=2, padx=1)

        reset_button = Button(button_frame, text="Reset",command=self.reset, font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        reset_button.grid(row=0, column=3, padx=1)

        # ================== Table Frame =========================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                      font=(("arial"), 12, "bold"), padx=2)
        table_frame.place(x=340, y=40, width=695, height=490)

        lebal_search_by = Label(table_frame, font=(("arial"), 12, "bold"), text="Search By:", bg="red", fg="white")
        lebal_search_by.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var, font=(("arial"), 10, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.text_search_var = StringVar()
        entry_search = ttk.Entry(table_frame, width=24,textvariable=self.text_search_var, font=(("arial"), 10, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        search_button = Button(table_frame, text="Search", command=self.search,font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        search_button.grid(row=0, column=3, padx=2)

        show_all_button = Button(table_frame, text="Show All", command=self.fetch_data,font=(("arial"), 10, "bold"), bg="black", fg="gold",
                               width=9)
        show_all_button.grid(row=0, column=4, padx=2)


        #============= Show data table ===================
        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=30, width=690, height=340)

        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.cust_detail_table = ttk.Treeview(details_frame,columns=("Ref", "Name", "Mother Name", "Gender",
                                                                     "Post","Mobile", "Email","Nationality",
                                                                     "Id Proof", "Id Number", "Address")
                                              , xscrollcommand=scroll_x.set,
                                              yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)

        self.cust_detail_table.heading("Ref", text="Refer No")
        self.cust_detail_table.heading("Name", text="Name")
        self.cust_detail_table.heading("Mother Name", text="Mother Name")
        self.cust_detail_table.heading("Gender", text="Gender")
        self.cust_detail_table.heading("Post", text="Post")
        self.cust_detail_table.heading("Mobile", text="Mobile")
        self.cust_detail_table.heading("Email", text="Email")
        self.cust_detail_table.heading("Nationality", text="Nationality")
        self.cust_detail_table.heading("Id Proof", text="Id Proof")
        self.cust_detail_table.heading("Id Number", text="Id Number")
        self.cust_detail_table.heading("Address", text="Address")

        self.cust_detail_table["show"]="headings"

        self.cust_detail_table.column("Ref", width=100)
        self.cust_detail_table.column("Name", width=100)
        self.cust_detail_table.column("Mother Name", width=100)
        self.cust_detail_table.column("Gender", width=100)
        self.cust_detail_table.column("Post", width=100)
        self.cust_detail_table.column("Mobile", width=100)
        self.cust_detail_table.column("Email", width=100)
        self.cust_detail_table.column("Nationality", width=100)
        self.cust_detail_table.column("Id Proof", width=100)
        self.cust_detail_table.column("Id Number", width=100)
        self.cust_detail_table.column("Address", width=100)



        self.cust_detail_table.pack(fill=BOTH, expand=1)
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mother.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "All fields are required", parent= self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")

                mycursor = mydb.cursor()

                mycursor.execute("insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_idProof.get(),
                        self.var_idNumber.get(),
                        self.var_address.get() ))
                mydb.commit()
                self.fetch_data()
                mydb.close()
                self.reset()
                messagebox.showinfo("Success", "Customer has been added successfully", parent= self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Some thing went worn {str(e)}",parent= self.root)
                mydb.rollback()
                mydb.close()

    def fetch_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = mydb.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("",END,values=i)
                mydb.commit()
            mydb.close()

    def get_cursor(self,event=""):
        cursor_row = self.cust_detail_table.focus()
        content = self.cust_detail_table.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idProof.set(row[8])
        self.var_idNumber.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile == "":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = mydb.cursor()
            my_cursor.execute("update customer set Name=%s, Mother = %s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s where Ref=%s",(
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idProof.get(),
                self.var_idNumber.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            mydb.commit()
            self.fetch_data()
            mydb.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully",parent=self.root)

    def delete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer",parent=self.root)
        if mdelete > 0:
            mydb = mysql.connector.connect(host="localhost", user="root",password="", database="management")
            my_cursor = mydb.cursor()
            query = "delete from customer where Ref=%s"
            val = (self.var_ref.get(),)
            my_cursor.execute(query,val)
            mydb.commit()
            self.fetch_data()
            mydb.close()
            messagebox.showinfo("Succcess", "Customer details has been deleted successfully", parent=self.root)

        else:
            if not mdelete:
                return

    def reset(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(int(x))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_idNumber.set("")

    def search(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="management")

        my_cursor = mydb.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search_var.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("", END, values=i)
                mydb.commit()
            mydb.close()





root = Tk()
obj = CustomerWindow(root)
root.mainloop()
