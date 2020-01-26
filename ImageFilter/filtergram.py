
import filters

def main():
    filename = input("Enter the name of the image file to edit: ")

    img = filters.load_img(filename)

    obamicon_image = filters.obamicon(img)

    filters.save_img(obamicon_image, "recolored.jpg")

    grayscale_image = filters.grayscale(img)

    filters.save_img(grayscale_image, "grayscale.jpg")

    inverted_image = filters.invert(img)

    filters.save_img(inverted_image, "inverted.jpg")

    bluescale_image = filters.blue_recolor(img)

    filters.save_img(bluescale_image, "blue_recolor.jpg")

if __name__ == "__main__":
    main()
