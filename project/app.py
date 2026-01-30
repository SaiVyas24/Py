import streamlit as st
import pandas as pd

st.title("Student Management System")
st.write("Welcome to the student management system app.")

# Input fields
name = st.text_input("Enter student name:")
age = st.number_input("Enter student age:", min_value=1, max_value=25)
marks = st.number_input("Enter student marks:", min_value=0, max_value=100)

# Button action
if st.button("Add Student"):
    if name == "":
        st.error("Please enter student name")
    else:
        st.success(f"Student {name} added successfully!")
        student_data = {
            "Name": name,
            "Age": age,
            "Marks": marks
        }
        df = pd.DataFrame([student_data])
        st.dataframe(df)

st.write("You can manage student records here.")
st.write("This is a simple app to demonstrate Streamlit capabilities.")