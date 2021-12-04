from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("550x250")        # the interface size
root.title("GRADE BOX")          # project namee
root.config(bg="gray")


def do_nothing():            # nothing when clicked on
    file_win = Toplevel(root)
    button = Button(file_win, text="Do nothing button")
    button.pack()


menu = Menu(root)        # menu option
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=do_nothing)
file_menu.add_command(label="Open", command=do_nothing)
file_menu.add_command(label="Save", command=do_nothing)
file_menu.add_command(label="Save as...", command=do_nothing)
file_menu.add_command(label="Close", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label="Undo", command=do_nothing)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=do_nothing)
edit_menu.add_command(label="Copy", command=do_nothing)
edit_menu.add_command(label="Paste", command=do_nothing)
edit_menu.add_command(label="Delete", command=do_nothing)
edit_menu.add_command(label="Select All", command=do_nothing)
menu.add_cascade(label="Edit", menu=edit_menu)
help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label="Help Index", command=do_nothing)
help_menu.add_command(label="About...", command=do_nothing)
menu.add_cascade(label="Help", menu=help_menu)

course = [StringVar(), StringVar(), StringVar()]         # user input is entered
course[0].set("Name: " + course[0].get())                # getting values from user's input
course[1].set("Department: " + course[1].get())
course[2].set("Course: " + course[2].get())
seek = StringVar()


def clear():         # the clear button area
    score1Entry.delete(0, END)
    nameEntry.delete(0, END)
    departmentEntry.delete(0, END)
    levelEntry.delete(0, END)
    seekEntry.delete(0, END)
    score2Entry.delete(0, END)
    score3Entry.delete(0, END)
    score4Entry.delete(0, END)
    result1.delete(0, END)
    result2.delete(0, END)
    result3.delete(0, END)
    result4.delete(0, END)


def save():          # save button area
    rest = course[0].get() + "\t" + course[1].get() + "\t" + course[2].get() + "\n"
    file = grade[0].get() + "\n" + grade[1].get() + "\n" + grade[2].get() + "\n" + grade[3].get() + "\n"
    with open("text.txt", "a") as x:
        x.write(rest)
        x.write(file)
        if course[0].get() in x.read():
            messagebox.showinfo("Outcome", "name already in file")
        else:
            return x.write(rest)


def search():            # search button area
    with open("text.txt") as f:
        if seek.get() in f.read():
            messagebox.showinfo("Outcome", "Name found")
        else:
            messagebox.showinfo("Outcome", "Name not found")


score1, score2, score3, score4 = (IntVar(), IntVar(), IntVar(), IntVar())
grade = (StringVar(), StringVar(), StringVar(), StringVar())


def calculate(var1, var2, var3, var4):           # calculating user result
    data = [var1, var2, var3, var4]
    for i in range(len(data)):
        if data[i] <= 30:
            grade[i].set("Fail")
        elif data[i] <= 50:
            grade[i].set("Pass")
        elif data[i] <= 70:
            grade[i].set("Credit")
        elif data[i] <= 100:
            grade[i].set("Excellence")
        else:
            grade[i].set("NONE")


'''
nameLabel = Label(root, text="Name", bg="gray").grid(row=0, column=0)
departmentLabel = Label(root, text="Department", bg="gray").grid(row=1, column=0)
levelLabel = Label(root, text="Course", bg="gray").grid(row=2, column=0)
'''
nameEntry = Entry(root, width=30, bg="pink", textvariable=course[0])
departmentEntry = Entry(root, width=30, bg="pink", textvariable=course[1])
levelEntry = Entry(root, width=30, bg="pink", textvariable=course[2])
seekEntry = Entry(root, width=20, textvariable=seek)
seekLabel = Button(root, text="Search for existing name", bg="pink", state="disable").grid(row=6, column=2)
scoreLabel = Button(root, text="ENTER YOUR SCORE", bg="gray").grid(row=4, columnspan=1)
resultLabel = Button(root, text="RESULT", bg="gray", ).grid(row=4, columnspan=3)
score1Entry = Entry(root, width=20, textvariable=score1)
score2Entry = Entry(root, width=20, textvariable=score2)
score3Entry = Entry(root, width=20, textvariable=score3)
score4Entry = Entry(root, width=20, textvariable=score4)
result1 = Entry(root, width=20, textvariable=grade[0])
result2 = Entry(root, width=20, textvariable=grade[1])
result3 = Entry(root, width=20, textvariable=grade[2])
result4 = Entry(root, width=20, textvariable=grade[3])

nameEntry.grid(row=1, column=0, padx=10, pady=10)
departmentEntry.grid(row=1, column=1, padx=10, pady=10)
levelEntry.grid(row=1, column=2, padx=10, pady=10)
seekEntry.grid(row=7, column=2, padx=10, pady=10)
score1Entry.grid(row=5, columnspan=1, padx=10, pady=10)
score2Entry.grid(row=6, columnspan=1, padx=10, pady=10)
score3Entry.grid(row=7, columnspan=1, padx=10, pady=10)
score4Entry.grid(row=8, columnspan=1, padx=10, pady=10)
result1.grid(row=5, columnspan=3, padx=10, pady=10)
result2.grid(row=6, columnspan=3, padx=10, pady=10)
result3.grid(row=7, columnspan=3, padx=10, pady=10)
result4.grid(row=8, columnspan=3, padx=10, pady=10)

saveButton = Button(root, text="Save", bg="gray", fg="pink", command=save).grid(row=9, column=0)
completeButton = Button(root, text="Complete", bg="gray", fg="pink",
                        command=lambda: calculate(score1.get(), score2.get(), score3.get(), score4.get())).grid(row=9,
                                                                                                                column=1)
clear_b = Button(root, text="Clear", bg="white", fg="black", command=lambda: clear()).grid(row=9, columnspan=2)
searchButton = Button(root, text="Search", bg="pink", command=search).grid(row=8, column=2)

root.config(menu=menu)
root.mainloop()
