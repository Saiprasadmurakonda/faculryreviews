import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
#pymysql , mysql.connector , sqlite3
win=tk.Tk()
win.geometry("1300x700+0+0")
win.title("Faculty Review Portal")
title_label=tk.Label(win, text="Faculty Review Portal", font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP, fill= tk.X)
detail_frame=tk.LabelFrame(win, text="Kindly fill these fields",font= ("Arial",20),bd=12, relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=800,height=520)
data_frame=tk.Frame(win, bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=840,y=90,width=350,height=575)

# Varaibles
rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
syllabus=tk.StringVar()
interest=tk.StringVar()
quiz=tk.StringVar()
punctual=tk.StringVar()
opinion=tk.StringVar()

# search_by=tk.StringVar()

# --Entry -- #
rollno_lbl=tk.Label(detail_frame,text="Roll No", font=("Arial",15),bg="lightgrey")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_frame,bd=7, font=("Arial",15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name", font=("Arial",15),bg="lightgrey")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_frame,bd=7, font=("Arial",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)


class_lbl=tk.Label(detail_frame,text="Class", font=("Arial",15),bg="lightgrey")
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent=tk.Entry(detail_frame,bd=7, font=("Arial",15),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)

section_lbl=tk.Label(detail_frame,text="Section", font=("Arial",15),bg="lightgrey")
section_lbl.grid(row=3,column=0,padx=2,pady=2)

section_ent=tk.Entry(detail_frame,bd=7, font=("Arial",15),textvariable=section)
section_ent.grid(row=3,column=1,padx=2,pady=2)

syllabus_lbl=tk.Label(detail_frame,text="covers syllabus in time", font=("Arial",15),bg="lightgrey")
syllabus_lbl.grid(row=4,column=0,padx=2,pady=2)

syllabus_ent=ttk.Combobox(detail_frame, font=("Arial",15),state="readonly", textvariable=syllabus)
syllabus_ent['values']=("1","2","3","4","5")
syllabus_ent.grid(row=4,column=1,padx=2,pady=2)

interest_lbl=tk.Label(detail_frame,text="links to real life experiences ", font=("Arial",15),bg="lightgrey")
interest_lbl.grid(row=5,column=0,padx=2,pady=2)

interest_ent=ttk.Combobox(detail_frame,font=("Arial",15),state="readonly", textvariable=interest)
interest_ent['values']=("1","2","3","4","5")
interest_ent.grid(row=5,column=1,padx=2,pady=2)

quiz_lbl=tk.Label(detail_frame,text="conducts regular quizzes and teaches accordingly.", font=("Arial",15),bg="lightgrey")
quiz_lbl.grid(row=6,column=0,padx=2,pady=2)

quiz_ent=ttk.Combobox(detail_frame, font=("Arial",15),state="readonly", textvariable=quiz)
quiz_ent['values']=("1","2","3","4","5")
quiz_ent.grid(row=6,column=1,padx=2,pady=2)

punctual_lbl=tk.Label(detail_frame,text="regular and punctual in class.", font=("Arial",15),bg="lightgrey")
punctual_lbl.grid(row=7,column=0,padx=2,pady=2)
punctual_ent=ttk.Combobox(detail_frame, font=("Arial",15),state="readonly",textvariable=punctual)
punctual_ent['values']=("1","2","3","4","5")
punctual_ent.grid(row=7,column=1,padx=2,pady=2)



opinion_lbl=tk.Label(detail_frame,text="invites opinion and questions on subject matter", font=("Arial",15),bg="lightgrey")
opinion_lbl.grid(row=8,column=0,padx=2,pady=2)

opinion_ent=ttk.Combobox(detail_frame, font=("Arial",15),state="readonly", textvariable=opinion)
opinion_ent['values']=("1","2","3","4","5")
opinion_ent.grid(row=8,column=1,padx=2,pady=2)


# functions
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms2")
    curr=conn.cursor()
    curr.execute("SELECT * FROM data2")
    rows=curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
        conn.close()
def add_func():
    if rollno.get()=="" or name.get()=="" or class_var.get()=="":
        messagebox.showerror("Error! Please fill all the fields")
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="sms2")
        curr=conn.cursor()
        curr.execute("INSERT INTO DATA2 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),section.get(),syllabus.get(),interest.get(),quiz.get(),punctual.get(),opinion.get()))
        conn.commit()
        conn.close()
        fetch_data()
def get_cursor(event):
    """Fetches Data of selected Row"""
    cursor_row=student_table.focus()
    content= student_table.item(cursor_row)
    row=content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    syllabus.set(row[4])
    interest.set(row[5])
    quiz.set(row[6])
    punctual.set(row[7])
    opinion.set(row[8])
def clear():
    """This will clear the entry boxes"""
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    syllabus.set("")
    interest.set("")
    quiz.set("")
    punctual.set("")
    opinion.set("")


def update_fun():
    """This will update"""
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms2")
    curr=conn.cursor()
    curr.execute("UPDATE DATA2 SET name=%s , class=%s, section=%s,syllabus=%s, interest=%s, quiz=%s,punctual=%s,opinion=%s where rollno=%s",(name.get(),class_var.get(),section.get(),syllabus.get(),interest.get(),quiz.get(),punctual.get(),opinion.get(),rollno.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()

def delete():
    """ This will delete"""
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms2")
    curr=conn.cursor()
    curr.execute("DELETE FROM DATA2 where rollno=%s and name=%s",(rollno.get(), name.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()


# Buttons

btn_frame= tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=18,y=390,width=340,height=120)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)


update_btn=tk.Button(btn_frame,bg="lightgrey",text="Update",bd=7,font=("Arial",13),width=15,command=update_fun)
update_btn.grid(row=0,column=1,padx=2,pady=2)


delete_btn=tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15,command=delete)
delete_btn.grid(row=1,column=0,padx=2,pady=2)


clear_btn=tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=7,font=("Arial",13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=2,pady=2)


# Database Frame
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(data_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

"""Name, Class, Section, contact, Father Name, Gender, D.O.B, Address"""
student_table= ttk.Treeview(main_frame, columns=("Roll No.","Name","Class", "Section", "syllabus", "interest",  "quiz", "punctual","opinion",),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("Roll No.",text="Roll No.")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("syllabus",text="syllabus")
student_table.heading("interest",text="interest")
student_table.heading("quiz",text="quiz")
student_table.heading("punctual",text="punctual")
student_table.heading("opinion",text="opinion")

student_table['show']='headings'


student_table.column("Name",width=100)
student_table.column("Roll No.",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("syllabus",width=100)
student_table.column("interest",width=100)
student_table.column("quiz",width=100)
student_table.column("punctual",width=100)
student_table.column("opinion",width=150)

student_table.pack(fill= tk.BOTH, expand=True)


fetch_data()
student_table.bind("<ButtonRelease -1>",get_cursor)

win.mainloop()
