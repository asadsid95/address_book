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
delete_label = Label(root, text="Delete ID")
delete_label.grid(row=9,column=0)

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
delete_entry = Entry(root, width=25)
delete_entry.grid(row=9,column=1,columnspan=2,pady=10,padx=10)

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
    # print(profiles[0])

    print_profiles = ''
    for profile in profiles:
        print_profiles += str(profile[0]) + " " + str(profile[1]) + "\t" + str(profile[6]) + "\n"

    query_label = Label(root, text=print_profiles)
    query_label.grid(row=11,column=0, columnspan=2)

    conn.commit()
    conn.close

def delete():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    
    cur.execute("DELETE FROM addresses WHERE oid=" + delete_entry.get())
    
    conn.commit()
    conn.close

def edit():
    editor = Tk()
    editor.title("Editor")

    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("UPDATE address  *, oid FROM addresses")
    profiles = cur.fetchall()
    # print(profiles[0])

    print_profiles = ''
    for profile in profiles:
        print_profiles += str(profile[0]) + " " + str(profile[1]) + "\t" + str(profile[6]) + "\n"

    query_label = Label(root, text=print_profiles)
    query_label.grid(row=11,column=0, columnspan=2)

    conn.commit()
    conn.close

    # label fields
    f_name_editor = Label(editor, text="First name")
    f_name_editor.grid(row=0, column=0)
    l_name_editor = Label(editor, text="Last name")
    l_name_editor.grid(row=1, column=0)
    address_editor = Label(editor, text="Address")
    address_editor.grid(row=2, column=0)
    city_editor = Label(editor, text="City")
    city_editor.grid(row=3, column=0)
    state_editor = Label(editor, text="State")
    state_editor.grid(row=4, column=0)
    zipcode_editor = Label(editor, text="Zipcode")
    zipcode_editor.grid(row=5, column=0)

    # user input
    f_name =  Entry (editor, width=25)
    f_name.grid(row=0, column=1)
    l_name = Entry(editor, width=25)
    l_name.grid(row=1, column=1)
    address = Entry(editor, width=25)
    address.grid(row=2, column=1)
    city = Entry(editor, width=25)
    city.grid(row=3, column=1)
    state = Entry(editor, width=25)
    state.grid(row=4, column=1)
    zipcode = Entry(editor, width=25)
    zipcode.grid(row=5, column=1)

    update_button = Button(editor, text="Update Record")
    update_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# submit button
submit_button=Button(root, text="Submit", command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# query button
query_button=Button(root, text="Query", command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# delete button
delete_button=Button(root,text="Delete Records",command=delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# note: create new window for editor
edit_button=Button(root,text="Update Records",command=edit)
edit_button.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=120)


root.mainloop()