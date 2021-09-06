# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:58:20 2021

@author: MANJEET KUMAR YADAV
"""

# import cv2
# import os
# import face_recognition

# Redaing file from the local disk
# img = cv2.imread(r"C:\Users\MANJEET KUMAR YADAV\.spyder-py3\photos\cat.jpg")

# #Resizing image to small size
# img = cv2.resize(img,(400,300))

# #displaying the original image
# #cv2.imshow("original image",img)

# #applying algorithm to blur the image
# img = cv2.blur(img, ksize = (9, 9))

# # #displaying the blur image
# cv2.imshow("blur image",img)

# it will give a list of all images and any file that is a particular dir

# images = os.listdir(r"C:\Users\MANJEET KUMAR YADAV\.spyder-py3\photos")


# copy the code from the site

# make a list of all the available images
# images = os.listdir('images')
 
# load your image
# image_to_be_matched = face_recognition.load_image_file('manjeet.png')
 
# encoded the loaded image into a feature vector

# image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
 
# # <a href="https://www.pythonpool.com/python-iterate-through-list/" target="_blank" rel="noreferrer noopener">iterate</a> over each image
# for image in images:
#     # load the image
#     current_image = face_recognition.load_image_file("images/" + image)
#     # encode the loaded image into a feature vector
#     current_image_encoded = face_recognition.face_encodings(current_image)[0]
#     # match your image with the image and check if it matches
#     result = face_recognition.compare_faces(
#         [image_to_be_matched_encoded], current_image_encoded)
#     # check if it was a match
#     if result[0] == True:
#         print "Matched: " + image
#     else:
#         print "Not matched: " + image</pre> 



import face_recognition
import numpy as np
import cv2


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("manjeet.png")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("preeti.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "manjeet",
    "preeti"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()



























