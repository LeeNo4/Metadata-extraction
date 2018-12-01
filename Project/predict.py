import numpy as np
import pandas as pd
import datetime as dt
from mpl_toolkits.axes_grid1 import ImageGrid
import os
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from keras.applications.vgg16 import preprocess_input, decode_predictions
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import glob

start = dt.datetime.now()

INPUT_SIZE = 224
NUM_CLASSES = 16
SEED = 1987
data_dir = '../input/dog-breed-identification'
rootdir = 'imagedata'
list1 = os.listdir(rootdir)
address = ['Pekinese', 'Blenheim_spaniel', 'basset', 'Japanese_spaniel', 'chihuaua', 'Maltese', 'chow', 'toy_terrier', 'bluetick', 'redbone']
dir = rootdir+'/'+address[0]
lista = os.listdir(dir)

def read_img(path, train_or_test, size):
    img = image.load_img(path, target_size=size)
    img = image.img_to_array(img)
    return img

model = ResNet50(weights='imagenet')
j = int(np.sqrt(NUM_CLASSES))
i = int(np.ceil(1. * NUM_CLASSES / j))
fig = plt.figure(1, figsize=(16, 16))
grid = ImageGrid(fig, 111, nrows_ncols=(i, j), axes_pad=0.05)
for i in range(len(lista)):

    if 'metadata' in lista[i]:
        continue
    path = os.path.join(dir, lista[i])

    ax = grid[i]
    try:
        img = read_img(path, 'train', (224, 224))
    except IOError,OSError:
        continue

    ax.imshow(img / 255.)
    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    preds = model.predict(x)
    _, imagenet_class_name, prob = decode_predictions(preds, top=1)[0][0]
    ax.text(10, 180, ' %s (%.2f)' % (imagenet_class_name , prob), color='w', backgroundcolor='k', alpha=0.8)
    ax.axis('off')
    print(path,imagenet_class_name)
plt.show()