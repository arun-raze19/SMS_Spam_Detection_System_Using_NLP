#by Arunkumar . V (arunkumar1974pro@gmail.com)
import streamlit as st
import pickle
with open('sms_vector.pkl', 'rb') as f:
    sms_vector = pickle.load(f)
with open('sms_model.pkl', 'rb') as f:
    sms_model = pickle.load(f)
st.title('SMS Spam Detection System Using NLP')
user_input = st.text_area('Enter the SMS message(text) to classify:', '')
if st.button('Detect'):
    if user_input.strip():
        input_tfidf = sms_vector.transform([user_input])
        prediction = sms_model.predict(input_tfidf)[0]
        if prediction == 1:
            st.error('This message is Detected as a SPAM.')
        else:
            st.success('This message is Detected as a HAM (NOT SPAM).')
    else:
        st.warning('Please enter a valid SMS text.')
#by Arunkumar . V (arunkumar1974pro@gmail.com)