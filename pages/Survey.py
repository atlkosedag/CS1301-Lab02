# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
)
# PAGE TITLE AND USER DIRECTIONS
st.title("Music Genre Survey")
st.write("Answer these questions about your favorite music genre.")
# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.text_input("What is your favorite music genre?")
    value_input = st.text_input("How important are instruments to this genre? (1-10)")
    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")
    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.

        genres = ["Psychedelic Rock", "Funk", "Jazz", "Hip-Hop", "Indie Rock"]

        if category_input in genres and value_input.isdigit():
            value = int(value_input)

            if value >= 1 and value <= 10:
                file = open("data.csv", "a")
                file.write(category_input + "," + str(value) + "\n")
                file.close()

                st.success("Your data has been submitted!")
                st.write(f"You entered: **Category:** {category_input}, **Value:** {value}")
            else:
                st.error("Please enter a number between 1 and 10.")
        else:
            st.error("Please enter one of the five genres and a valid number.")

# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
