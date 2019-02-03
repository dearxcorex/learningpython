#!/usr/bin/env python3

import face_recognition


face_obama = face_recognition.load_image_file("obama.jpg")
face_encoding = face_recognition.face_encodings(face_obama)[0]

#unknowface 

unknow_pic = face_recognition.load_image_file("unknow.jpeg")
#print(unknow_pic[0])
unknow_face_encoding = face_recognition.face_encodings(unknow_pic)[0]

results = face_recognition.compare_faces([face_encoding],unknow_face_encoding)

#print(results)

'''
if results[0] == True:
    print("obama")

else:
    print("NO")


'''    
