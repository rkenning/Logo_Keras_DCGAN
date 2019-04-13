import os
import sys
import numpy as np
from random import shuffle
from PIL import Image

def load_txt_files(txt_dir_path, extension):
    texts = []
    for f in os.listdir(txt_dir_path):
        filepath = os.path.join(txt_dir_path, f)
        if os.path.isfile(filepath) and f.endswith(extension):
            with open(filepath, 'r') as file:
                text = file.read().replace('\n', '')
            texts.append(text)
    return np.array(texts)


def main():
    seed = 40
    np.random.seed(seed)

    current_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(current_dir, '..'))
    current_dir = current_dir if current_dir is not '' else '.'


    txt_dir_path = current_dir + '/data/BathMLGen'
    model_dir_path = 'C:/ModelTemp/models'
    from dcgan_v3 import DCGanV3
    gan = DCGanV3()
    gan.load_model(model_dir_path)

    #load the text
    texts = load_txt_files(txt_dir_path,'txt')
    counter = 1

    for text in texts:
           generated_image = gan.generate_image_from_text(text)
           filename = current_dir + '/data/outputs/' + DCGanV3.model_name + '-generated-' + str(counter) + '.png'
           print("Writing :"+filename)
           generated_image.save(filename)
           im = Image.open(filename)
           resize = im.resize((600,600))
           filename = current_dir + '/data/outputs/' + DCGanV3.model_name + '-generated-' + str(counter) + '-big.png'
           resize.save(filename)
           counter += 1

if __name__ == '__main__':
    main()
