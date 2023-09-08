from PIL import Image
from pytesseract import pytesseract


path = "image.png"
image = Image.open(path)
text = pytesseract.image_to_string(image)
print(text)
