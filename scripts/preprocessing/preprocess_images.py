import os, tarfile, tempfile, glob, sys
from PIL import Image
from multiprocessing.dummy import Pool as ThreadPool
# Use ThreadPool instead of Pool because the problem is IO (input/output, reading, writing, saving) bound and not CPU bound

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../utils/'))
from image_utils import *
from utils import Timer

data_dir = 'data/'
processed_images_dir = os.path.join(data_dir,'processed','formula_images')
if not os.path.isdir(processed_images_dir):
  os.makedirs(processed_images_dir)
timer = Timer()

def preprocess_image(image_path):
  image = Image.open(image_path).convert('L') # Convert to 8-bit pixels, black and white
  image = crop_image(image, default_size=[600,60])
  image = downsample_image(image, ratio=2)

  image.save(os.path.join(processed_images_dir,os.path.basename(image_path)))


def main():
  with tempfile.TemporaryDirectory() as temp_dir:
    with tarfile.open(os.path.join(data_dir,'raw','formula_images.tar.gz')) as tar:
      tar.extractall(temp_dir)
      print(f"Extracted gzip into temporary directory in {timer.elapsed_time()}",end="\n\n\n")

    image_paths = glob.glob(os.path.join(temp_dir,"formula_images/*.png"))
    pool = ThreadPool(4)
    pool.map(preprocess_image, image_paths)
    pool.close()
    pool.join()
    print(f"Completed image preprocessing in {timer.elapsed_time()}.",end="\n\n\n")
    # i, percent = 0, 0
    # for image_path in image_paths:
    #   image = Image.open(image_path).convert('L') # Convert to 8-bit pixels, black and white
    #   image = crop_image(image, default_size=[600,60])
    #   image = downsample_image(image, ratio=2)

    #   processed_images_dir = os.path.join(data_dir,'processed','formula_images')
    #   if not os.path.isdir(processed_images_dir):
    #     os.makedirs(processed_images_dir)
    #   image.save(os.path.join(processed_images_dir,os.path.basename(image_path)))

    #   if i % (len(images) / 10) == 0:
    #     percent+=10
    #     print(f"{percent}% done! {i} images preprocessed so far! {timer.elapsed_time()} elapsed.",end="\n\n\n")
    #   i+=1


if __name__ == '__main__':
  main()