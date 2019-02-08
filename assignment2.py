import cv2

def onClick(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX,mouseY = x,y
        print("mouse is at " , x, y)

        #still not working properly!------------
        #print(hsv[x,y])

#adjust mins
def adjust_hue_MIN(value):
    print("adjustHue")

def adjust_sat_MIN(value):
    print("adjustSaturation")

def adjust_val_MIN(value):
    print("adjust value")

#adjust maxs
def adjust_hue_MAX(value):
    print("adjustHue")

def adjust_sat_MAX(value):
    print("adjustSaturation")

def adjust_val_MAX(value):
    print("adjust value")





cap = cv2.VideoCapture(0)
cv2.namedWindow("hsv",0)
cv2.namedWindow("Video",0)



while True:
    status, img = cap.read()
    cv2.imshow("Video", img)

    #convert img to HSV and save to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #creating max sliders on hsv window
    cv2.createTrackbar('Hue MIN','hsv',0,180,adjust_hue_MIN)
    cv2.createTrackbar('Sat MIN','hsv',0,255,adjust_sat_MIN)
    cv2.createTrackbar('Val MIN','hsv',0,255,adjust_val_MIN)
    #creating min sliders on hsv window
    cv2.createTrackbar('Hue MAX','hsv',0,180,adjust_hue_MAX)
    cv2.createTrackbar('Sat MAX','hsv',0,255,adjust_sat_MAX)
    cv2.createTrackbar('Val MAX','hsv',0,255,adjust_val_MAX)



    #display hsv window
    cv2.imshow("hsv", hsv);

    #on click on hsv window, call onClick function
    cv2.setMouseCallback('hsv',onClick)

    k = cv2.waitKey(1)
    if k == 27:
        break

    

cv2.destroyAllWindows()
print("windows closed")



