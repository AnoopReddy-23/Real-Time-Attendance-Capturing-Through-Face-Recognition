import tkinter as tk
from tkinter import ttk
import pymysql

class ViewStudentsUI:
    def __init__(self, master):
        self.master = master
        master.title("View Students")
        master.geometry('800x600')
        master.configure(background='#F0F0F0')

        view_button = tk.Button(master, text="View Students", command=self.view_students)
        view_button.pack()

    def view_students(self):
        try:
            connection = pymysql.connect(host='localhost',
                                         database='facerec',
                                         user='root',
                                         password='root')

            cursor = connection.cursor()
            select_query = "SELECT name, roll_no FROM student"
            cursor.execute(select_query)
            students = cursor.fetchall()

            view_students_window = tk.Toplevel(self.master)
            view_students_window.title("View Students")
            view_students_window.geometry('800x600')
            view_students_window.configure(background='#F0F0F0')

            tree = ttk.Treeview(view_students_window, style="Custom.Treeview")
            tree["columns"] = ("Name", "Roll No")
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("Name", anchor=tk.CENTER, width=150)
            tree.column("Roll No", anchor=tk.CENTER, width=100)

            tree.heading("Name", text="Name")
            tree.heading("Roll No", text="Roll No")

            tree.tag_configure("Custom.Treeview", font=('Arial', 12))
            tree.tag_configure("Custom.Treeview", background='#FFFFFF')
            tree.tag_configure("Custom.Treeview", foreground='#333333')

            for student in students:
                tree.insert("", tk.END, values=student)

            tree.pack(expand=True, fill=tk.BOTH)

        except pymysql.Error as error:
            tk.messagebox.showerror("Error", f"Failed to fetch student data from MySQL table: {error}")

        finally:
            if connection is not None and connection.open:
                cursor.close()
                connection.close()

if __name__ == '__main__':
    root = tk.Tk()
    view_students_ui = ViewStudentsUI(root)
    root.mainloop()
