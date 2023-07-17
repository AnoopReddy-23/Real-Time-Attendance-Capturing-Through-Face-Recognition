import tkinter as tk
import os

class HomePageUI:
    def __init__(self, master):
        self.master = master
        master.title("Real Time Attendance through Face Recognition")
        master.geometry('800x600')

        title_label = tk.Label(master, text="Real Time Attendance through Face Recognition", bg="#333333",
                               fg="white", width=50, height=2, font=('Arial', 20, 'bold'))
        title_label.pack(pady=20)

        button_frame = tk.Frame(master, bg='#F0F0F0')
        button_frame.pack()

        add_button = tk.Button(button_frame, text="Add Student", command=self.add_student, fg="white", bg="#007BFF",
                               width=15, height=2, font=('Arial', 12, 'bold'), relief=tk.FLAT)
        add_button.grid(row=0, column=0, padx=20, pady=10)

        view_button = tk.Button(button_frame, text="View Students", command=self.view_students, fg="white", bg="#FFC107",
                                width=15, height=2, font=('Arial', 12, 'bold'), relief=tk.FLAT)
        view_button.grid(row=0, column=1, padx=20, pady=10)

        train_button = tk.Button(button_frame, text="Train", command=self.train, fg="white", bg="#28A745",
                                 width=15, height=2, font=('Arial', 12, 'bold'), relief=tk.FLAT)
        train_button.grid(row=1, column=0, padx=20, pady=10)

        attendance_button = tk.Button(button_frame, text="Take Attendance", command=self.take_attendance, fg="white",
                                      bg="#DC3545", width=15, height=2, font=('Arial', 12, 'bold'), relief=tk.FLAT)
        attendance_button.grid(row=1, column=1, padx=20, pady=10)

    def add_student(self):
        os.system('python addStudent.py')

    def view_students(self):
        os.system('python allStudents.py')

    def train(self):
        os.system('python train.py')

    def take_attendance(self):
        os.system('python attendance.py')

if __name__ == '__main__':
    root = tk.Tk()
    home_page = HomePageUI(root)
    root.mainloop()
