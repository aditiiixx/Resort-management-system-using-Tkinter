# IMPORTING REQUIRED MODULES
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkinter import ttk
import mysql.connector as my
import pyautogui
import matplotlib.pyplot as plt

# establishing connection between python and mysql
db = my.connect(host="localhost", user="root", password="{********}", database="resort")
c = db.cursor()

# defining tkinter window attributes
root = Tk()
root.geometry("676x630")
root.title("Intra Resort Bookings")
root.resizable(0, 0)

# to hide tabs
style = ttk.Style()
style.layout('TNotebook.Tab', [])

def proceedcommand():
    varias = [c11var.get(), c12var.get()]
    tabs = [tab2, tab9]
    for j in range(2):
        if varias[j] == 1:
            Notebook.select(nb, tab_id=tabs[j])  # to jump to the selected tab
            break
        elif [c11var.get(), c12var.get()] == [0, 0]:
            messagebox.showerror("Error", "Please Select A Field")  # messagebox to display error
            break

def review_command():
    i9 = 'SELECT RATING FROM RATINGS'
    c.execute(i9)
    ratings = c.fetchall()  # to fetch data from mysql
    rating_lst, count = [], []
    l1val, l2val, l3val, l4val, l5val = 0, 0, 0, 0, 0
    for h in range(len(ratings)):
        rating_lst.append(ratings[h][0])  # adding elements to list using append
    for m in range(len(rating_lst)):
        if rating_lst[m] == 1:
            l1val += 1
        elif rating_lst[m] == 2:
            l2val += 1
        elif rating_lst[m] == 3:
            l3val += 1
        elif rating_lst[m] == 4:
            l4val += 1
        elif rating_lst[m] == 5:
            l5val += 1
    # adding elements to a particular index position in list
    count.insert(0, l1val)
    count.insert(1, l2val)
    count.insert(2, l3val)
    count.insert(3, l4val)
    count.insert(4, l5val)
    rate = [1, 2, 3, 4, 5]
    # plotting bar graph using matplotlib
    plt.bar(rate, count, color=['fuchsia', 'yellow', 'lime', 'aqua', 'blue'])
    plt.title("CUSTOMER REVIEWS")
    plt.xlabel("RATINGS")
    plt.ylabel("NUMBER OF CUSTOMERS")
    plt.show()  # to display bar graph


def submit_command():
    try:
        values1 = [fvalue.get(), lvalue.get(), centry.get(), aentry.get(), evalue.get()]
        msges1 = [" First Name", 'Last Name', 'Contact Number', 'Aadhar Number/ Passport Id', 'Email Id']
        for k in range(len(values1)):
            if values1[k] == "":
                messagebox.showerror("Error", f'Please Enter {msges1[k]}')
                break
        # to insert data in mysql table
        i1 = 'INSERT INTO CREDENTIALS VALUES(%s, %s, %s, %s, %s)'
        c.execute(i1, (fvalue.get(), lvalue.get(), centry.get(), aentry.get(), evalue.get()))
        db.commit()
    except:
        messagebox.showerror("ERROR", f'PLEASE ENTER VALID DETAILS !!')
    else:
        if fvalue.get() != "" and lvalue.get() != "" and centry.get() != "" and aentry.get() != "" and \
                evalue.get() != "":
            Notebook.select(nb, tab_id=tab3)
            Label(tab8, text="BOOKING SUMMARY", font=('Geometr415 Blk BT', 14), bg='white').place(x=250, y=110)
            Label(tab8, text=f"NAME : {fvalue.get()} {lvalue.get()}\nCONTACT NUMBER :{centry.get()}\nAADHAR "
                             f"NUMBER/PASSPORT ID : "
                             f"{aentry.get()}\nEMAIL-ID :{evalue.get()}", bg='white',
                  font=('Calibri(Body)', 14, 'bold'), anchor=W).place(x=160, y=140)

def back_command():
    backvar = Notebook.index(nb, tab_id='current')
    if backvar == 1 or 8:
        Notebook.select(nb, tab_id=tab1)

def previous_page_command():
    prevar = Notebook.index(nb, tab_id='current')
    tabs = [tab3, tab4, tab5, tab6]
    for num in range(3, 7):
        if prevar == num:
            Notebook.select(nb, tab_id=tabs[num - 3])

def next_page_command():
    nextvar = Notebook.index(nb, tab_id='current')
    tabs = [tab4, tab5, tab6, tab7]
    for num2 in range(2, 6):
        if nextvar == num2:
            Notebook.select(nb, tab_id=tabs[num2 - 2])

def book_command():
    global room_name, price
    # fetching values of checkbutton
    a1 = a1var.get()
    a2 = a2var.get()
    a3 = a3var.get()
    a4 = a4var.get()
    a5 = a5var.get()
    a6 = a6var.get()
    a7 = a7var.get()
    a8 = a8var.get()
    a9 = a9var.get()
    a10 = a10var.get()

    if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0 and a5 == 0:
        if a6 == 0 and a7 == 0 and a8 == 0 and a9 == 0 and a10 == 0:
            messagebox.showerror("Error", "PLEASE SELECT A ROOM TO PROCEED FOR BOOKING")
    if a1 == 1 or a2 == 1 or a3 == 1 or a4 == 1 or a5 == 1 or a6 == 1 or a7 == 1 or a8 == 1 or a9 == 1 or a10 == 1:
        Notebook.select(nb, tab_id=tab8)

    rooms = ["PLAZA GARDEN VIEW ROOM", "DOUBLE BED ROOM", "QUEEN BED ROOM", "KING BED ROOM", "TWIN BED ROOM",
             "EXECUTIVE SUITE", "JUNIOR SUITE", "PRESIDENTIAL SUITE", "ROYAL SPA VILLA", "ROYAL INFINITY VILLA"]
    prices1 = ["Rs.20465", "Rs.22435", "Rs.23735", "Rs.27635", "Rs.29935", "Rs.33975", "Rs.35435", "Rs.45885",
               "Rs.70835", "Rs.60435"]
    a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    for num3 in range(0, 10, 1):
        if a[num3] == 1:
            Label(tab8, text=f"ROOM :{rooms[num3]}\nPRICE :{prices1[num3]}", bg='white',
                  font=('Calibri(Body)', 14, 'bold'), anchor=W).place(x=160, y=234)
            room_name = rooms[num3]
            price = prices1[num3].split("Rs.")
            price = int(price[1])


def finalize_command():
    global room_number, prices2
    values2 = [invalue.get(), outvalue.get(), peoplevalue.get()]
    if values2[0] == "yyyy-mm-dd" or values2[1] == "yyyy-mm-dd" or values2[2] == 0:
        # messagebox to show error
        messagebox.showerror("Error", f'PLEASE FILL THE EMPTY ENTRIES')
    elif values2[0] > values2[1]:
        messagebox.showerror("Error", f'YOU CANT CHEK-OUT BEFORE CHECK-IN (>_<) \nPLEASE ENTER VALID BOOKING DATES!!')
    else:
        c.execute('SELECT ROOM_NUMBER FROM STAY_DETAILS ORDER BY ROOM_NUMBER DESC')
        rno = c.fetchall()
        room_number = rno[0][0] + 1
        amenities = ["AIRPORT TRANSPORTATION", "HOT TUB / SPA", "GAME ROOM", "LAUNDRY", "LOUNGE / BAR", "DINING"]
        prices2 = [4899, 7999, 11499, 4999, 13599, 15000]
        amenities_checked = [c81var, c82var, c83var, c84var, c85var, c86var]
        cost = 0
        for var in range(0, 6):
            if amenities_checked[var].get() == 1:
                cost += prices2[var]
                # to insert data in mysql table
                i4 = 'INSERT INTO EXTRA_AMENITIES VALUES(%s, %s, %s)'
                c.execute(i4, (room_number, amenities[var], prices2[var]))

        i3 = 'INSERT INTO STAY_DETAILS VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        c.execute(i3, (aentry.get(), invalue.get(), outvalue.get(), peoplevalue.get(), room_number, room_name,
                       price * (peoplevalue.get()) * (daysvalue.get()), "CHECKED-IN", daysvalue.get()))

        db.commit()
        total_cost = price * (peoplevalue.get()) * (daysvalue.get()) + cost
        # messagebox to show information
        var12 = messagebox.showinfo("BOOKING SUCCESSFUL!",
                                    f'''THANK YOU {fvalue.get()} {lvalue.get()} FOR BOOKING WITH US, 
                                        YOUR ROOM NUMBER IS {room_number} 
                                        YOUR TOTAL COST IS {total_cost}
                                        YOU MAY PAY AT RECEPTION
                                        ENJOY YOUR VACATION!!!''')
        if var12 == "ok":
            root.destroy()  # command to close tkinter window


def checkout_command():
    c.execute(f'SELECT AP_ID FROM STAY_DETAILS WHERE ROOM_NUMBER = {roomvalue.get()}')
    ap_id_sql = c.fetchone()  # to fetch single value from data
    c.execute(f'SELECT TOTAL_ROOM_COST FROM STAY_DETAILS WHERE ROOM_NUMBER = {roomvalue.get()}')
    total_cost_sql = c.fetchone()
    c.execute(f'SELECT SUM(AMENITY_COST) FROM EXTRA_AMENITIES WHERE ROOM_NO = {roomvalue.get()}')
    amenity_sum_sql = c.fetchone()
    c.execute(f'SELECT ROOM_NUMBER FROM STAY_DETAILS')
    room_lst_sql = c.fetchall()  # to fetch all values from data
    e = 0
    if roomvalue.get() == 0 or avalue2.get() == 0:
        messagebox.showerror("ERROR", f'PLEASE ENTER ALL THE REQUIRED DETAILS')
    elif roomvalue.get() != 0:
        for z in range(len(room_lst_sql)):
            if roomvalue.get() == room_lst_sql[z][0]:
                e += 1
        if e == 0:
            messagebox.showerror("ERROR", f'INVALID ROOM NUMBER')
        # to check if entered room number and aadhar number match or not!
        elif ap_id_sql[0] != avalue2.get():
            messagebox.showerror("ERROR", f'INVALID AADHAR NUMBER/PASSPORT ID FOR ENTERED ROOM NUMBER')
        else:
            if amenity_sum_sql[0] is None:
                payable_amount = total_cost_sql[0]
                # update data in mysql table
                c.execute(f'UPDATE STAY_DETAILS SET STATUS ="CHECKED-OUT" WHERE ROOM_NUMBER = {roomvalue.get()}')
                #  python module used to take rating of the stay from user
                rate = pyautogui.confirm(title='CHECKOUT SUCCESSFUL!', 
	                                    text=f'THANK YOU FOR CHOOSING US!\n'
                                        f'HOPE YOU ENJOYED WELL :)\n'
                                        f'YOUR TOTAL BILL WAS: {payable_amount}\n'
                                        f'PLEASE RATE YOUR STAY AT OUR RESORT!!',
                                        buttons=['1', '2', '3', '4', '5'])
                i8 = 'INSERT INTO RATINGS VALUES(%s, %s)'
                c.execute(i8, (roomvalue.get(), rate))
            elif amenity_sum_sql[0] is not None:
                i6 = f'UPDATE STAY_DETAILS SET STATUS ="CHECKED-OUT" WHERE          ROOM_NUMBER = {roomvalue.get()}'
                c.execute(i6)
                payable_amount = total_cost_sql[0] + amenity_sum_sql[0]
                rate = pyautogui.confirm(title='CHECKOUT SUCCESSFUL!', text=f'THANK YOU              FOR CHOOSING US!\n'
                                          f'HOPE YOU ENJOYED WELL :)\n'
                                          f'YOUR TOTAL BILL WAS: {payable_amount}\n'
                                          f'PLEASE RATE YOUR STAY AT OUR RESORT!!',
                                         buttons=['1', '2', '3', '4', '5'])
                nb.select(tab1)
                i9 = 'INSERT INTO RATINGS VALUES(%s, %s)'
                c.execute(i9, (roomvalue.get(), rate))

    db.commit()
    db.rollback()


nb = Notebook(root)  # defining and creating notebook

# creating frames in notebook
tab1 = Frame(nb)
tab2 = Frame(nb)
tab3 = Frame(nb, bg='tan2')
tab4 = Frame(nb, bg='tan2')
tab5 = Frame(nb, bg='tan2')
tab6 = Frame(nb, bg='tan2')
tab7 = Frame(nb, bg='tan2')
tab8 = Frame(nb)
tab9 = Frame(nb)

tab_lst = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9]
texts = ["HOME", "CHECK - IN", "ROOMS 1", "ROOMS 2", "ROOMS 3", "ROOMS 4", "ROOMS 5", "BOOKING", "CHECK - OUT"]
for i in range(len(tab_lst)):
    tab_lst[i].pack(fill=BOTH)
    nb.add(tab_lst[i], text=texts[i])  # to add tabs to notebook

# importing images
pic1 = PhotoImage(file="page1.PNG")
pic2 = PhotoImage(file="page2.PNG")
pic3 = PhotoImage(file="page3.PNG")
pic4 = PhotoImage(file="page4.PNG")
pic5 = PhotoImage(file="page5.PNG")
pic6 = PhotoImage(file="homepg.PNG")
pic7 = PhotoImage(file="checkinpg.PNG")
pic8 = PhotoImage(file="bookingpg.PNG")
pic9 = PhotoImage(file="checkoutpg.PNG")
# setting background images in tabs
d1 = Label(tab3, image=pic1, bg="pink").pack(fill=BOTH)
d2 = Label(tab4, image=pic2, bg="pink").pack(fill=BOTH)
d3 = Label(tab5, image=pic3, bg="pink").pack(fill=BOTH)
d4 = Label(tab6, image=pic4, bg="pink").pack(fill=BOTH)
d5 = Label(tab7, image=pic5, bg="pink").pack(fill=BOTH)
d6 = Label(tab1, image=pic6, bg="pink").pack(fill=BOTH)
d7 = Label(tab2, image=pic7, bg="pink").pack(fill=BOTH)
d8 = Label(tab8, image=pic8, bg="pink").pack(fill=BOTH)
d9 = Label(tab9, image=pic9, bg="pink").pack(fill=BOTH)

nb.pack(fill=BOTH)

# DEFINING VARIABLES
c11var = IntVar()
c12var = IntVar()

label1 = Label(tab1).pack()
c11 = Checkbutton(tab1, text="CHECK - IN", bg="cyan", variable=c11var, font=('Lucida Calligraphy', 11),
                  activebackground="hot pink", bd=6)
c11.place(x=65, y=130, anchor=NW)
c12 = Checkbutton(tab1, text="CHECK - OUT", bg="cyan", variable=c12var, font=('Lucida Calligraphy', 11),
                  activebackground="hot pink", bd=6)
c12.place(x=345, y=130, anchor=NW)

Button(tab1, text="PROCEED", command=proceedcommand, font=('Lucida Calligraphy', 11, 'bold'), bg="blue",
       fg="white",
       activebackground="hot pink", relief="groove", bd=6).place(x=220, y=200)

Label(tab2, text="First Name", font=('Geometr415 Blk BT', 20), bg='salmon4', fg="white").place(x=150, y=200)
Label(tab2, text="Last Name", font=('Geometr415 Blk BT', 20), bg='salmon4', fg="white").place(x=150, y=240)
Label(tab2, text="Contact Number", font=('Geometr415 Blk BT', 20), bg='salmon4', fg="white").place(x=150, y=280)
Label(tab2, text=f"Aadhar Number /\n Passport Id", font=('Geometr415 Blk BT', 20),
      bg='salmon4', fg="white").place(x=150, y=320)
Label(tab2, text="Email id", font=('Geometr415 Blk BT', 20), bg='salmon4', fg="white").place(x=150, y=392)

Label(tab8, text="CHECK - IN ", bg='black', fg='white', font='bold').place(x=20, y=290)
Label(tab8, text="CHECK - OUT ", bg='black', fg='white', font='bold').place(x=340, y=290)
Label(tab8, text="NUMBER\n OF PERSONS", bg='black', fg='white', font='bold').place(x=20, y=320)
Label(tab8, text="NUMBER OF\n DAYS ", bg='black', fg='white', font='bold').place(x=340, y=320)
Label(tab8,
      text=f'WANT TO ENJOY SOME EXTRA AMENITIES ?\nTHERE YOU GO... JUST CHECK THE BOXES YOU WANT :) ',
      bg='white', fg='black', font=('Geometr415 Blk BT', 11, 'bold')).place(x=80, y=367)

label4 = Label(tab9, text="PLEASE ENTER THE FOLLOWING DETAILS :--", bg='white', fg='black',
               font=('Geometr415 Blk BT', 16, 'bold')).place(x=100, y=150)
roomno = Label(tab9, text="Room Number", font=('Geometr415 Blk BT', 16), bg='black', fg="white").place(x=170, y=250)
aadharno2 = Label(tab9, text=f"Aadhar Number /\nPassport Id", font=('Geometr415 Blk BT', 16),
                  bg='black', fg="white").place(x=170, y=300)

fvalue = StringVar()
lvalue = StringVar()
cvalue = IntVar(value="")
avalue1 = IntVar(value="")
evalue = StringVar()
invalue = StringVar(value="yyyy-mm-dd")
outvalue = StringVar(value="yyyy-mm-dd")
peoplevalue = IntVar()
daysvalue = IntVar()
roomvalue = IntVar()
avalue2 = IntVar()

# ENTRY WIDGET
fentry = Entry(tab2, textvariable=fvalue)
fentry.place(x=380, y=210)
lentry = Entry(tab2, textvariable=lvalue)
lentry.place(x=380, y=250)
centry = Entry(tab2, textvariable=cvalue)
centry.place(x=380, y=290)
aentry = Entry(tab2, textvariable=avalue1)
aentry.place(x=380, y=350)
eentry = Entry(tab2, textvariable=evalue)
eentry.place(x=380, y=400)

inentry = Entry(tab8, textvariable=invalue).place(x=140, y=290)
outentry = Entry(tab8, textvariable=outvalue).place(x=460, y=290)
peopleentry = Entry(tab8, textvariable=peoplevalue).place(x=140, y=320)
daysentry = Entry(tab8, textvariable=daysvalue).place(x=460, y=320)
roomentry = Entry(tab9, textvariable=roomvalue).place(x=360, y=255)
aentry2 = Entry(tab9, textvariable=avalue2).place(x=360, y=315)

a1var = IntVar()
a2var = IntVar()
a3var = IntVar()
a4var = IntVar()
a5var = IntVar()
a6var = IntVar()
a7var = IntVar()
a8var = IntVar()
a9var = IntVar()
a10var = IntVar()
c81var = IntVar()
c82var = IntVar()
c83var = IntVar()
c84var = IntVar()
c85var = IntVar()
c86var = IntVar()

# CHECKBUTTON WIDGET
Checkbutton(tab3, text="PLAZA GARDEN VIEW ROOM", bg="tan2", variable=a1var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=35, anchor=NW)
Checkbutton(tab3, text="DOUBLE BED ROOM", bg="tan2", variable=a2var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=240, anchor=NW)
Checkbutton(tab4, text="QUEEN BED ROOM", bg="tan2", variable=a3var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=30,
                                                          anchor=NW)
Checkbutton(tab4, text="KING BED ROOM", bg="tan2", variable=a4var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=240, anchor=NW)
Checkbutton(tab5, text="TWIN BED ROOM", bg="tan2", variable=a5var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=30, anchor=NW)
Checkbutton(tab5, text="EXECUTIVE SUITE", bg="tan2", variable=a6var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=300, anchor=NW)
Checkbutton(tab6, text="JUNIOR SUITE", bg="tan2", variable=a7var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=15, anchor=NW)
Checkbutton(tab6, text="PRESIDENTIAL SUITE", bg="tan2", variable=a8var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=276, anchor=NW)
Checkbutton(tab7, text="ROYAL SPA VILLA", bg="tan2", variable=a9var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=10, anchor=NW)
Checkbutton(tab7, text="ROYAL INFINITY VILLA", bg="tan2", variable=a10var, activebackground="cyan",
            font=('Geometr415 Blk BT', 12, 'bold')).place(x=2, y=270, anchor=NW)


# BUTTON WIDGET
b21 = Button(tab2, text="SUBMIT", command=submit_command, bd=6, font=('Lucida Calligraphy', 16), bg="saddle brown",
             relief="groove", activebackground="sienna1").place(x=400, y=470)
b22 = Button(tab2, text="BACK", command=back_command, bd=6, font=('Lucida Calligraphy', 16), bg="saddle brown",
             relief="groove", activebackground="sienna1").place(x=100, y=470)
b31 = Button(tab3, text="NEXT -->", command=next_page_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=RIGHT)
b32 = Button(tab3, text="BOOK NOW", command=book_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=BOTTOM)
b41 = Button(tab4, text="NEXT -->", command=next_page_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=RIGHT)
b42 = Button(tab4, text="<-- PREVIOUS", command=previous_page_command, bg="cyan",
             activebackground="deep pink", relief="groove", bd=6).pack(side=LEFT)
b43 = Button(tab4, text="BOOK NOW", command=book_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=BOTTOM)
b51 = Button(tab5, text="NEXT -->", command=next_page_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=RIGHT)
b52 = Button(tab5, text="<-- PREVIOUS", command=previous_page_command, bg="cyan",
             activebackground="deep pink", relief="groove", bd=6).pack(side=LEFT)
b53 = Button(tab5, text="BOOK NOW", command=book_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=BOTTOM)
b61 = Button(tab6, text="NEXT -->", command=next_page_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=RIGHT)
b62 = Button(tab6, text="<-- PREVIOUS", command=previous_page_command, bg="cyan",
             activebackground="deep pink", relief="groove", bd=6).pack(side=LEFT)
b63 = Button(tab6, text="BOOK NOW", command=book_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=BOTTOM)
b71 = Button(tab7, text="<-- PREVIOUS", command=previous_page_command, bg="cyan",
             activebackground="deep pink", relief="groove", bd=6).pack(side=LEFT)
b72 = Button(tab7, text="BOOK NOW", command=book_command, bg="cyan", activebackground="deep pink", relief="groove",
             bd=6).pack(side=BOTTOM)
b8 = Button(tab8, text="FINALISE MY BOOKING", command=finalize_command, bg="hot pink", activebackground="deep sky blue",
            relief="groove", bd=6, font=('Lucida Calligraphy', 12)).place(x=220, y=560)
b91 = Button(tab9, text="CHECK - OUT", command=checkout_command, font=('Lucida Calligraphy', 16, 'bold'),
             bg="blue2", relief="groove", activebackground="hot pink", bd=7, fg='white').place(x=340, y=390)
b92 = Button(tab9, text="BACK", command=back_command, font=('Lucida Calligraphy', 16, 'bold'),
             bg="blue2", relief="groove", activebackground="hot pink", bd=7, fg='white').place(x=140, y=390)
b10 = Button(tab1, text="CLICK HERE FOR CUSTOMER REVIEWS", command=review_command, font=('Lucida Calligraphy', 16),
             bg="cyan", relief="groove", activebackground="hot pink", bd=7).place(x=2, y=350, anchor=NW)


c81 = Checkbutton(tab8, text="AIRPORT TRANSPORTATION  [Rs.4,899.00]", variable=c81var, bg="black", fg="cyan",
                  font='bold').place(x=20, y=420)
c82 = Checkbutton(tab8, text="HOT TUB / SPA  [Rs.7,999.00]", variable=c82var, bg='black', fg="deep pink",
                  font='bold').place(x=20, y=440)
c83 = Checkbutton(tab8, text="GAME ROOM  [Rs.11,499.00]", variable=c83var, bg='black', fg="cyan",
                  font='bold').place(x=20, y=460)
c84 = Checkbutton(tab8, text="LAUNDRY  [Rs.4,999]", variable=c84var, bg='black', fg="deep pink",
                  font='bold').place(x=20, y=480)
c85 = Checkbutton(tab8, text="LOUNGE / BAR  [Rs.13,599.00]", variable=c85var, bg='black', fg="cyan",
                  font='bold').place(x=20, y=500)
c86 = Checkbutton(tab8, text="DINING  [Rs.15,000.00]", variable=c86var, bg='black', fg="deep pink",
                  font='bold').place(x=20, y=520)

# TO BE CALLED FOR GUI TO FUNCTION PROPERLY
root.mainloop()
