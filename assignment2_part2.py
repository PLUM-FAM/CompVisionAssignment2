import numpy
import cv2

#helper function to increase frame brightness
def increase_brightness(src, value):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    src = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return src


#capture camera and create windows
cap = cv2.VideoCapture(0)
cv2.namedWindow("normal",0)
#cv2.namedWindow("gray",0)
# cv2.namedWindow("threechannel",0)
# cv2.namedWindow("image1",0)
# cv2.namedWindow("absDiff",0)

status, img = cap.read()
average = numpy.float32(img)

#process each frame
while True:
        status, img = cap.read()
        
        threeChannel = numpy.float32(img/255)

        #brighten the image slightly
        result = increase_brightness(img,30)
        
        #5x5 mask blur image
        result = cv2.blur(result, (5,5))
        #result = cv2.GaussianBlur(result,(5,5),0)

        #accumulateWeighted (take running average)
        cv2.accumulateWeighted(result,average,0.1)
        result = cv2.convertScaleAbs(average)

        #take difference
        result = cv2.absdiff(result,img)
        
        #grayscale the image
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        #threshold the grayscale with low number
        # logan - best threshold 0, 100 
        ret1, result = cv2.threshold(result, 10,50, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #blur again
        result = cv2.blur(result,(5,5))
        #result = cv2.GaussianBlur(result,(5,5),0)

        
        #threshold again
        # Logan - best threshhold 120 - 255
        ret1, result = cv2.threshold(result, 200,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


        #erode and dialate to eliminate noise
        kernel = numpy.ones((5,5),numpy.uint8)
        #result = cv2.erode(result,kernel,iterations = 1)
        #result = cv2.dilate(result,kernel,iterations = 1)


        #contours
        contours = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        # print(len(contours))
        for c in contours:
                #logan best at 9000
            if(cv2.contourArea(c) > 5000):
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



        #cv2.drawContours(result, contours, -1, (0,255,0), 3)

       




        #refresh all windows
        cv2.imshow("normal", img)
        #cv2.imshow("grayscale",gray)
        cv2.imshow("img1",result)
        #cv2.imshow("absdiff", absdiff)
        #cv2.imshow("threechannel", threeChannel)


        #exit with escape key
        k = cv2.waitKey(1)
        if k == 27:
                break


cv2.destroyAllWindows()
print("windows closed")