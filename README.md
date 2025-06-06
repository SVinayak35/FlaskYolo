# FlaskYolo
This Flask application uses a trained YOLOv8m model to detect and count the number of people in an image. 
## Training
The model was trained on a Roboflow dataset (https://universe.roboflow.com/daniel-morantha-yt377/peoplecounting-o5wzh) of about 1900 images.

The Training results are available here : https://drive.google.com/drive/folders/1CbPxXoI3WnOy-wVxIQ1VywzIImZGgCtB?usp=sharing

Due to limited GPU capabilities on local computer, the training was done on Google Colab (https://colab.research.google.com/drive/1JB1i7AXHMYX7b9HEZEfsRgoYACMKXf1F?usp=sharing)

## How to run

To run the Flask app on your computer, use the following in your command prompt/terminal :

> curl -X POST -F image=@YOUR_IMAGE_PATH_HERE.jpg https://8744-2405-201-4020-d866-47c-599c-5b7e-9e21.ngrok-free.app/count

 Replace YOUR_IMAGE_PATH_HERE with the image which you wish to use.
 
