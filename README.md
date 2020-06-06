# Snippets
The goal of this project is to render an image with a math equation as LaTeX. The model is trained on over 100,000 images and formulas.

[The dataset can be downloaded here](https://zenodo.org/record/56198#.V2p0KTXT6eA).

## Quick Start

Download each file from the [im2latex-100k-dataset](https://zenodo.org/record/56198#.V2p0KTXT6eA) into a new folder `data/raw` inside the project. You do not need to expand `formula_images.tar.gz`. The script will parse through it.

Be sure to run all of the scripts from the root directory. The file paths are relative to the directory the script is run from.


### Preprocessing

If you want to skip the hassle of preprocessing, which takes computing time since the dataset is over 100,000 images, feel free to download [Harvard's preprocessed data](http://lstm.seas.harvard.edu/latex/data/). You will have to expand `formula_images_processed.tar.gz`. Their processed data may be better (I have not tested this method); it is different because their images are padded and data is filtered. I discovered this after I started preprocessing the raw data, which is honestly more fun. If you choose to use the Harvard processed data, you may want to write a quick python script using the `tarfile` package with 

```python
tar.extractall('data/preprocessed/formula_images_processed.tar.gz')
```


#### Images
Each image in the original dataset is a full A4 paper-sized image. This means that there is a lot of white space. The following script extracts `formula_images.tar.gz` into a temporary directory, and then uses threading to speed up the process of opening each image, cropping it, scaling it down, and saving it to a new folder. You can choose how many threads to create based on your computer specs.
```
python scripts/preprocessing/preprocess_images.py
```