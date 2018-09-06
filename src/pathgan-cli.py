# (c) Copyright 2017 Marc Assens. All Rights Reserved.

import click
import predict as pathgan


__author__ = "Marc Assens"
__version__ = "0.1"

@click.command()
@click.option('--img_path', prompt="Path with folder Images containing the images (without \'/\' at the end)")
@click.option('--out_path', prompt="Path where the results will be saved (without \'/\' at the end)")

def predict(img_path, out_path):
    """ Predicts multiple images and saves them in .mat format
    on an output path
    
    \b
    example command:
        python pathgan-cli.py  --img_path /root/sharedfolder/Images --out_path /root/sharedfolder/predict_scanpaths/salient360_submission_code/output
        
        
        - On Marc's Computer - 
        python pathgan-cli.py  --img_path /Users/massens/Documents/playground/titan/salient360_submission_code/submission_evaluation/test_images --out_path /Users/massens/Documents/playground/pathgan/output/1_weights_with_time_at_0
    """


    print('\n\n###########################')
    print('Starting program')
    print(img_path)
    pathgan.predict_and_save(img_path, out_path)

if __name__ == '__main__':
    predict()
