import cv2 as cv
import cnn_test

def capture_contour():
  cv.namedWindow('Params')
  cv.resizeWindow('Params', 640, 90)
  cv.createTrackbar('Threshold1', 'Params', 103, 255, empty)
  cv.createTrackbar('Threshold2', 'Params', 39, 255, empty)
  
  # Create function to generate contours
  cap = cv.VideoCapture(1)
  cv.namedWindow('Results', cv.WINDOW_NORMAL)
  
  while True:
      bool, img = cap.read()
      if cnn_test.generate_predictions(img, actual_label="Potato") == 1:
        imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
        thres1 = cv.getTrackbarPos('Threshold1', 'Params')
        thres2 = cv.getTrackbarPos('Threshold2', 'Params')
        imgCanny = cv.Canny(imgBlur, thres1, thres2)

        kernel = np.ones((5, 5))
        imgDil = cv.dilate(imgCanny, kernel, iterations=1)
        contours, _ = cv.findContours(imgDil, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        return img, contours



      


