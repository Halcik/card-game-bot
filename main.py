from PIL import Image, ImageFilter
import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki
import pyautogui as pg

#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#===================================================

image = Image.open("test.png")
change_image = image.copy()
change_image= change_image.convert("L") #szaro-białe, to są tryby, jest też CMYK i RGB (każda literka osobno)
change_image.save("change.png")
powers = pyt.image_to_string(Image.open('change.png'), lang="pol").split()
print(powers)

purple = powers[0][0]
green = powers[0][2]
blue = powers[0][4]
red = powers[0][6]
print(purple, green, blue, red)

#====================================================

