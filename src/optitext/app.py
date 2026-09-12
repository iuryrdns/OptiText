import cv2 as cv
import pytesseract
from PIL import Image

img_path = "data/raw/test.png"

## img = Image.open(img_path) - com Pillow
img = cv.imread(img_path)




def main():
    print(img.size)
    img.save(format="PNG", fp="data/process/test.png", )


if __name__ == '__main__':
    main()