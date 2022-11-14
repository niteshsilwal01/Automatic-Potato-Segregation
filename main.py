import cv2
import numpy as np
import cnn_test

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    if cnn_test.generate_predictions(test_image_path=frame,actual_label='Potato') ==1:
        print('Potato Found !!')
    
        # Belt
        belt = frame[209: 327, 137: 280]
        gray_belt = cv2.cvtColor(belt, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray_belt, 80, 255, cv2.THRESH_BINARY)
        
        # Detect the Potatoes
        _, contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            
            # Calculate area
            area = cv2.contourArea(cnt)
            
            # Distinguish small and big potatoes
            if area > 400:
                # big potato
                cv2.rectangle(belt, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #Detection by sensor 3 & turn servo 3 on 
                
                
                
            elif 100 < area < 400:
                #small potato
                cv2.rectangle(belt, (x, y), (x + w, y + h), (255, 0, 0), 2)
                #Detection by sensor 2 & turn servo 2 on
                
            cv2.putText(belt, str(area), (x, y), 1, 1, (0, 255, 0))
    else:
        print('Potato Not Found !!')
        #Buzzer on
        #Detection by sensor 1 & turn servo 1 on
    
    cv2.imshow("Frame", frame)
    cv2.imshow("belt", belt)
    cv2.imshow("threshold", threshold)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    
cap.release()
cv2.destroyAllWindows()