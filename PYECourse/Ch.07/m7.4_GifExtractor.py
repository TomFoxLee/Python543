# Ch.07.2.2 Extract frame from .gif file

from PIL import Image

im = Image.open(".\\PYECourse\\Ch.07\\bunnychew.gif")

try:
    im.save(".\\PYECourse\\Ch.07\\picframe{:02d}.png".format(im.tell()))
    while True:
        im.seek(im.tell() + 1)
        im.save(".\\PYECourse\\Ch.07\\picframe{:02d}.png".format(im.tell()))

except:
    print("Process End.")
