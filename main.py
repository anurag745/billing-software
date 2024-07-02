from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import keyboard
from PIL import Image, ImageTk

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")
        
        # Title
        lbl_title = Label(self.root, text="BILLING SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="black")
        lbl_title.place(x=0, y=0, width=1500, height=50)

        # Main frame
        MainFrame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        MainFrame.place(x=0, y=50, width=1500, height=750)

        # Customer Frame
        CustomerFrame = LabelFrame(MainFrame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="black")
        CustomerFrame.place(x=10, y=5, width=900, height=90)

        self.lbl_mob = Label(CustomerFrame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)
        self.input_mob = ttk.Entry(CustomerFrame, font=("times new roman", 12))
        self.input_mob.grid(row=0, column=1)

        self.lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_name.grid(row=0, column=4, stick=W, padx=5, pady=2)
        self.input_name = ttk.Entry(CustomerFrame, font=("times new roman", 12))
        self.input_name.grid(row=0, column=5)

        # Product Frame
        ProductFrame = LabelFrame(MainFrame, text="Products", font=("times new roman", 12, "bold"), bg="white", fg="black")
        ProductFrame.place(x=10, y=100, width=900, height=400)

        # Custom Product Frame
        CustomProductFrame = LabelFrame(MainFrame, text="Add Custom Product", font=("times new roman", 12, "bold"), bg="white", fg="black")
        CustomProductFrame.place(x=10, y=520, width=900, height=150)

        self.lbl_custom_product_no = Label(CustomProductFrame, text="Product No", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_custom_product_no.grid(row=0, column=0, stick=W, padx=5, pady=2)
        self.input_custom_product_no = ttk.Entry(CustomProductFrame, font=("times new roman", 12))
        self.input_custom_product_no.grid(row=0, column=1)

        self.lbl_custom_product_name = Label(CustomProductFrame, text="Name", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_custom_product_name.grid(row=0, column=2, stick=W, padx=5, pady=2)
        self.input_custom_product_name = ttk.Entry(CustomProductFrame, font=("times new roman", 12))
        self.input_custom_product_name.grid(row=0, column=3)

        self.lbl_custom_product_price = Label(CustomProductFrame, text="Price", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_custom_product_price.grid(row=1, column=0, stick=W, padx=5, pady=2)
        self.input_custom_product_price = ttk.Entry(CustomProductFrame, font=("times new roman", 12))
        self.input_custom_product_price.grid(row=1, column=1)

        self.lbl_custom_product_quantity = Label(CustomProductFrame, text="Quantity", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_custom_product_quantity.grid(row=1, column=2, stick=W, padx=5, pady=2)
        self.input_custom_product_quantity = ttk.Entry(CustomProductFrame, font=("times new roman", 12))
        self.input_custom_product_quantity.grid(row=1, column=3)

        # Button to add custom product
        self.Btnadd_product = Button(CustomProductFrame, text="Add Product", font=('arial', 13, "bold"), bg="green", fg="white", cursor="hand2", command=self.add_custom_product)
        self.Btnadd_product.grid(row=2, column=0, columnspan=4, pady=10)

         # Bill Area
        Rightlabel = LabelFrame(MainFrame, text="Bill Area", font=("times new roman", 12, "bold"))
        Rightlabel.place(x=950, y=110, width=500, height=350)

        scrolly = Scrollbar(Rightlabel, orient=VERTICAL)
        self.textarea = Text(Rightlabel, yscrollcommand=scrolly.set, bg="white", fg="blue")
        scrolly.pack(side=RIGHT, fill=Y)
        self.textarea.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.textarea.yview)

        Rightlabel.bind('<Enter>', self._bound_to_mousewheel_text)
        Rightlabel.bind('<Leave>', self._unbound_to_mousewheel_text)

        # Button Frame
        BtnFrame = Frame(MainFrame, bg="white")
        BtnFrame.place(x=950, y=550)

        self.Btngenerate_bill = Button(BtnFrame, height=2, text="Generate Bill", font=('arial', 13, "bold"), bg="green", fg="white", cursor="hand2", command=self.generate_bill)
        self.Btngenerate_bill.grid(row=0, column=0, padx=100, pady=2)

        self.Btnsave_as_pdf = Button(BtnFrame, height=2, text="Save as PDF", font=('arial', 13, "bold"), bg="green", fg="white", cursor="hand2", command=self.save_as_pdf)
        self.Btnsave_as_pdf.grid(row=0, column=1, padx=5, pady=2)

        # Bill number
        BillnoFrame = Frame(MainFrame, bg="white", bd=2, relief=GROOVE)
        BillnoFrame.place(x=950, y=12, width=500, height=80)

        lbl_billno = Label(BillnoFrame, text="Bill No. : ", bg="white", fg="black", font=('arial', 13, "bold"))
        lbl_billno.grid(row=0, column=0, padx=10, pady=25)
        self.input_billno = ttk.Entry(BillnoFrame, font=("times new roman", 12))
        self.input_billno.grid(row=0, column=1, pady=5)
        self.Searchbtn = Button(BillnoFrame, text="Search", font=('arial', 13, "bold"), bg="green", fg="white", cursor="hand2", command=self.search)
        self.Searchbtn.grid(row=0, column=2, padx=3, pady=1)

        # Treeview Scrollbar
        product_scroll = Scrollbar(ProductFrame)
        product_scroll.pack(side=RIGHT, fill=Y)

        
        # Treeview Table
        self.product_table = ttk.Treeview(ProductFrame, style="Custom.Treeview", yscrollcommand=product_scroll.set, columns=("product_no", "name", "price", "quantity", "total_cost"))
        self.product_table.pack(fill=BOTH, expand=1)
        product_scroll.config(command=self.product_table.yview)

        self.product_table.heading("product_no", text="Product No")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("quantity", text="Quantity")
        self.product_table.heading("total_cost", text="Total Cost")

        self.product_table['show'] = 'headings'
        self.product_table.column("product_no", width=100)
        self.product_table.column("name", width=150)
        self.product_table.column("price", width=100)
        self.product_table.column("quantity", width=100)
        self.product_table.column("total_cost", width=100)

        # Bindings for mousewheel
        self.product_table.bind('<Enter>', self._bound_to_mousewheel)
        self.product_table.bind('<Leave>', self._unbound_to_mousewheel)

        keyboard.on_press(self.on_barcode_scan)


    def on_barcode_scan(self, event):
        barcode = event.name
        if len(barcode) > 1:
            self.add_scanned_product(barcode)

    def add_scanned_product(self, barcode):
        product_name = barcode
        product_price = 0
        product_quantity = 1
        total_cost = product_price * product_quantity

        self.product_table.insert("", "end", values=(barcode, product_name, product_price, product_quantity, total_cost))

    def search(self):
        pass

    def generate_bill(self):
        customer_name = self.input_name.get()
        customer_mob = self.input_mob.get()
        if customer_name and customer_mob:
            self.textarea.delete('1.0', END)
            self.textarea.insert(END, "BILL\n")
            self.textarea.insert(END, "-----------------\n")
            self.textarea.insert(END, f"Customer Name: {customer_name}\n")
            self.textarea.insert(END, f"Mobile No: {customer_mob}\n")
            self.textarea.insert(END, "-----------------\n")
            self.textarea.insert(END, "Products:\n")
            for child in self.product_table.get_children():
                product = self.product_table.item(child)["values"]
                self.textarea.insert(END, f"{product[0]} - {product[1]} - {product[2]} - {product[3]} - {product[4]}\n")
            self.textarea.insert(END, "-----------------\n")
            self.textarea.insert(END, "Total Cost: \n")
            self.textarea.insert(END, "-----------------\n")
            self.textarea.insert(END, "Thank you for shopping with us!")
        else:
            messagebox.showerror("Error", "Please enter customer details")

    def save_as_pdf(self):
        bill_content = self.textarea.get('1.0', END)
        if bill_content.strip():
            try:
                with open("bill.txt", "w") as f:
                    f.write(bill_content)
                os.system("libreoffice --convert-to pdf bill.txt")
                messagebox.showinfo("Save as PDF", "Bill saved as PDF successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save as PDF: {e}")
        else:
            messagebox.showerror("Error", "Bill content is empty")

    def add_custom_product(self):
        product_no = self.input_custom_product_no.get()
        product_name = self.input_custom_product_name.get()
        product_price = self.input_custom_product_price.get()
        product_quantity = self.input_custom_product_quantity.get()

        if product_no and product_name and product_price and product_quantity:
            try:
                total_cost = int(product_price) * int(product_quantity)
                self.product_table.insert("", "end", values=(product_no, product_name, product_price, product_quantity, total_cost))
                self.input_custom_product_no.delete(0, END)
                self.input_custom_product_name.delete(0, END)
                self.input_custom_product_price.delete(0, END)
                self.input_custom_product_quantity.delete(0, END)
            except ValueError:
                messagebox.showerror("Error", "Price and Quantity must be numbers")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    
    def _bound_to_mousewheel(self, event):
        self.product_table.bind_all("<MouseWheel>", self._on_mousewheel)
    def _unbound_to_mousewheel(self, event):
        self.product_table.unbind_all("<MouseWheel>")

    def _bound_to_mousewheel_text(self, event):
        self.textarea.bind_all("<MouseWheel>", self._on_mousewheel_text)

    def _unbound_to_mousewheel_text(self, event):
        self.textarea.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.product_table.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_mousewheel_text(self, event):
        self.textarea.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()

