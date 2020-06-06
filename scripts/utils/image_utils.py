import numpy as np
from PIL.Image import LANCZOS

# images in dataset is A4 sized
# so there is a lot of white space
# if we crop the image to a preset size, all images
def crop_image(image, default_size=None):
  image_data = np.asarray(image, dtype=np.uint8) # Unsigned integer (0 to 255)

  # since the entire image is nearly white, we want anything that is not white
  # non-zero index
  nnz_idx = np.where(image_data!=255)

  if len(nnz_idx[0]) == 0: # if top-left is not white, then we can crop from top-left (essentially resizes)
    # check if default size is given as a parameter
    if not default_size:
      return raw_image
    else:
      assert len(default_size) == 2, default_size
      x_min, y_min, x_max, y_max = 0, 0, default_size[0], default_size[1]
      cropped_image = image.crop((x_min, y_min, x_max+1, y_max+1))
      return cropped_image

  # if there is white space, then crop by adjusting inital crop point
  y_min = np.min(nnz_idx[0])
  y_max = np.max(nnz_idx[0])
  x_min = np.min(nnz_idx[1])
  x_max = np.max(nnz_idx[1])
  cropped_image = image.crop((x_min, y_min, x_max+1, y_max+1))
  return cropped_image


# scale down image
def downsample_image(image, ratio=2):
  assert ratio >= 1, ratio
  if ratio == 1:
    return image

  size = np.array(image.size)/ratio # downsample ratio
  image.thumbnail(size=size, resample=LANCZOS) # resampling filter returns highest quality for downscaling, tradeoff is not great performance
  return image


