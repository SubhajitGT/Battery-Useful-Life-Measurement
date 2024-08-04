import streamlit as st
import pickle
import gzip
import numpy as np

def main():
    st.title('Battery Life Prediction :battery: -->')

    with gzip.open('random_forest_comp_best_model.pkl.gz', 'rb') as file:
        loaded_model = pickle.load(file)

    num1 = st.number_input("Enter **Cycle_Index** value")
    st.write("The number of charge-discharge cycles the battery has undergone.")
    num2 = st.number_input("Enter **Discharge Time (s)** value")
    st.write("The total time the battery takes to discharge during a cycle.")
    num3 = st.number_input("Enter **Max. Voltage Dischar. (V)** value")
    st.write("The maximum voltage reached during the discharge phase.")
    num4 = st.number_input("Enter **Min. Voltage Charg. (V)** value")
    st.write("The minimum voltage reached during the charge phase.")

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