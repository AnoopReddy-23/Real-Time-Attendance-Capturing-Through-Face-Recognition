import cv2
import face_recognition
import xlwt
import datetime
import os
import pymysql

# Load the face encodings and names from the file
known_faces = []
known_names = []

with open('encodings.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        face_encoding = [float(e) for e in data[:-1]]
        name = data[-1]
        known_faces.append(face_encoding)
        known_names.append(name)

video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
face_names = []
present_students = []

while True:
    ret, frame = video_capture.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Compare the face with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # Calculate face distance to determine if it matches any known face
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = face_distances.argmin()

        # If a match is found and the distance is below a threshold, assign the known name
        if matches[best_match_index] and face_distances[best_match_index] < 0.5:
            name = known_names[best_match_index]

        face_names.append(name)
        if name not in present_students:
            present_students.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw the name on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('Take Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

# Establish a connection to the MySQL student table
connection = pymysql.connect(host='localhost',
                             database='facerec',
                             user='root',
                             password='root')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the Attendance folder if it doesn't exist
if not os.path.exists('Attendance'):
    os.makedirs('Attendance')

# Save attendance in an Excel sheet
wb = xlwt.Workbook()
sheet = wb.add_sheet('Attendance')

sheet.write(0, 0, 'Date')
sheet.write(0, 1, 'Time')
sheet.write(0, 2, 'Roll No')
sheet.write(0, 3, 'Name')

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H-%M-%S")

for i, student_roll in enumerate(present_students):
    # Retrieve the student name based on the roll number from the student table
    query = f"SELECT name FROM student WHERE roll_no = '{student_roll}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        student_name = result[0]
        sheet.write(i + 1, 0, date)
        sheet.write(i + 1, 1, time)
        sheet.write(i + 1, 2, student_roll)
        sheet.write(i + 1, 3, student_name)

attendance_filename = f'Attendance/attendance_{date}_{time}.xls'
wb.save(attendance_filename)

# Close the cursor and connection to the database
cursor.close()
connection.close()

print(f"Attendance recorded. File saved as: {attendance_filename}")
