from sqlite3.dbapi2 import Row
from tkinter import *
import sqlite3

root = Tk()

# cur.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer 
#     )""")

# label fields
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# user input
f_name =  Entry (root, width=25)
f_name.grid(row=0, column=1)
l_name = Entry(root, width=25)
l_name.grid(row=1, column=1)
address = Entry(root, width=25)
address.grid(row=2, column=1)
city = Entry(root, width=25)
city.grid(row=3, column=1)
state = Entry(root, width=25)
state.grid(row=4, column=1)
zipcode = Entry(root, width=25)
zipcode.grid(row=5, column=1)

def submit():

    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn.commit()
    conn.close

def query():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM addresses")
    profiles = cur.fetchall()
    print(profiles)

    print_profiles = ''
    for profile in profiles[0]:
        print_profiles += str(profile) + "\n"

    query_label = Label(root, text=print_profiles)
    query_label.grid(row=8,column=0)

    conn.commit()
    conn.close

# submit button
submit_button=Button(root, text="Submit", command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=60)

# query button
query_button=Button(root, text="Query", command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=60)
root.mainloop()

