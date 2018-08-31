from images import Image

def blackandWhite(Image):
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    #
    for y in range(Image.getHeight()):
        for x in range (Image.getWidth()):
            (r, g, b) = Image.getPixel(x, y)
            average = (r + g + b) // 3
            #
            if average < 128:
                Image.setPixel(x, y, blackPixel)
            else:
                Image.setPixel(x, y, whitePixel)

def main(filename = "bdbh.gif"):
    image = Image(filename)
    image.draw()
    #
    blackandWhite(image)
    #
    image.draw()

if __name__ == "__main__":
    main()

