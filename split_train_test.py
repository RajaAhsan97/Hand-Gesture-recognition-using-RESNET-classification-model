"""
    Code to split images into train and test images by random shuffling
"""

import os
import random
from PIL import Image

base_dir = 'Sign Language for Alphabets'

os.mkdir('train')
os.mkdir('test')
os.mkdir('valid')

# iterate over all cattle tags
for cattle in os.listdir(base_dir):
    path = os.path.join(base_dir, cattle)

    cattle_images = os.listdir(path)
    random.shuffle(cattle_images)

    count = 0     # counter to put 2 images into test folder and remaining images in training folder
    # iterate over all images of cattle
    for img in cattle_images:
        image = Image.open(os.path.join(path, img))

        test_cattle_fldr = os.path.join('test', cattle)
        train_cattle_fldr = os.path.join('train', cattle)
        valid_cattle_fldr = os.path.join('valid', cattle)
        
        # create cattle label in test folder
        if not os.path.exists(test_cattle_fldr):
            os.mkdir(test_cattle_fldr)
        # create cattle label in train folder
        if not os.path.exists(train_cattle_fldr):
            os.mkdir(train_cattle_fldr)
        if not os.path.exists(valid_cattle_fldr):
            os.mkdir(valid_cattle_fldr)

        # save 2 images in test folder
        if count > 0 and count <= 50: 
            image.save(os.path.join(test_cattle_fldr, img))
        elif count > 50 and count <=100:
            image.save(os.path.join(valid_cattle_fldr, img))
        else:   # save remaining images in train folder
            image.save(os.path.join(train_cattle_fldr, img))

        count+=1
