# CS3-DS4002
# Documentation Map

DATA Folder:
Includes all required data needed for the case study, with the scripts to clean the original downloaded dataset

SCRIPTS Folder:
Includes all required scripts notebooks with code needed for case study.

ARTICLES Folder:
Includes all supplemental reading for further information into the case study's code and topic.

Hook Document & Rubric
The hook document includes relevant background information regarding the case study topic and objectives.
The Rubric includes assignment details required to meet specifications.

# Software and Platform

All coding was done in Python in Jupyter Notebooks and Google Colab using Windows 10 software. 
The required packages and add-ons include: Pandas, Numpy, matplotlib, tensorflow, keras, os, sys, itertools, sklearn


# Instructions for reproducing results

Step 1: Reading through required documents
Start by reading through the hook document, rubric, and articles to get yourself situated with the case study. Research more information if you are still confused about the concept/technologies used.

Step 2: import data
Download the .rar file from the attached link in the DATA folder, you may need an external website to extract the zip file.
This data is not set up correctly to be used by our model, so it will require some cleaning.

Step 3: Cleaning data
Use the attached script to clean the data, it should take all of the images from each user and combine them into their respective alphabetical lables. None of the data should be lost by this point and it should produce a zip file for you to use. Some additional cleaning may be done in the main SCRIPTS folder, removing any corrupted images.

Step 3: Model Creation and Training
Use the base ResNet50v2 model from the tensorflow.keras package to start creating your new model. Once the base model (with the top layers excluded) is imported you will then preprocess the data, set up some callbacks, then finally train the data for the first time.
After this first phase is completed, you will then unfreeze the base model, while keeping the batch normalization layers forzen, and retrain the model with a smaller learning rate. After this the model should be ready to give you your final validation accuracy and loss.
Create a list of all the accuracies and loss for each respective label and evaluate if your model needs work.
 
Step 4: Plotting Results
Create a confusion matrix using the package from sklearn to see where the model is predicting wrong in your validation set and draw conclusions from it.
