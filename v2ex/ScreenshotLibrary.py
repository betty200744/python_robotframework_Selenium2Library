
import sys
from PIL import Image
from ImageCompare import FuzzyImageCompare
import selenium



def screenshotCompare(*args):
    if len(args) < 2:
        sys.exit()

    tot = len(args)
    tot = (tot ** 2 - tot) / 2

    print 'Comparing %d images:' % tot

    images = {}
    for img in args[0:]:
        images[img] = Image.open(img)

    results, i = {}, 1
    for namea, imga in images.items():
        for nameb, imgb in images.items():
            if namea == nameb or (nameb, namea) in results:
                continue

            print ' * %2d / %2d:' % (i, tot),
            print namea, nameb, '...',

            cmp = FuzzyImageCompare(imga, imgb)
            sim = cmp.similarity()
            results[(namea, nameb)] = sim

            print '%.2f %%' % sim
            i += 1

    res = max(results.values())
    if res > 80:
        return True
    else:
        return False


def crop_video_screenshot(screenshot, x , y, width, height):
    im = Image.open(screenshot)  # uses PIL library to open image in memory

    left = x
    top = y
    right = x + width
    bottom = y + height

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save(screenshot)  # saves new cropped image



