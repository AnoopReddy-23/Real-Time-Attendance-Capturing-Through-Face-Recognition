# import face_recognition
# import os
#
# known_faces = []
# known_names = []
#
# # Load face images and names from the student_faces folder
# for dir_name in os.listdir('student_faces'):
#     if os.path.isdir(os.path.join('student_faces', dir_name)):
#         for filename in os.listdir(os.path.join('student_faces', dir_name)):
#             if filename.endswith('.jpg'):
#                 face_image = face_recognition.load_image_file(os.path.join('student_faces', dir_name, filename))
#                 face_encodings = face_recognition.face_encodings(face_image)
#
#                 if len(face_encodings) > 0:
#                     face_encoding = face_encodings[0]
#                     known_faces.append(face_encoding)
#                     known_names.append(dir_name)
#
# # Save the encodings and names to a file
# with open('encodings.txt', 'w') as file:
#     for i in range(len(known_faces)):
#         face_encoding = known_faces[i]
#         name = known_names[i]
#         encoding_str = ','.join(str(e) for e in face_encoding)
#         file.write(f"{encoding_str},{name}\n")
#
# print("Training completed.")

import face_recognition
import os
import tkinter as tk

def train_model():
    known_faces = []
    known_names = []

    # Load face images and names from the student_faces folder
    for dir_name in os.listdir('student_faces'):
        if os.path.isdir(os.path.join('student_faces', dir_name)):
            for filename in os.listdir(os.path.join('student_faces', dir_name)):
                if filename.endswith('.jpg'):
                    face_image = face_recognition.load_image_file(os.path.join('student_faces', dir_name, filename))
                    face_encodings = face_recognition.face_encodings(face_image)

                    if len(face_encodings) > 0:
                        face_encoding = face_encodings[0]
                        known_faces.append(face_encoding)
                        known_names.append(dir_name)

    # Save the encodings and names to a file
    with open('encodings.txt', 'w') as file:
        for i in range(len(known_faces)):
            face_encoding = known_faces[i]
            name = known_names[i]
            encoding_str = ','.join(str(e) for e in face_encoding)
            file.write(f"{encoding_str},{name}\n")

    # Update the GUI status label
    status_label['text'] = "Training completed."

def start_training():
    # Update the GUI status label
    status_label['text'] = "Training in progress..."
    status_label.update()

    # Call the train_model function
    train_model()

# Create a Tkinter GUI window
window = tk.Tk()
window.title("Face Recognition Training")
window.geometry("400x200")

# Create a label to display the status
status_label = tk.Label(window, text="Click 'Start Training' to begin the training.", font=("Arial", 14))
status_label.pack(pady=50)

# Create a button to start the training
start_button = tk.Button(window, text="Start Training", command=start_training, font=("Arial", 14))
start_button.pack()

# Start the Tkinter event loop
window.mainloop()