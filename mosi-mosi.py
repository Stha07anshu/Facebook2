
from tkinter import *
import sqlite3
from tkinter import messagebox
from turtle import update

root =Tk()
root.title('Facebook')
conn = sqlite3.connect("database2.db")
c = conn.cursor()

# c.execute("""CREATE TABLE user(
#     firstname text,
#     lastname text,
#     age integer,
#     address text,
#     city text,
#     zipcode integer,
#     password text,
#     gender text

# )""")


  
f_name = Entry(root,width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root,width=30)
l_name.grid(row=1, column=1)

age= Entry(root, width=30)
age.grid(row=2, column=1)

address = Entry(root, width=30)
address.grid(row=3, column=1)

city = Entry(root, width=30)
city.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

password=Entry(root,width=30)
password.grid(row=6,column=1)

gender=Entry(root,width=30)
gender.grid(row=7,column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=11,column=1,pady=5)

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=2, column=0) 

address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)

city_label = Label(root, text="City")
city_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=6, column=0)

gender_label = Label(root, text="Gender")
gender_label.grid(row=7, column=0)


delete_label = Label(root,text="Delete ID")
delete_label.grid(row=11,column=0,pady=5)

def submit():
    conn = sqlite3.connect('database2.db')
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (:f_name, :l_name, :age, :address, :city, :zipcode, :password, :gender)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'age':age.get(),
        'address':address.get(),
        'city':city.get(),
        'zipcode':zipcode.get(),
        'password':password.get(),
        'gender':gender.get()
    })
    messagebox.showinfo("Address", "Inserted Successfully")
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    password.delete(0,END)
    gender.delete(0,END)

def query():
    conn = sqlite3.connect('database2.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM user ")
    records = c.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record += str(record[0]) + ' '+ str(record[1]) +' ' + '\t' + str(record[8]) + "\n"

    query_label = Label(root, text= print_record)
    query_label.grid(row=10, column=0, columnspan=2)
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect("database2.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE user SET
    firstname = :firstname, 
    lastname = :lastname, 
    age = :age, 
    address = :address, 
    city = :city, 
    zipcode = :zipcode, 
    password = :password, 
    gender = :gender 
    WHERE oid = """ + record_id, 
    {'firstname':f_name.get(),
    'lastname': l_name.get(),
    'age': age.get(),
    'address' : address.get(),
    'city' : city.get(),
    'zipcode' : zipcode.get(),
    'password' : password.get(),
    'gender' : gender.get()
    })
    conn.commit()
    conn.close()
    editor.distroy()


def delete():
    conn=sqlite3.connect('database2.db')
    c=conn.cursor()

    c.execute("DELETE from user WHERE oid = " +delete_box.get())
    print("Deleted Successfully")
    delete_box.delete(0,END)
    conn.commit()
    conn.close()


def edit():
    global editor 
    editor=Toplevel()
    editor.title('Update Date')
    editor.geometry('300x400')
    conn=sqlite3.connect("database2.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE oid="+ record_id )
    records= c.fetchall()
    print(records)

    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor
    global password_editor
    global gender_editor

    f_name_editor = Entry(editor ,width=30)
    f_name_editor.grid(row=0, column=1, padx=20)

    l_name_editor = Entry(editor ,width=30)
    l_name_editor.grid(row=1, column=1)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2, column=1)

    address_editor = Entry(editor , width=30)
    address_editor.grid(row=3, column=1)

    city_editor = Entry(editor , width=30)
    city_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor , width=30)
    zipcode_editor.grid(row=5, column=1)

    password_editor = Entry(editor , width=30)
    password_editor.grid(row=6, column=1)

    
    gender_editor = Entry(editor , width=30)
    gender_editor.grid(row=7, column=1)

    f_name_label = Label(editor,text="First Name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    age_label = Label(editor, text="Age")
    age_label.grid(row=2, column=0) 

    address_label = Label(editor, text="Address")
    address_label.grid(row=3, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    password_label = Label(editor, text="Password")
    password_label.grid(row=6, column=0)

    gender_label = Label(editor, text="Gender")
    gender_label.grid(row=7, column=0)



    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        city_editor.insert(0,record[3])
        zipcode_editor.insert(0,record[5])
        password_editor.insert(0,record[6])
        gender_editor.insert(0,record[7])
    
    
    edit_btn = Button(editor,text="Save",command=update)
    edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=125)
    


submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

edit_btn=Button(root,text="Update",command=edit)
edit_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=125)

conn.commit()
conn.close()
mainloop()