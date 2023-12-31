import cv2
import matplotlib.pylab as plt
import numpy as np

def Region_of_Interest(img,vertices):
    mask = np.zeros_like(img)
    # ch_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

def Hough_Lines(img,lines):
    img = np.copy(img)
#     blank_img = np.zeros((img.shape[0],img.shape[1],3),dtype = np.uint8)
    blank_img = np.zeros_like(img)
    for line in lines :
        for x1,y1,x2,y2 in line:
            cv2.line(blank_img,(x1,y1),(x2,y2),(0,255,0),10)
    
    img = cv2.addWeighted(img,0.8,blank_img,1,1)
    return img

image = cv2.imread(r'C:\Users\AI\Downloads\test_image.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(image.shape)
h = image.shape[0]
w = image.shape[1] 
ROI_vertices = [(0,h),(w/2,h/2),(w,h)]

gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image,100,200)
ROI_image = Region_of_Interest(canny_image,np.array([ROI_vertices],np.int32))
lines = cv2.HoughLinesP(ROI_image,rho=6,theta=np.pi/180,threshold=160,lines= np.array([]),minLineLength=40,maxLineGap=50)
image_lines = Hough_Lines(image,lines)

plt.imshow(image_lines)
plt.show()