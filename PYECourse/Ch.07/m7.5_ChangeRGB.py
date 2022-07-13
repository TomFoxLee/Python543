# Ch.07.2.2 change RGB channel

from PIL import Image

im = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")

print(im.format, im.size, im.mode)

im1 = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")
im1.thumbnail((96, 96))
im1.save(".\\PYECourse\\Ch.07\\tedTN.jpg", "JPEG")

im2 = Image.open(".\\PYECourse\\Ch.07\\ted.jpg")
r, g, b = im2.split()

om2a = Image.merge("RGB", (b, g, r))
om2a.save(".\\PYECourse\\Ch.07\\tedBGR.jpg")

newg = g.point(lambda i: i * 0.9)
newb = b.point(lambda i: i < 100)
om2b = Image.merge(im2.mode, (r, newg, newb))
om2b.save(".\\PYECourse\\Ch.07\\tedMERGE.jpg")
