# Chronic Kidney Disease Prediction Project
This project predicts the likelihood of a patient having Chronic Kidney Disease (CKD) based on various health metrics. The prediction model is deployed as a web application using Streamlit.

## Project Structure
1. app.py: This is the main Python script for the Streamlit web application. It takes user input for different health parameters and uses a pre-trained model to make a prediction.

2. Chronic disease predictions.ipynb: This Jupyter notebook documents the machine learning workflow, including data preprocessing, model training, and evaluation.

3. models/: This directory stores the trained machine learning models and the data scaler.

4. model_gbc.pkl: The trained Gradient Boosting Classifier model.

5. scaler.pkl: The MinMaxScaler object used for scaling the numeric features.

## Machine Learning Workflow
The Chronic disease predictions.ipynb notebook details the steps taken to build the prediction model:

Data Loading and Selection: The project uses a dataset containing various health indicators. 

Key features such as age, bp (blood pressure), sg (specific gravity), al (albumin level), hemo (hemoglobin level), sc (serum creatinine), htn (hypertension), dm (diabetes mellitus), cad (coronary artery disease), appet (appetite), and pc (pus cell) were selected for the model.

## Data Preprocessing and Cleaning:

1. Missing values in numerical columns (age, bp, hemo, sc) were filled with the median of their respective columns.

2. Missing values in categorical columns (sg, al, htn, dm, cad, appet, pc) were filled using the mode (most frequent value).

3. String values in object-type columns were cleaned by removing leading/trailing whitespace and tabs.

## Encoding and Scaling:

1. Categorical features like htn, dm, cad, appet, and pc were converted into numerical values (e.g., "yes" -> 1, "no" -> 0).

2. The target variable, classification ("ckd" or "notckd"), was also encoded to 1 and 0, respectively.

3. Numerical features (age, bp, sg, al, hemo, sc) were scaled using MinMaxScaler to normalize their values between 0 and 1.

4. Data Balancing: The original dataset had an imbalance with 250 instances of 'ckd' and 150 instances of 'notckd'. To address this, the SMOTE (Synthetic Minority Over-sampling Technique) was used to balance the dataset, resulting in 250 instances for each class.

## Model Training and Selection:

1. Several classification models were trained and evaluated, including Logistic Regression, Support Vector Classifier, Random Forest Classifier, K-Nearest Neighbors, Decision Tree Classifier, Gaussian Naive Bayes, AdaBoost Classifier, and Gradient Boosting Classifier.

2. The models were trained on a balanced training set and evaluated on a test set.

3. The Gradient Boosting Classifier achieved the highest accuracy of 0.99 and was selected as the final model.

4. Model Persistence: The trained Gradient Boosting Classifier model and the MinMaxScaler scaler were saved using the pickle library for use in the Streamlit application.

## How to Use the App
1. The Streamlit application (app.py) provides a user-friendly interface to predict the likelihood of CKD.

2. Run the App: Execute the app.py file using Streamlit.

3. Input Parameters: The interface allows you to input patient data for the following features: age, bp, sg, al, hemo, sc, htn, dm, cad, appet, and pc.

4. Get Prediction: Click the "Predict" button to get the result, which indicates whether the patient is likely to have Chronic Kidney Disease.
