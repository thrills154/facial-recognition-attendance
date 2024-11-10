# import face_recognition
# import cv2
# import numpy as np
# from datetime import datetime
#
# # Example known faces (must be replaced with actual encodings and names)
# known_face_encodings = [...]  # Ensure this list is populated
# known_face_names = [...]       # Ensure this list is populated
#
# def recognize_faces():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         return
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Frame not captured.")
#             break
#
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#         rgb_small_frame = small_frame[:, :, ::-1]
#
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"
#
#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#                 print(f"Attendance recorded for {name} at {datetime.now()}")
#
#         cv2.imshow('Face Recognition Attendance', frame)
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
# recognize_faces()
# # import importlib
# #
# # List of required modules
# modules = [
#     "os", "pickle", "numpy", "cv2", "face_recognition", "cvzone",
#     "firebase_admin", "datetime"
# ]
#
# # Check for each module
# for module in modules:
#     try:
#         importlib.import_module(module)
#         print(f"{module}: Installed")
#     except ImportError:
#         print(f"{module}: Not Installed")
