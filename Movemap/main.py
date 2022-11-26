# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np

# Make an image 1455

#img = np.zeros((1455, 1925, 3), dtype=np.uint8)
img = cv2.imread('hyang01.png')

#shapes_master = np.zeros_like(img, np.uint8)
#img2 = np.zeros((1455, 1925, 3), dtype=np.uint8)

# colors for different objects
biker = (60, 60, 210)
pedestrian = (210, 60, 60)
cart = (60, 21, 60)
car = (190, 185, 60)
white_test = (255, 255, 255)

#kernel = np.ones((5, 5), np.float32)/25
#found = True


#open file
f = open("labels.txt", "r")
for i in range(12500): #12500
    img_cp = img.copy()
    for j in range(20): #20
        coordinates_str = f.readline()

        coordinates_str = coordinates_str.replace("(", "")
        coordinates_str = coordinates_str.replace(")", "")
        coordinates_str = coordinates_str.split()
        color_str = coordinates_str[0].replace(",", "").split(":")
        del color_str[0]

        x_min = int(coordinates_str[1].replace(",", ""))
        y_min = int(coordinates_str[2].replace(",", ""))
        x_max = int(coordinates_str[3].replace(",", ""))
        y_max = int(coordinates_str[4])
        x_center = int(((x_max - x_min)/2) + x_min)
        y_center = int(((y_max - y_min)/2) + y_min)
        if color_str[0] == 'Pedestrian':
            #continue
            cv2.circle(img_cp, [x_center, y_center], radius=5, color=pedestrian, thickness=-1)  # pedestrian
        elif color_str[0] == 'Biker':
            #continue
            cv2.circle(img_cp, [x_center, y_center], radius=5, color=biker, thickness=-1)  # biker

        elif color_str[0] == 'Cart':
            #continue
            cv2.circle(img_cp, [x_center, y_center], radius=5, color=cart, thickness=-1)  # cart
            #found = True

        elif color_str[0] == 'Car':
            #continue
            cv2.circle(img_cp, [x_center, y_center], radius=5, color=car, thickness=-1)  # car
            #found = True

        else:
            print("error line nr: %i", i)
            continue


        #img_cp = cv2.filter2D(img_cp, -1, kernel)
    #if found:
    img_cp = cv2.GaussianBlur(img_cp, (5, 5), 0)
        #found = False
    img_new = cv2.addWeighted(img_cp, 0.04, img, 1 - 0.04, 0)
    img = img_new.copy()

    # noe med img 1.....
    img = cv2.addWeighted(img, 0.1, img2, 0.1, 1.0)
    img2 = np.zeros((1455, 1925, 3), dtype=np.uint8)




#img = cv2.GaussianBlur(img, (3, 3), 0)
print(x_min)
print(y_min)
print(x_max)
print(y_max)

cv2.imwrite("heat_map.png", img)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#from vidstab.VidStab import VidStab
#stabilizer = VidStab()

#cap = cv2.VideoCapture('videos.mov')
#BackGround = cv2.bgsegm.createBackgroundSubtractorMOG()

#while True:
#    done,frame = cap.read()
#    fgmask = BackGround.apply(frame)

#    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame,
#                                                  smoothing_window=10)
#    if not done:
#        break
#    mainFrame = cv2.resize(frame, (1080, 700))
#    stabilized_frame = cv2.resize(fgmask, (1095, 800))

#    contours,h = cv2.findContours(stabilized_frame, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

#    for cnt in contours:
#        area = cv2.contourArea(cnt)
#        if area <25:
#            continue

#        x,y,w,h = cv2.boundingRect(cnt)
#        offset = 3
#        cv2.rectangle(mainFrame,(x-offset,y-offset),(x+w+offset,y+h+offset),(0,255,0),2)

#    cv2.imshow('mainFrame', mainFrame)
#    cv2.imshow('maskedFrame', stabilized_frame)


#    if cv2.waitKey(75) & 0xFF == ord('q'):
#        break
#cap.release()
#cv2.destroyAllWindows()

