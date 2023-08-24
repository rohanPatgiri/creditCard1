import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def creditCard_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == [0]):
      return 'The transaction is not fraudulent'
    else:
      return 'The transaction is fraudulent'
  
    
  
def main():
    
    
    # giving a title
    st.title('Credit Card Fraud dtetction Web App')
    
    
    # getting the input data from the user
    
    
    Time = st.text_input('Enter Value ')
    v1 = st.text_input('Enter Value')
    v2 = st.text_input('Enter Value')
    v3 = st.text_input('Enter Value')
    v4 = st.text_input('Enter Value')
    v5 = st.text_input('Enter Value')
    v6 = st.text_input('Enter Value')
    v7 = st.text_input('Enter Value')
    v8 = st.text_input('Enter Value')
    v9 = st.text_input('Enter Value')
    v10 = st.text_input('Enter Value')
    v11 = st.text_input('Enter Value')
    v12 = st.text_input('Enter Value')
    v13 = st.text_input('Enter Value')
    v14 = st.text_input('Enter Value')
    v15 = st.text_input('Enter Value')
    v16 = st.text_input('Enter Value')
    v17 = st.text_input('Enter Value')
    v18 = st.text_input('Enter Value')
    v19 = st.text_input('Enter Value')
    v20 = st.text_input('Enter Value')
    v21 = st.text_input('Enter Value')
    v22 = st.text_input('Enter Value')
    v23 = st.text_input('Enter Value')
    v24 = st.text_input('Enter Value')
    v25 = st.text_input('Enter Value')
    v26 = st.text_input('Enter Value')
    v27 = st.text_input('Enter Value')
    v28 = st.text_input('Enter Value')
   
    
    
    Amount = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = creditCard_prediction([Time,v1,v2,v3,v4,v5,
                                           v6,v7,v8,v9,v10,v11,
                                           v12,v13,v14,v15,v16,
                                           v17,v18,v19,v20, v21,
                                           v22,v23,v24,v25,v26,
                                           v27,v28, Amount])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
   main()