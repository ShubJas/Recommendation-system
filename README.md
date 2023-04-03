# Music Recommendation-system using emotion detection
download FER2013 dataset
<br />https://www.kaggle.com/msambare/fer2013
<br />In the same folder, create a new folder named data and save the test and train folders in it.



### Packages need to be installed
numpy
<br />opencv-python
<br />keras
<br />tensorflow
<br />pillow
<br />


- Run <code>pip install -r requirements.txt</code> to install all dependencies.


### To train Emotion detector model
Run Train.py

After Training , you will find the trained model structure and weights are stored in your project directory. emotion_model.json and emotion_model.h5
<br />copy these two files, create model folder in your project directory and paste it.

### To run your emotion detection file
Run detect_emotion.py
<br />You can either take your live camera feed or paste the path of the video by commenting the code other out in Test.py 

### To analyse the model
Run evaluate.py

### To run the webapp
Run app.py and visit the link that appears in the Terminal
