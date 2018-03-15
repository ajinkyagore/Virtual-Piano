import cv2
import numpy as np
from threading import Thread
from playsound import playsound
#from piano_thread import WebcamVideoStream
import pygame
import time

pygame.init()
pygame.mixer.init()

def sound1():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
	time.sleep(2)	

def sound2():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1s.wav').play()
	time.sleep(2)	

def sound3():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/b1.wav').play()
	time.sleep(2)	

def sound4():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1.wav').play()
	time.sleep(2)	

def sound5():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1s.wav').play()
	time.sleep(2)	

def sound6():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c2.wav').play()
	time.sleep(2)	

def sound7():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1.wav').play()
	time.sleep(2)	

def sound8():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1s.wav').play()
	time.sleep(2)	

def sound9():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/e1.wav').play()
	time.sleep(2)	

def sound10():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1.wav').play()
	time.sleep(2)	

def sound11():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1s.wav').play()
	time.sleep(2)	

def sound12():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1.wav').play()
	time.sleep(2)	

def sound13():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1s.wav').play()
	time.sleep(2)	

def sound14():
	pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
	time.sleep(2)	


cap = cv2.VideoCapture(1)
# vs = WebcamVideoStream(src=1).start()
k = True
key_threshold = 1300
ret, t0 = cap.read()
ret, t1 = cap.read()
# t0 = vs.read()
# t1 = vs.read()
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
thread1 = Thread()
thread2 = Thread()

while True:
	t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
	diff = cv2.absdiff(t1, t0)
	ret,threshold_image = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	key1 = cv2.countNonZero(threshold_image[355:410,0:35])
	key2 = cv2.countNonZero(threshold_image[355:410,40:85])
	key3 = cv2.countNonZero(threshold_image[355:410,90:130])
	key4 = cv2.countNonZero(threshold_image[355:410,135:183])
	key5 = cv2.countNonZero(threshold_image[355:410,183:230])
	key6 = cv2.countNonZero(threshold_image[355:410,230:275])
	key7 = cv2.countNonZero(threshold_image[355:410,275:325])
	key8 = cv2.countNonZero(threshold_image[355:410,325:370])
	key9 = cv2.countNonZero(threshold_image[355:410,370:420])
	key10 = cv2.countNonZero(threshold_image[355:410,420:470])
	key11 = cv2.countNonZero(threshold_image[355:410,470:515])
	key12 = cv2.countNonZero(threshold_image[355:410,515:560])
	key13 = cv2.countNonZero(threshold_image[355:410,560:610])
	key14 = cv2.countNonZero(threshold_image[355:410,610:638])
	
	if k:
	 	if key1 > key_threshold:
	 		Thread(target=sound1).start()

	 	if key2 > key_threshold:
	 		Thread(target=sound2).start()

	 	if key3 > key_threshold:
	 		Thread(target=sound3).start()

	 	if key4 > key_threshold:
	 		Thread(target=sound4).start()

	 	if key5 > key_threshold:
	 		Thread(target=sound5).start()

	 	if key6 > key_threshold:
	 		Thread(target=sound6).start()

	 	if key7 > key_threshold:
	 		Thread(target=sound7).start()

	 	if key8 > key_threshold:
	 		Thread(target=sound8).start()

	 	if key9 > key_threshold:
	 		Thread(target=sound9).start()

	 	if key10 > key_threshold:
	 		Thread(target=sound10).start()

	 	if key11 > key_threshold:
	 		Thread(target=sound11).start()

	 	if key12 > key_threshold:
	 		Thread(target=sound12).start()

	 	if key13 > key_threshold:
	 		Thread(target=sound13).start()

	 	if key14 > key_threshold:
	 		Thread(target=sound14).start()

	k = not k
	cv2.imshow('Window', threshold_image)

	t0 = t1
	ret, t1 = cap.read()
	#t1 = vs.read()	
	#time.sleep(0.1)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
#vs.stop()
