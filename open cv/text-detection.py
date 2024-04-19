import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

img_path = 'denise-jans-laoBHO09sU0-unsplash.jpg'

img = cv.imread(img_path)

reader = easyocr.Reader(['en'], gpu=False)

text = reader.readtext(img)

threshold = 0.25

for t in text:
    print(t)

    bbox, text, score = t

    cv.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
    cv.putText(img, text, bbox[0], cv.FONT_HERSHEY_COMPLEX, 1.5, (255,0,0) ,2)

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()