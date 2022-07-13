# Ch.07.2.3 get image enhance contrast

from PIL import Image
from PIL import ImageEnhance

im = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")

om = ImageEnhance.Contrast(im)
om.enhance(20).save(".\\PYECourse\\Ch.07\\tedEnContrast.jpg")
