# Python program to save a
# video using OpenCV


import cv2
from pygrabber.dshow_graph import FilterGraph

print("Wybierz urzadzenie")
dev = FilterGraph().get_input_devices()
for i in range(0, len(dev)):
    print(str(i) + ": " + str(dev[i]))
ch_cam = int(input())

video = cv2.VideoCapture(ch_cam)
if video.isOpened() == False:
    print("Error opening camera")
    exit()

# change size from camera to integer tuple
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
static_back = None
result = cv2.VideoWriter('video.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         20, size)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recording=False
photo_counter = 0
motion = 0

while (True):
    ret, frame = video.read()


    if ret == True:
        if recording or motion == 1:
            result.write(frame)

        #facial detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


        #motion detection
        motion = 0
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if static_back is None:
            static_back = gray
            continue
        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
        cnts, _ = cv2.findContours(thresh_frame.copy(),
                                   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            # making green rectangle around the moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow('Podglad', frame)

        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            break
        if k & 0xFF == ord(' '):
            cv2.imwrite("photo" + str(photo_counter) + ".png", frame)
            photo_counter = photo_counter + 1
        if k & 0xFF == ord('r'):
            recording = not recording
    else:
        break

video.release()
result.release()
cv2.destroyAllWindows()
