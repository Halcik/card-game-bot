from PIL import Image
import pytesseract as pyt #from installer (for windows) https://github.com/UB-Mannheim/tesseract/wiki

#langCodes - https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(pyt.image_to_string(Image.open('test.png'), lang="pol+eng"))