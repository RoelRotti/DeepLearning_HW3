
from PIL import Image
import glob

# save image to file with correct label
def sort_images(path, tr_tst):
    for i in range(0,10,1):
        files = glob.glob(path + str(i) +"/*.png")
        for filename in files: #assuming gif
            im=Image.open(filename)
            if im.size == (32,32):
                print(im.size)
                im.save('32x32/'+filename)
            elif im.size == (48,48):
                im.save('48x48/'+filename)
            elif im.size == (64,64):
                im.save('64x64/'+filename)
            im.close()

trainPath = ("mnist-varres/train/")
sort_images(trainPath, 'train')
testPath = ("mnist-varres/test/")
sort_images(testPath, 'test')

