import cv2 as cv
import numpy as np
import serial
import process_image
import cnn_test

# Define the serial connection to Arduino
arduinoData = serial.Serial('com3', 9600)

if cnn_test.generate_predictions() == 1:
    contours = process_image.capture_contour()[1]
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if 4000 <= area <= 10000:
            print('Small Potato')
    
            cv.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    
            text = 'Area :' + str(int(area))
            cv.putText(img, text, (x - 35, y), cv.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
    
            cmd = 'ONE\r'
            arduinoData.write(cmd.encode())
    
        elif 45000 <= area <= 50000:
            print('Medium Potato')
    
            cv.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    
            text = 'Area :' + str(int(area))
            cv.putText(img, text, (x - 35, y), cv.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
    
            cmd = 'TWO\r'
            arduinoData.write(cmd.encode())
    
        elif area >= 50000:
            cv.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    
            text = 'Area :' + str(int(area))
            cv.putText(img, text, (x - 35, y), cv.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
    
            cmd = 'THREE\r'
            arduinoData.write(cmd.encode())
            print("Big Potato")
    
    cv.imshow('Results', img)
    
    if cv.waitKey(1) & 0xFF == ord('c'):
        break
    
    # Release resources when done
    cap.release()
    cv.destroyAllWindows()
