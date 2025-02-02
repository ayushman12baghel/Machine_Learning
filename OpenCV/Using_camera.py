import cv2

cap=cv2.VideoCapture(0)
out=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'),20.0,(640,480))
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
