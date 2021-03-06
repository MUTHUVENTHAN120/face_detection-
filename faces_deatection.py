import cv2
face  = cv2.CascadeClassifier('C:/Users/MUTHUKUMAR/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_console = cv2.CascadeClassifier('C:/Users/MUTHUKUMAR/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml')
cop =cv2.VideoCapture(0)
while True :
    ret ,img = cop.read()
    grp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grp)
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray = grp[y:y+h,x:x+w]
        face_color = img [y:y+h,x:x+w]
        eyes = eye_console.detectMultiScale(face_gray)
        for(ex,ey,ew,eh) in eyes :
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(113)&0xff
    if k==113:
        break
cop.release()
cv2.destroyallwindow()
    
        
