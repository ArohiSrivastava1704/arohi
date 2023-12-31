import cv2    # Importing libraries
import numpy as np
import matplotlib.pyplot as plt




def GrayImage(Image):        # Converting Image to grayscale
    grayImage = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    return grayImage

def Blur(Image):         #Reducing noise and smoothing it for detect edges
    blurImage = cv2.GaussianBlur(Image,(5,5),0)
    return blurImage

def  Canny(Image):
    cannyImage = cv2.Canny(Image,50,150)
    return cannyImage

def RegionOfInterest(Image):
    height = Image.shape[0]
    vertices = np.array([[(200,height),(1100,height),(550,250)]],np.int64)   #Triangular area is ROI
    mask = np.zeros_like(Image)
    cv2.fillPoly(mask,vertices,255)
    masked_image = cv2.bitwise_and(Image,mask)  #Merging masked image into Original Image
    return masked_image
    
def HoughLine(Image,lines):
    # blank_image = np.zeros((Image.shape[0],Image.shape[1],3),dtype = np.uint8)
    blank_image = np.zeros_like(Image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),10)
    
    Hough_Image = cv2.addWeighted(Image,.8,blank_image,1,0)
    return Hough_Image
        


cap = cv2.VideoCapture(r"C:\Users\AI\Downloads\test2.mp4")
while cap.isOpened():
    ret,frame = cap.read()
    gray_image = GrayImage(frame)
    blur_image = Blur(gray_image)
    canny_image = Canny(blur_image)
    cropped_image = RegionOfInterest(canny_image)
    lines = cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=20)
    Hough_Image = HoughLine(frame,lines)
    cv2.imshow("Result",Hough_Image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()