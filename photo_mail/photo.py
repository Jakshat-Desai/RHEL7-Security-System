#!/usr/bin/python36
import cv2,subprocess
cap=cv2.VideoCapture(0)
ret,img=cap.read()
dt=subprocess.getoutput("date")
cv2.imwrite('/root/Desktop/photo_mail/security/jakeimg_'+str(dt)+'.jpg',img)
cap.release()
