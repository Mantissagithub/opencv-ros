import cv2 as cv
img = cv.imread('dima-kapralov-geTGVJsR6EA-unsplash.jpg')
# cv.imshow('Women', img)

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Women', rescaleFrame(img))
cv.waitKey(0)