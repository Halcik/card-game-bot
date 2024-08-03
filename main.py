import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import numpy as np
import weakref
import pyautogui as pg


#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Card:
  star = cv2.imread("star.png", cv2.IMREAD_GRAYSCALE)
  n_cards = 0
  positions = []

  def __init__(self, image=None):
    Card.n_cards+=1
    if image is None:
      image = self.take_screenshoot()
    self.image_read = self.change_image(image)
    self.n_stars = self.get_stars(self.image_read)
    print("Gwiazdki:", self.n_stars)
    self.powers = self.get_powers(self.image_read)
    print("Moce:", self.powers)
    self.energy = 4
    self.level = self.set_level() # probably to be removed
    Card.positions.append(weakref.ref(self))
    self.n_card = Card.n_cards
    self.position = self.set_position()


  def __del__(self):
    del self.n_stars
    del self.powers
    del self.image_read
    del self.energy
    del self.level # probably to be removed
    del self.position
    del self.n_card  
    if weakref.ref(self) in Card.positions:
      Card.positions.remove(weakref.ref(self))
    

  def __str__(self):
    return f'''Karta {self.position}:
    *Energia = {self.energy}
    *Moce = {self.powers}
    *Możliwości ulepszenia = {self.n_stars}
    *Level = {self.level}'''


  def take_screenshoot(self): 
    screenshot = pg.screenshot()
    screenshot.save('screen.png')
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


  def change_image(self, image):
    image_read = cv2.imread(image)
    image_read = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
    return image_read


  def set_level(self): # probably to be removed
    match self.n_stars:
      case 4: #violet
        level = 4
      case 3: #gold
        level = 3
      case 2: #blue
        level = 2
      case 1: #gray
        level = 1
      case _:
        level = 1
    return level
  

  def get_stars(self, image_read): #dodać skalowanie - jeśli w danym skalowaniu wykryje jakąś gwiazdkę, to break
    res = cv2.matchTemplate(image_read, Card.star, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    n_stars = len(loc[0])
    return n_stars
  

  def set_position(self):
    position = Card.positions.index(weakref.ref(self))
    if len(Card.positions)<=3:
      return position
    
    while position>=0:
      if self.powers[4] < Card.positions[position-1].__call__().powers[4] or position==0:
        return position
      
      if self.powers[4] == Card.positions[position-1].__call__().powers[4] and self.n_card < Card.positions[position-1].__call__().n_card:
        return position
      
      temp_card = Card.positions[position-1]
      Card.positions[position-1] = weakref.ref(self)
      Card.positions[position] = temp_card
      Card.positions[position].__call__().position+=1
      position-=1


  def get_powers(self, image_read):
    powers = pyt.image_to_string(image_read).split()
    powers = "".join(powers)
    try:
      purple = int(powers[0])
      green = int(powers[2])
      blue = int(powers[4])
      red = int(powers[6])
      powers = [purple, green, blue, red, purple+green+blue+red]
      return powers
    except:
      print(f"Pobranie mocy nie powiodło się")
      return 0
    

  def use(self):
    if self.energy>=1:
      self.energy-=1
    print("Nie można użyć karty")


  def update_stars(self):
    if self.n_stars>0:
      self.n_stars-=1


  @classmethod
  def get(cls, image=None):
    if 0<=len(cls.positions)<6:
        return cls(image)
    return "Nie udało się stworzyć karty"
  
  @classmethod
  def sum_of_powers(cls, power=4):
    sum = 0
    for card in cls.positions:
      sum += card.__call__().powers[power]
    return sum
  
  @classmethod
  def delete_weak_card(cls): #didn't work
    weak_card_ref = cls.positions[-1]
    cls.positions.remove(weak_card_ref)
  

if __name__ =='__main__':
  card_one = Card.get("test.png")
  #card_one = Card.get("card_0.png")