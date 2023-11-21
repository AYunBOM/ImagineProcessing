import cv2

height = int(input('높이 : '))
width = int(input('너비 : '))

title = "ex11 - mainWindow"
cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        result, image = cap.read()
        img_height = 230
        img_width = 320
        roi_height = int((height-img_height)/2)
        roi_width = int((width - img_width) / 2)
        blue, red = (255, 0, 0), (0, 0, 255)
        image[0:roi_height ,0:width] = blue
        image[roi_height+img_height:height, 0:width] = blue
        image[0:height, 0:roi_width] = blue
        image[0:height, roi_width+img_width:width] = blue
        image[roi_height:roi_height+2, roi_width:roi_width+img_width] = red
        image[roi_height+img_height:roi_height+img_height+2, roi_width:roi_width+img_width] = red
        image[roi_height:roi_height+img_height, roi_width:roi_width+2] = red
        image[roi_height:roi_height+img_height, roi_width+img_width:roi_width+img_width+2] = red

        if result:
            cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(title, image)
            cv2.resizeWindow(title, height, width)
            cv2.waitKey(33)
        else:
            break
else:
    print('cannot open the file')

cap.release()
cv2.destroyAllWindows()


