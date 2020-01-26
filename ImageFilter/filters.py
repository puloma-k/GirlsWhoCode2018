# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
# Parameters: The name of the file to be opened (string)
# Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im

# Define your show_img() function here.
# Parameters: The image object to display.
# Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
# Parameters: The image object to save, the name to save the file as (string)
# Returns: nothing.
def save_img(im, filename):
    im.save(filename)
    show_img(im)

# Define your obamicon() function here.
# Parameters: The image object to apply the filter to.
# Returns: A New Image object with the filter applied.
def obamicon(im):
    pixels = im.getdata()
    new_pixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] +pixel[2]

        if intensity < 182:
            new_pixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)
        elif intensity >= 546:
            new_pixels.append(yellow)

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image

def grayscale(im):
    pixels = im.getdata()
    new_pixels = []

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] +pixel[2]
        average = int(intensity / 3)

        average_RGB = (average, average, average)

        new_pixels.append(average_RGB)

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image

def invert(im):
    pixels = im.getdata()
    new_pixels = []

    for pixel in pixels:
        inverted_R = 255 - pixel[0]
        inverted_G = 255 - pixel[1]
        inverted_B = 255 - pixel[2]

        inverted_RGB = (inverted_R, inverted_G, inverted_B)

        new_pixels.append(inverted_RGB)

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image

def blue_recolor(im):
    pixels = im.getdata()
    new_pixels = []

    darkBlue = (0, 51, 76)
    medBlue = (75, 156, 180)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] +pixel[2]

        if intensity < 200:
            new_pixels.append(darkBlue)
        elif intensity >= 200 and intensity < 300:
            new_pixels.append(medBlue)
        elif intensity >= 300 and intensity < 400:
            new_pixels.append(lightBlue)
        elif intensity >= 400:
            new_pixels.append(yellow)

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image
