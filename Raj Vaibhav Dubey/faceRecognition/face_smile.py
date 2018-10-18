

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
font = cv2.FONT_HERSHEY_COMPLEX

video_capture = cv2.VideoCapture(0)
def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 4)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color= frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 6)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 1)	
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
		for(sx , sy, sw, sh) in smiles:
			cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0, 0, 255), 1)
			cv2.putText(roi_color, "Stay Happy", (sx ,sy ), font, 0.5, (255,255,255), 2)
	return frame



while True:
	_, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	canvas = detect(gray, frame)
	cv2.imshow('Video', canvas)
	if cv2.waitKey(1) & 0xFF == ord('x'):
		break
video_capture.release()
cv2.destroyAllWindows()


