from tkinter import *;
from PIL import Image, ImageTk;
from tkinter import ttk

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
        lebal_floor = Label(left_label_frame, text="Floor", font=(("arial"), 10, "bold"),
                                         padx=2, pady=6)
        lebal_floor.grid(row=0, column=0, sticky=W)

        entry_floor = ttk.Entry(left_label_frame, width=29, font=(("arial"), 10, "bold"))
        entry_floor.grid(row=0, column=1)

        # ==== Room No Label ==========
        lebal_room_no = Label(left_label_frame, text="Room No", font=(("arial"), 10, "bold"),
                            padx=2, pady=6)
        lebal_room_no.grid(row=1, column=0, sticky=W)

        entry_room_no = ttk.Entry(left_label_frame, width=29, font=(("arial"), 10, "bold"))
        entry_room_no.grid(row=1, column=1)


        # ==== Room Type Label ==========
        lebal_room_type = Label(left_label_frame, text="Room Type", font=(("arial"), 10, "bold"),
                            padx=2, pady=6)
        lebal_room_type.grid(row=2, column=0, sticky=W)

        entry_room_type = ttk.Entry(left_label_frame, width=29, font=(("arial"), 10, "bold"))
        entry_room_type.grid(row=2, column=1)

        # ================= Buttons ========================
        button_frame = Frame(left_label_frame, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=220, width=400, height=40)

        add_button = Button(button_frame, text="Add", font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
        add_button.grid(row=0, column=0, padx=1)

        update_button = Button(button_frame, text="Update", font=(("arial"), 10, "bold"), bg="black", fg="gold",
                               width=9)
        update_button.grid(row=0, column=1, padx=1)

        delete_button = Button(button_frame, text="Delete", font=(("arial"), 10, "bold"), bg="black", fg="gold",
                               width=9)
        delete_button.grid(row=0, column=2, padx=1)

        reset_button = Button(button_frame, text="Reset", font=(("arial"), 10, "bold"), bg="black", fg="gold", width=9)
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

root = Tk()
obj = RoomDetails(root)
root.mainloop()
