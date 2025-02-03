# 📧 SMS Spam Detection System Using NLP


## 🚀 Overview

Welcome to the SMS Spam Detection System! This project leverages Natural Language Processing (NLP) techniques to classify SMS messages as spam or ham (non-spam). Developed during an internship with AICTE's "AI: Transformative Learning with TechSaksham"—a joint CSR initiative by Microsoft and SAP focusing on AI technologies—this system aims to enhance communication safety by filtering out unwanted messages.

Explore the live application here: [SMS Spam Detection App](https://smsspamdetectionsystemusingnlp.streamlit.app/)

## 🛠️ Features

- **Real-time Classification**: Instantly determine if an SMS is spam or ham.
- **User-Friendly Interface**: Intuitive design for seamless user experience.
- **Machine Learning Model**: Trained on a labeled dataset for accurate predictions.
- **Deployment**: Accessible via a web application powered by Streamlit.



## 🗂️ Project Structure

```bash
SMS_Spam_Detection_System_Using_NLP/
├── app.py                     # Streamlit application script
├── sms-spam-detection.ipynb   # Jupyter Notebook for data analysis and model training
├── sms-spam.csv               # Dataset containing labeled SMS messages
├── sms_model.pkl              # Serialized trained machine learning model
├── sms_vector.pkl             # Serialized vectorizer for text data
├── requirements.txt           # List of dependencies
├── .gitignore                 # Files and directories to be ignored by Git
└── README.md                  # Project documentation
```

## 📝 Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arun-raze19/SMS_Spam_Detection_System_Using_NLP.git
   cd SMS_Spam_Detection_System_Using_NLP
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. **Interact with the App**:
   Open your browser and navigate to `http://localhost:8501` to use the application.

## 📚 Methodology

- **Data Preprocessing**: Cleaning and preparing the SMS data for analysis.
- **Feature Extraction**: Utilizing techniques like TF-IDF to convert text into numerical features.
- **Model Training**: Implementing machine learning algorithms to classify messages.
- **Evaluation**: Assessing model performance using metrics such as accuracy, precision, and recall.

For detailed insights, refer to the [Jupyter Notebook](sms-spam-detection.ipynb).

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes. Ensure that your contributions align with the project's objectives and maintain code quality.



## 📞 Contact

For any inquiries or feedback, please reach out to me in [Linkedin](www.linkedin.com/in/arunraze) .
