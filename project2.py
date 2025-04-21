import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
# cap = cv.VideoCapture(0) 
# while True:
#  ret, frame =cap.read()  
#  cv.imshow("Frame", frame)
#  cv.waitKey(1)

#reading image 

# img= cv.imread('photos/one.png')
# cv.imshow('one',img)
# cv.waitKey(0)

#reading videos

# capture=cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame=capture.read()
    
#     cv.imshow('Video',frame)
#     if cv.waitKey(10) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# img= cv.imread('photos/one.png')
# cv.imshow('one',img)

# def rescaleFrame(frame, scale=0.75):
    
#    width = int(frame.shape[1]* scale)
#    height =int(frame.shape[0]* scale)
#    dimensions= (width,height)
#    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 
# capture=cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame=capture.read()
    
#     frame_resized = rescaleFrame(frame, scale=.5)
    
#     cv.imshow('Video',frame)
#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(10) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

# blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)
# blank[:]=0,0,255
# cv.imshow('red',blank)
# cv.waitKey(0)
# cv.putText(blank,'hello',(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
# cv.imshow('Text',blank)

# cv.waitKey(0)    

# img= cv.imread('photos/one.png')
# cv.imshow('one',img)
#grayscaling
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)


#edgevcascade
# canny= cv.Canny(img,125,175)
# cv.imshow('Canny Edges',canny)
# cv.waitKey(0)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# #bgr to hssv
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# #bgr to l*a*b
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)


# img= cv.imread('photos/two.jpg')
# cv.imshow('two',img)
# b,g,r= cv.split(img)

# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# img= cv.imread('photos/two.jpg')
# cv.imshow('two',img)
# blank=np.zeroes((400,400),dtype='uint8')
# rectangle=cv.rectangle(blank.copy(),(30,30)(370,370),255,-1)
# circle=cv.circle(blank.copy(),(200,200),200,255,-1)
# cv.imshow('Rectangle',rectangle)
# cv.imshow('Circke',circle)

#histogram
# img= cv.imread('photos/two.jpg')
# cv.imshow('two',img)

# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# gray_hist= cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Hitogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
# cv.waitKey(0)

# img=cv.imread('photos/one.png')
# cv.imshow('cats',img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
# cv.imshow('threwshodl',thresh)

# cv.waitKey(0)

# img= cv.imread('photos/sahil.JPG')
# cv.imshow('person',img)
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAy',gray)
# haar_cascade=cv.CascadeClassifier('haar_face.xml')

# faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=1)

# print(f'the number of faces found ={len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
#     cv.imshow('Detected faces',img)
# cv.waitKey(0)  

