import cv2
import numpy

class CVModule:

    image_dimensions = (480, 360)

    def __init__(self, args):
        pass

    def output_dimensions(self):
  	     return self.image_dimensions

     def process_image(self, img):
         img = cv2.resize(img, self.image_dimensions)

         edges = cv2.Canny(img, 100, 200)

    def main():
        pass

if __name__ == "__main__":
    CVModule.main()
