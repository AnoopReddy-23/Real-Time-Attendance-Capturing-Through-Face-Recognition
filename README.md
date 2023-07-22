 # Real-Time-Attendance-Capturing-Through-Face-Recognition

This project is a Face Recognition based Attendance Management System. The system uses face recognition technology to mark the attendance of students by recognizing their faces. It simplifies the attendance process by automatically capturing and storing attendance data in an Excel sheet.
The Face Recognition Attendance System is a powerful and efficient solution for managing attendance in educational institutions and organizations. This system leverages cutting-edge face recognition technology to accurately and automatically mark the attendance of students or employees, streamlining the attendance tracking process and reducing administrative burden.

## Features

### 1. Real-time Face Recognition

The Face Recognition Attendance System offers real-time face recognition capabilities, enabling it to identify multiple faces simultaneously. The system can recognize faces from various angles and distances, making it suitable for diverse scenarios, including classrooms, lecture halls, and office spaces.

### 2. User-friendly Graphical Interface

The system comes with a user-friendly graphical interface developed using Tkinter, a Python library for GUI. The interface enables easy interaction with the application, making it accessible to users with minimal technical expertise.

### 3. Storage of Face Encodings and Names

To enhance the speed and accuracy of face recognition, the system stores pre-calculated face encodings and corresponding names in a file (`encodings.txt`). This efficient storage method eliminates the need to recompute encodings for each recognition, ensuring a smooth and responsive attendance tracking experience.

### 4. Fetching Student Names from MySQL Database

In addition to using pre-stored face encodings, the system can fetch student or employee names from a MySQL database based on their unique identifiers, such as roll numbers or employee IDs. This feature provides improved identification and personalization, ensuring accurate attendance recording.

### 5. Excel Sheet for Attendance Records

The system saves the attendance data in an Excel sheet. Each attendance entry includes the date, time, and the names of the recognized individuals who are present. The Excel sheet serves as a convenient and organized record of attendance, allowing administrators to review and manage attendance data efficiently.


## Requirements

- Python 3.x
- OpenCV
- face_recognition
- xlwt
- pymysql
- tkinter (for GUI)


