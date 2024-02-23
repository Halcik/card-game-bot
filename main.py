import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import numpy as np


#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#===================================================

image = cv2.imread("test.png")
change_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", change_image)
#cv2.waitKey(0)

powers = pyt.image_to_string(change_image, lang="pol+eng").split()

purple = powers[0][0]
green = powers[0][2]
blue = powers[0][4]
red = powers[0][6]
print(purple, green, blue, red)

#====================================================
star = cv2.imread("star.png")
star = cv2.cvtColor(star, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", star)
# cv2.waitKey(0)

height, width = change_image.shape
H, W = star.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF] 

for method in methods:
   change_image2 = change_image.copy()
   result = cv2.matchTemplate(change_image2, star, method)
   min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
   print(min_loc, max_loc)
   if method in [cv2.TM_SQDIFF,cv2.TM_CCORR]:
     lacation = min_loc
   else:
     location = max_loc
   bottom_right = (location[0] + W, location[1] + H)
   cv2.rectangle(change_image2, location,bottom_right, 255, 5)
   
   cv2.imshow("change", change_image2)
   cv2.waitKey(0)
   cv2.destroyAllWindows() 


