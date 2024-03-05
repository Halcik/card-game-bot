import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import numpy as np


#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Card:
  star = cv2.imread("star.png", cv2.IMREAD_GRAYSCALE)
  n_cards = 0

  def __init__(self, image, n_stars, powers):
    self.image = image
    self.n_stars = n_stars
    self.powers = powers
    self.energy = 4
    self.position = None #do napisania, kolejność ułożenia (zmienia się potem)
    self.level = None #do napisania - czy złota, fioletowa, czy szara

  def __del__(self):
    del self.n_stars
    del self.powers
    del self.image
    del self.energy
    del self.position
    del self.level

  def __str__(self):
    return f'''Karta {self.image}:
    *Energia = {self.energy}
    *Moce = {self.powers}
    *Możliwości ulepszenia = {self.n_stars}'''

  @classmethod
  def get(cls, image):
    if 0<=Card.n_cards<6:
      image_read = cv2.imread(image)
      image_read = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
      powers = pyt.image_to_string(image_read).split()
      powers = "".join(powers)
      try:
        purple = powers[0]
        green = powers[2]
        blue = powers[4]
        red = powers[6]
        powers = [purple, green, blue, red]
      except:
        print(f"Pobranie mocy dla {image} nie powiodło się")
        
      res = cv2.matchTemplate(image_read, Card.star, cv2.TM_CCOEFF_NORMED)
      threshold = 0.8
      loc = np.where( res >= threshold)
      n_stars = len(loc[0])
      Card.n_cards+=1
      return cls(image, n_stars, powers)
    else:
      return "Nie udało się stworzyć"

card_one = Card.get("test.png")
print(card_one)

#===================================================
# tests = ["test.png", "test_blue.png", "test_gold.png", "test_gray.png", "test_violet.png"]

# star = cv2.imread("star.png", cv2.IMREAD_GRAYSCALE)

# for test in tests:
#   image = cv2.imread(test)
#   change_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#   powers = pyt.image_to_string(change_image).split()
#   powers = "".join(powers)

#   try:
#     purple = powers[0]
#     green = powers[2]
#     blue = powers[4]
#     red = powers[6]
#     print(f"test dla {test}:", purple, green, blue, red)
#   except:
#     print(f"Pobranie mocy dla {test} nie powiodło się")
    
#   w, h = star.shape[::-1]
#   res = cv2.matchTemplate(change_image, star, cv2.TM_CCOEFF_NORMED)
#   threshold = 0.8
#   loc = np.where( res >= threshold)
#   n_stars = len(loc[0]) #ilość gwiazdek do zwiększania poziomu
#   for pt in zip(*loc[::-1]):
#     cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#   cv2.imshow("change", image)
#   cv2.waitKey(0)

  


