import streamlit as st
import pickle

def main():
    st.title('Simple Spam Classification App')
    
    user_input = st.text_area('Enter sentences (one per line):')

    # Load models
    with open('spam_detect_model.pkl', 'rb') as f: 
        loaded_model = pickle.load(f)
    
    with open('vectorizer_filename.pkl', 'rb') as f: 
        vect_model = pickle.load(f)

    # Create a button to predict
    if st.button('Predict'):
        if user_input:
            # Split user input into sentences
            sentences = user_input.split('\n')
            predictions = []

            for sentence in sentences:
                X = vect_model.transform([sentence]) # Transforming the sentence
                X_dense=X.toarray()
                prediction = loaded_model.predict(X_dense)  # Make prediction
                predictions.append(prediction[0])  # Append the first element of prediction

            # Display predictions
            st.write('Predicted classes:')
            for sentence, prediction in zip(sentences, predictions):
                st.write(f'Input: {sentence} | Predicted class: {prediction}')
        else:
            st.warning('Please enter sentences')  # Warning if no input

# Ensure main runs only when the script is executed directly
if __name__ == "__main__":
    main()
