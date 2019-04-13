# keras-text-to-image to generate Bath ML Meetup Logo

Text to Image using GloVe and Word2Vec with Generative Adversarial Network Models in Keras

Thanks to : Xianshun Chen where his original project generating Pokomons provided the bases for my development
Original Project - https://github.com/chen0040/keras-text-to-image'


I have streamlined the original project and picked one method of generating the model with keras

# Usage

* Training Image files should be placed in /data/train_images
* Training Text files should be placed in /data/train_text
* Execute dcgan_v3_train_BathML.py (Highly recomend using a GPU tensorflow install detailed below)
* Text to be used for generation should be placed in the location /data/generate_text (Separate text files will generate separate images)
* Execute dcgan_v3_generate_BathML.py (This doesn't require a GPU tensorflow install) & generated images should be written to the location /data/generated_images


# Configure to run on GPU on Windows

* Step 1: Change tensorflow to tensorflow-gpu in requirements.txt and install tensorflow-gpu
* Step 2: Download and install the [CUDA® Toolkit 9.0](https://developer.nvidia.com/cuda-90-download-archive) (Please note that
currently CUDA® Toolkit 9.1 is not yet supported by tensorflow, therefore you should download CUDA® Toolkit 9.0)
* Step 3: Download and unzip the [cuDNN 7.4 for CUDA@ Toolkit 9.0](https://developer.nvidia.com/cudnn) and add the
bin folder of the unzipped directory to the $PATH of your Windows environment 
