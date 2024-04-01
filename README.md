Fraud Detection ML App
This is a simple machine learning application for fraud detection built using Streamlit.

Overview
This application utilizes a trained machine learning model to predict fraud based on provided transaction details. The model predicts whether a transaction is fraudulent or not based on the type of transaction, amount, old balance, and new balance.

Getting Started
To run the application locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your_username/fraud-detection.git
Navigate to the project directory:
bash
Copy code
cd fraud-detection
Install the required dependencies:
bash
Copy code
pip install streamlit numpy pandas
Run the application:
bash
Copy code
streamlit run app.py
Usage
Enter the type of transaction (1 to 5).
Input the transaction amount.
Provide the old balance before the transaction.
Enter the new balance after the transaction.
Click on the "Predict" button to see the prediction.
Click on the "About" button to know more about the app.
Model Details
The application uses a pre-trained classifier model saved as classifier.pkl for fraud detection.

About
This application is created by Rishabh Tanpure and is built with Streamlit.
