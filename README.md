# TASK3-END-TO-END-DATA-SCIENCE-PROJECT


## Project Overview

    This project demonstrates a complete **End-to-End Data Science workflow**, starting from data preprocessing to model deployment using an API. The objective of this project is to predict whether a customer will churn (leave a service) or stay, based on historical customer data.
    
    Customer churn prediction is a critical problem in industries such as telecom, banking, and e-commerce, where retaining customers is more cost-effective than acquiring new ones.
    
    This project covers all stages of a real-world data science pipeline, including:
    
    * Data collection
    * Data preprocessing
    * Feature engineering
    * Model training and evaluation
    * Model deployment using API


## Key Features

    * Complete Data Science lifecycle implementation
    * Data preprocessing and cleaning
    * Feature encoding and scaling
    * Machine Learning model training (Logistic Regression)
    * Model evaluation and prediction
    * Deployment using **FastAPI**
    * Real-time prediction through API

## Technologies Used

    * Python
    * pandas
    * NumPy
    * scikit-learn
    * FastAPI
    * Uvicorn
    * Pickle



##  Project Structure

   
     TASk3/
      │
      ├── train_model.py
      ├── model.py
      ├── app.py
      ├── churn.csv
      ├── model.pkl
      ├── scaler.pkl
      ├── requirements.txt
      └── README.md
   

##  Dataset Information

    The dataset used in this project is a customer dataset containing various features such as:
    
    * Customer demographics
    * Account information
    * Service usage details
    
    The target variable is:
    
    * **Churn** (Yes/No)
    
    The dataset is preprocessed by handling missing values, encoding categorical variables, and scaling numerical features before feeding it into the model.


## 🔄 Project Workflow

    ### 1️⃣ Data Collection
    
    The dataset is collected and loaded into the system using pandas.
    
    ### 2️⃣ Data Preprocessing
    
    * Removal of unnecessary columns
    * Handling missing values
    * Encoding categorical variables using LabelEncoder
    * Feature scaling using StandardScaler
    
    ### 3️⃣ Model Building
    
    A **Logistic Regression** model is trained on the processed data. This model is chosen due to its simplicity and effectiveness for binary classification problems.
    
    ### 4️⃣ Model Evaluation
    
    The model is evaluated based on its prediction performance. It learns patterns in customer behavior to identify potential churn.
    
    ### 5️⃣ Model Saving
    
    The trained model and scaler are saved using pickle files (`model.pkl`, `scaler.pkl`) for reuse in deployment.
    
    ### 6️⃣ Deployment using API
    
    The model is deployed using FastAPI, allowing users to send input data and receive predictions in real-time.


## How to Run the Project
    
    ### Step 1: Install Dependencies
    
    ```bash id="x7y8z9"
    pip install -r requirements.txt
    ```
    
    ---
    
    ### Step 2: Train the Model
    
    ```bash id="k9l8m7"
    python train_model.py
    ```
    
    This will generate:
    
    * `model.pkl`
    * `scaler.pkl`
    
    ---
    
    ### Step 3: Run the API Server
    
    ```bash id="p0o9i8"
    uvicorn app:app --reload
    ```
    
    ---
    
    ### Step 4: Open in Browser
    
    * API Home:
    
      ```
      http://127.0.0.1:8000
      ```
    
    * API Documentation (Swagger UI):
    
      ```
      http://127.0.0.1:8000/docs
      ```

## 📊 Output

* Real-time churn prediction
      * API response indicating:
      
        * "Customer will churn"
        * "Customer will stay"


## 📈 Key Concepts Covered

    * End-to-End Data Science Workflow
    * Data Preprocessing
    * Feature Engineering
    * Machine Learning (Classification)
    * Model Deployment
    * API Development


##  Insights

    * Data preprocessing plays a crucial role in model performance
    * Logistic Regression is effective for binary classification tasks
    * Deployment makes models usable in real-world applications
    * APIs enable integration with web and mobile applications

## Future Improvements

    * Use advanced models (Random Forest, XGBoost)
    * Add a frontend UI (Streamlit or React)
    * Deploy on cloud platforms (Render, AWS)
    * Add model monitoring and logging
    * Improve dataset with more features

##  Conclusion
    
    This project successfully demonstrates how to build and deploy a **complete data science solution**. It highlights the importance of combining data analysis, machine learning, and deployment to solve real-world business problems.
    sing practical data science skills.
