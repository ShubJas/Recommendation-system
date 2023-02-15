# Recommendation-system using emotion detection
download FER2013 dataset
https://www.kaggle.com/msambare/fer2013
In the same folder, create a new folder named data and save the test and train folders in it.



Packages need to be installed
pip install numpy
pip install opencv-python
pip install keras
pip3 install tensorflow
pip install pillow


To train Emotion detector model
Run TrainEmotionDetector.py
After Training , you will find the trained model structure and weights are stored in your project directory. emotion_model.json emotion_model.h5
copy these two files, create model folder in your project directory and paste it.

To run your emotion detection file
Run TestEmotionDetector.py
You can either take your live camera feed or paste the path of the video by commenting the other out.

To analyse the model
Run EvaluateEmotionDetector.py

Music recom system to be added
