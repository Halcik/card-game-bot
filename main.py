import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import numpy as np
import weakref


#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Card:
  star = cv2.imread("star.png", cv2.IMREAD_GRAYSCALE)
  n_cards = 0
  positions = []

  def __init__(self, image):
    Card.n_cards+=1
    self.image_read = self.change_image(image)
    self.n_stars = self.get_stars(self.image_read)
    self.powers = self.get_powers(self.image_read)
    self.energy = 4
    self.level = self.set_level()
    Card.positions.append(weakref.ref(self))
    self.position = self.set_position()


  def __del__(self):
    del self.n_stars
    del self.powers
    del self.image_read
    del self.energy
    del self.level
    del self.position  
    if weakref.ref(self) in Card.positions:
      print("Byłem w liście")
      Card.positions.remove(weakref.ref(self))
    Card.n_cards-=1
    

  def __str__(self):
    return f'''Karta {self.position}:
    *Energia = {self.energy}
    *Moce = {self.powers}
    *Możliwości ulepszenia = {self.n_stars}
    *Level = {self.level}'''
  

  def change_image(self, image):
    image_read = cv2.imread(image)
    image_read = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
    return image_read


  def set_level(self):
    match self.n_stars:
      case 4: #violet
        level = 4
      case 3: #gold
        level = 3
      case 2: #blue
        level = 2
      case 1: #gray
        level = 1
    return level
  

  def get_stars(self, image_read):
    res = cv2.matchTemplate(image_read, Card.star, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    n_stars = len(loc[0])
    return n_stars
  
  def set_position(self):
    ...


  def get_powers(self, image_read):
    powers = pyt.image_to_string(image_read).split()
    powers = "".join(powers)
    try:
      purple = powers[0]
      green = powers[2]
      blue = powers[4]
      red = powers[6]
      powers = [purple, green, blue, red]
      return powers
    except:
      print(f"Pobranie mocy nie powiodło się")
      return 0


  @classmethod
  def get(cls, image):
    if 0<=Card.n_cards<6:
        return cls(image)
    return "Nie udało się stworzyć karty"
        

if __name__ =='__main__':
  card_one = Card.get("test.png")
  card_two = Card.get("test.png")
  card_three = Card.get("test.png")
  card_four = Card.get("test_gold.png")
  print(card_one.powers)
  print(Card.positions[0].__call__().powers)
