from tkinter import *
from tkinter import messagebox
import pymysql
import cv2
import os

def capture_images(roll_no):
    # Create a directory for storing the student's face images
    directory = f'student_faces/{roll_no}'
    if not os.path.exists(directory):
        os.makedirs(directory)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(1)

    count = 0  # Counter for capturing multiple images

    while count < 101:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite(f'{directory}/{roll_no}_{count}.jpg', frame[y:y + h, x:x + w])

        cv2.imshow('Add Student', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

    video_capture.release()
    cv2.destroyAllWindows()

def add_student():
    name = name_entry.get()
    roll_no = roll_entry.get()

    # Save student details to MySQL database
    try:
        connection = pymysql.connect(host='localhost',
                                     database='facerec',
                                     user='root',
                                     password='root')

        cursor = connection.cursor()
        insert_query = "INSERT INTO student (name, roll_no) VALUES (%s, %s)"
        student_data = (name, roll_no)
        cursor.execute(insert_query, student_data)
        connection.commit()
        messagebox.showinfo("Success", "Student added successfully to the database")

    except pymysql.Error as error:
        messagebox.showerror("Error", f"Failed to insert student data into MySQL table: {error}")

    finally:
        if connection is not None and connection.open:
            cursor.close()
            connection.close()
    capture_images(roll_no)



root = Tk()
root.title("Add Student")

name_label = Label(root, text="Name:")
name_label.pack()

name_entry = Entry(root)
name_entry.pack()

roll_label = Label(root, text="Roll No:")
roll_label.pack()

roll_entry = Entry(root)
roll_entry.pack()

add_button = Button(root, text="Add Student", command=add_student)
add_button.pack()

root.mainloop()
