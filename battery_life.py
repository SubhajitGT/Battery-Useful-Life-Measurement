import streamlit as st
import pickle
import gzip
import numpy as np

def main():
    st.title('Battery Life Prediction :battery: -->')

    with gzip.open('random_forest_model_Decrement_3.6_3.4V_and_4.15V.pkl.gz', 'rb') as file:
        loaded_model = pickle.load(file)

    num1 = st.number_input("Enter **Decrement 3.6-3.4V (s)** value")
    st.write("The time it takes for the battery voltage to drop from 3.6V to 3.4V during discharge.")
    num2 = st.number_input("Enter **Max. Voltage Dischar. (V)** value")
    st.write("The maximum voltage reached during the discharge phase.")
    num3 = st.number_input("Enter **Min. Voltage Charg. (V)** value")
    st.write("The minimum voltage reached during the charge phase.")
    num4 = st.number_input("Enter **Time at 4.15V (s)** value")
    st.write("The duration for which the battery stays at a specific voltage (4.15V) during the charging or discharging process")

    error_message = st.empty()
    def inputs_are_valid():
        return all(isinstance(i, (int, float)) and i != '' for i in [num1, num2, num3, num4])
    
    if st.button("Submit"):
        if inputs_are_valid():
            new_input = np.array([[num1, num2, num3, num4]])
            new_prediction = loaded_model.predict(new_input)
            st.write(f"Based on the inputs: {num1}, {num2}, {num3}, {num4}")
            st.write(f"The Prediction for **Battery Remaining Useful Life** is: {new_prediction[0]}")

        else:
            error_message.error("Please enter valid numeric values in all fields.")

if __name__=="__main__":
    main()