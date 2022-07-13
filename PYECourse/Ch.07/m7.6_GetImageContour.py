# Ch.07.2.3 get image contour

from PIL import Image
from PIL import ImageFilter

im = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")

om = im.filter(ImageFilter.CONTOUR)
om.save(".\\PYECourse\\Ch.07\\tedCountor.jpg")
