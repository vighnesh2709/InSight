import mediapipe as mp
import cv2 as cv
import numpy as np

mp_drawing=mp.solutions.drawing_utils # This is a module used to draw the points on the hand upon detection.
mp_hands=mp.solutions.hands # This is a mediapipe module used to find out where the points are on the hand.

cap=cv.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
  while True:
      ret,frame=cap.read()

      image=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
      image.flags.writeable=False
      result=hands.process(image)
      image.flags.writeable=True
      image=cv.cvtColor(image,cv.COLOR_RGB2BGR)
      print(result)
      print(result.multi_hand_landmarks)


      if result.multi_hand_landmarks:
         for num,hand in enumerate(result.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)

      cv.imshow("hand tracking",image)

      key=cv.waitKey(20)&0xFF
      if key==ord('d'):
        break
cap.release()
cv.destroyAllWindows()
