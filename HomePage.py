
# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="The Instruments Behind our Favorite Genres of Music",  # The title that appears in the browser tab
    page_icon="🎵",  # An emoji that appears as the icon in the browser tab
)
# WELCOME PAGE TITLE
st.title("The Instruments Behind our Favorite Genres of Music")

# INTRODUCTORY TEXT
st.write("""
This project explores how different instruments are used across various music genres.
I chose five of my personal favorite genres: psychedelic rock, funk, jazz, hip-hop, and indie rock.
The four instruments being compared are guitar, bass, drums, and keyboard.
I selected 20 real songs from artists including Pink Floyd, Parliament, Miles Davis, The Roots, and The Strokes.
I used song and album credits to identify which instruments were used, along with some estimate based on listening when I couldn't find specific credits for a song.
The first two graphs compare how often each instrument appears in the selected songs across the five genres.

For Part 2, I made a survey where people can choose their favorite genre and rate how important instruments are to it.
I used the responses to make two more graphs, one showing the most popular genres and another showing the ratings people gave.

### How to use this app:
- **Survey Page**: Choose your favorite genre and give a rating from 1 to 10.
- **Visuals Page**: Look at the instrument comparisons from Part 1 and the survey results from Part 2.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.

# st.image("images/welcome_image.png")
