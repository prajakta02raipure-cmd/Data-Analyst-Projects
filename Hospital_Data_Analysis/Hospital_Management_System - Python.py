from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from jupyter_server.auth import passwd


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablet = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.Noftablet = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.Expirydate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffects = StringVar()
        self.FurtherInfo = StringVar()
        self.StorageAdvice = StringVar()
        self.BP = StringVar()
        self.UseOfMedication = StringVar()
        self.PatientID = StringVar()
        self.NhsNo = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()


        lbtitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                        font=("Times New Roman", 50, "bold"))
        lbtitle.pack(side=TOP, fill=X)

        # Data Frame
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=5, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=495, height=350)

        # Buttons Frame
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        # Details Frame
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)

        # DataFrameLeft
        lblnameTablet = Label(DataFrameLeft, text="Name of Tablets :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblnameTablet.grid(row=0, column=0)

        comNameTablet = ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablet, font=("Times New Roman", 12, "bold"), width=38)
        comNameTablet["values"] = ("Nice","Corona Vaccination","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.grid(row=0, column=1, sticky=W)

        lblRef = Label(DataFrameLeft, text="Reference No. :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblRef.grid(row=1, column=0, sticky=W)
        txtRef = Entry(DataFrameLeft, textvariable=self.Ref, font=("Times New Roman", 12, "bold"), width=40)
        txtRef.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, text="Dose :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, textvariable=self.Dose, font=("Times New Roman", 12, "bold"), width=40)
        txtDose.grid(row=2, column=1)

        lblNofTablet = Label(DataFrameLeft, text="No. of Tablets :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblNofTablet.grid(row=3, column=0, sticky=W)
        txtNofTablet = Entry(DataFrameLeft, textvariable=self.Noftablet, font=("Times New Roman", 12, "bold"), width=40)
        txtNofTablet.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, text="Lot :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, textvariable=self.Lot, font=("Times New Roman", 12, "bold"), width=40)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, text="Issue Date :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, textvariable=self.IssueDate, font=("Times New Roman", 12, "bold"), width=40)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, text="Expiry Date :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, textvariable=self.Expirydate, font=("Times New Roman", 12, "bold"), width=40)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, text="Daily Dose :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, textvariable=self.DailyDose, font=("Times New Roman", 12, "bold"), width=40)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffects = Label(DataFrameLeft, text="Side Effects :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSideEffects = Entry(DataFrameLeft, textvariable=self.SideEffects, font=("Times New Roman", 12, "bold"), width=40)
        txtSideEffects.grid(row=8, column=1)

        lblFurtherInfo = Label(DataFrameLeft, text="Further Information :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft, textvariable=self.FurtherInfo, font=("Times New Roman", 12, "bold"), width=40)
        txtFurtherInfo.grid(row=0, column=3)

        lblBP = Label(DataFrameLeft, text="Blood Pressure :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblBP.grid(row=1, column=2, sticky=W)
        txtBP = Entry(DataFrameLeft, textvariable=self.BP, font=("Times New Roman", 12, "bold"), width=40)
        txtBP.grid(row=1, column=3)

        lblStorage = Label(DataFrameLeft, text="Storage Advice :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, textvariable=self.StorageAdvice, font=("Times New Roman", 12, "bold"), width=40)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, text="Medication :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataFrameLeft, textvariable=self.UseOfMedication, font=("Times New Roman", 12, "bold"), width=40)
        txtMedicine.grid(row=3, column=3)

        lblPatientID = Label(DataFrameLeft, text="Patient ID :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID = Entry(DataFrameLeft, textvariable=self.PatientID, font=("Times New Roman", 12, "bold"), width=40)
        txtPatientID.grid(row=4, column=3)

        lblNhsNo = Label(DataFrameLeft, text="Nhs No. :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblNhsNo.grid(row=5, column=2, sticky=W)
        txtNhsNo = Entry(DataFrameLeft, textvariable=self.NhsNo, font=("Times New Roman", 12, "bold"), width=40)
        txtNhsNo.grid(row=5, column=3)

        lblPatientName = Label(DataFrameLeft, text="Patient Name :", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataFrameLeft, textvariable=self.PatientName, font=("Times New Roman", 12, "bold"), width=40)
        txtPatientName.grid(row=6, column=3)

        lblDOB = Label(DataFrameLeft, text="Date of Birth :", font=("Times New Roman", 12, "bold"), padx=2,pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataFrameLeft, textvariable=self.DateOfBirth, font=("Times New Roman", 12, "bold"), width=40)
        txtDOB.grid(row=7, column=3)

        lblAddress = Label(DataFrameLeft, text="Patient Address :", font=("Times New Roman", 12, "bold"), padx=2,pady=6)
        lblAddress.grid(row=8, column=2, sticky=W)
        txtAddress = Entry(DataFrameLeft, textvariable=self.PatientAddress, font=("Times New Roman", 12, "bold"), width=40)
        txtAddress.grid(row=8, column=3)

        # Data Frame Right
        self.txtPrescription = Text(DataFrameRight, font=("Times New Roman", 12, "bold"), width=56, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        btPres = Button(ButtonFrame, command=self.iPrescription, text="Prescription", font=("Times New Roman", 12, "bold"), width=26, bg="green", fg="black", padx=2, pady=6)
        btPres.grid(row=0, column=0)

        btData = Button(ButtonFrame, command=self.iPrescriptionData, text="Prescription Data", font=("Times New Roman", 12, "bold"), width=26, bg="green", fg="black",padx=2, pady=6)
        btData.grid(row=0, column=1)

        btUpdate = Button(ButtonFrame, command=self.update, text="Update", font=("Times New Roman", 12, "bold"), bg="green", width=26, fg="black",padx=2, pady=6)
        btUpdate.grid(row=0, column=2)

        btDelete = Button(ButtonFrame, command=self.iDelete, text="Delete", font=("Times New Roman", 12, "bold"), bg="green", width=26, fg="black",padx=2, pady=6)
        btDelete.grid(row=0, column=3)

        btClear = Button(ButtonFrame, command=self.clear, text="Clear", font=("Times New Roman", 12, "bold"), bg="green", width=26, fg="black",padx=2, pady=6)
        btClear.grid(row=0, column=4)

        btExit = Button(ButtonFrame, command=self.iExit, text="Exit", font=("Times New Roman", 12, "bold"), bg="green", width=26, fg="black", padx=2, pady=6)
        btExit.grid(row=0, column=5)

        # Table
        # Scroll Bar
        scr_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scr_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.hosp_table = ttk.Treeview(DetailsFrame, columns=("nameoftablet","ref","dose","noftablets","lot","issuedate","expdate","dailydose","storage","nhsno","pname","dob","address"),xscrollcommand=scr_x.set, yscrollcommand=scr_y.set)
        scr_x.pack(side=BOTTOM, fill=X)
        scr_y.pack(side=RIGHT, fill=Y)

        scr_x= ttk.Scrollbar(command=self.hosp_table.xview)
        scr_y= ttk.Scrollbar(command=self.hosp_table.yview)

        self.hosp_table.heading("nameoftablet", text="Name of Tablets")
        self.hosp_table.heading("ref", text="Reference No.")
        self.hosp_table.heading("dose", text="Dose")
        self.hosp_table.heading("noftablets", text="No. of Tablets")
        self.hosp_table.heading("lot", text="Lot")
        self.hosp_table.heading("issuedate", text="Issue Date")
        self.hosp_table.heading("expdate", text="Expiry Date")
        self.hosp_table.heading("dailydose", text="Daily Dose")
        self.hosp_table.heading("storage", text="Storage")
        self.hosp_table.heading("nhsno", text="Nhs Number")
        self.hosp_table.heading("pname", text="Patient's Name")
        self.hosp_table.heading("dob", text="Date of Birth")
        self.hosp_table.heading("address", text="Patient's Address")

        self.hosp_table["show"]="headings"

        self.hosp_table.column("nameoftablet", width=100)
        self.hosp_table.column("ref", width=100)
        self.hosp_table.column("dose", width=100)
        self.hosp_table.column("noftablets", width=100)
        self.hosp_table.column("lot", width=100)
        self.hosp_table.column("issuedate", width=100)
        self.hosp_table.column("expdate", width=100)
        self.hosp_table.column("dailydose", width=100)
        self.hosp_table.column("storage", width=100)
        self.hosp_table.column("nhsno", width=100)
        self.hosp_table.column("pname", width=100)
        self.hosp_table.column("dob", width=100)
        self.hosp_table.column("address", width=100)

        self.hosp_table.pack(fill=BOTH, expand=1)
        self.hosp_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # Functionality Declaration
    def iPrescriptionData(self):
        print("Insert function called")
        if self.Nameoftablet.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Prajakta02*R",database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (
                                  self.Nameoftablet.get(),
                                  self.Ref.get(),
                                  self.Dose.get(),
                                  self.Noftablet.get(),
                                  self.Lot.get(),
                                  self.IssueDate.get(),
                                  self.Expirydate.get(),
                                  self.DailyDose.get(),
                                  self.StorageAdvice.get(),
                                  self.NhsNo.get(),
                                  self.PatientName.get(),
                                  self.DateOfBirth.get(),
                                  self.PatientAddress.get()
                               )
                              )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Prajakta02*R", database="mydata")
        my_cursor = conn.cursor()

        my_cursor.execute("""
            update hospital set
            Name_of_Tablet=%s,
            Dose=%s,
            No_of_Tablets=%s,
            Lot=%s,
            Issue_Date=%s,
            Expiry_date=%s,
            Daily_Dose=%s,
            Storage=%s,
            Nhs_No=%s,
            Patient_Name=%s,
            DOB=%s,
            Patient_Address=%s
            where Reference_no=%s
        """,
                          (
                              self.Nameoftablet.get(),
                              self.Dose.get(),
                              self.Noftablet.get(),
                              self.Lot.get(),
                              self.IssueDate.get(),
                              self.Expirydate.get(),
                              self.DailyDose.get(),
                              self.StorageAdvice.get(),
                              self.NhsNo.get(),
                              self.PatientName.get(),
                              self.DateOfBirth.get(),
                              self.PatientAddress.get(),
                              self.Ref.get(),
                          ))

        conn.commit()
        conn.close()
        self.fetch_data()

        messagebox.showinfo("Update", "Record has been updated successfully")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Prajakta02*R", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hosp_table.delete(*self.hosp_table.get_children())
            for i in rows:
                self.hosp_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hosp_table.focus()
        content = self.hosp_table.item(cursor_row)
        row = content.get("values")

        if not row:
            return

        self.Nameoftablet.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.Noftablet.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.Expirydate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NhsNo.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablet:\t\t\t" + self.Nameoftablet.get() + "\n")
        self.txtPrescription.insert(END, "Reference No.:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.Noftablet.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + self.Expirydate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effects:\t\t\t" + self.SideEffects.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInfo.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BP.get() + "\n")
        self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientID.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.NhsNo.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def iDelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Prajakta02*R", database="mydata")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_no=%s"
        value = (self.Ref.get(),)
        print("Executing:", query)
        print("With value:", value)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been deleted")

    def clear(self):
        self.Nameoftablet.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.Noftablet.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.Expirydate.set("")
        self.DailyDose.set("")
        self.SideEffects.set("")
        self.FurtherInfo.set("")
        self.StorageAdvice.set("")
        self.BP.set("")
        self.UseOfMedication.set("")
        self.PatientID.set("")
        self.NhsNo.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


root = Tk()
ob = Hospital(root)
root.mainloop()