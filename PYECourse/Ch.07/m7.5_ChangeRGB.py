# Ch.07.2.2 change RGB channel

from PIL import Image

im = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")
r, g, b = im.split()

om = Image.merge("RGB", (b, g, r))
om.save(".\\PYECourse\\Ch.07\\tedBGR.jpg")
