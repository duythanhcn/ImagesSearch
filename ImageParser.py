from searchEngine.ImageFeature import ImageFeature
import glob
import cv2


class ImageParser:
    def __init__(self):
        print('init')

    def parseImage(self, image):
        imf = ImageFeature((8, 12, 3)) 
        features = imf.exactFeature(image)
        return features

    def readImage(self, imgPath):
        return cv2.imread(imgPath)

    def parseDataset(self):
        output = open("dataset.csv", "w")
        for imagePath in glob.glob("dataset" + "/*.jpg"):
            imageID = imagePath[imagePath.rfind("/") + 1:]
            image = self.readImage(imagePath)
            features = self.parseImage(image)
            features = [str(f) for f in features]
            output.write("%s,%s\n" % (imageID, ",".join(features)))
            print(imageID)
            
        print('finshed parse dataset')
        output.close()
