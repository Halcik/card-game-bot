import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import numpy as np


#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#===================================================
tests = ["test.png", "test_blue.png", "test_gold.png", "test_gray.png", "test_violet.png"]

star = cv2.imread("star.png", cv2.IMREAD_GRAYSCALE)

for test in tests:
  image = cv2.imread(test)
  change_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  powers = pyt.image_to_string(change_image, lang="pol+eng").split()

  try: #nie działa dla wszystkich :/
    purple = powers[0][0]
    green = powers[0][2]
    blue = powers[0][4]
    red = powers[0][6]
    print(purple, green, blue, red)
  except:
    pass
  w, h = star.shape[::-1]
  res = cv2.matchTemplate(change_image, star, cv2.TM_CCOEFF_NORMED)
  threshold = 0.8
  loc = np.where( res >= threshold)
  for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
  cv2.imshow("change", image)
  cv2.waitKey(0)

  


