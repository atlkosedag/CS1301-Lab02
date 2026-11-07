# This creates the page for displaying data visualizations.
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import json
import csv
import statistics
# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
)
# PAGE TITLE
st.title("Music Genre and Instrument Analysis")
# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open("data.json","r") as file:
    music=json.load(file)
instruments=["Guitar","Bass","Drums","Keyboard"]
genres=list(music.keys())
counts={}
for instrument in instruments:
    counts[instrument]=0
for genre in genres:
    for song in music[genre]:
        for instrument in song["Instruments"]:
            counts[instrument]=counts[instrument]+1
names=list(counts.keys())
values=list(counts.values())
st.header("Instrument Appearances Across 20 Songs")
fig,ax=plt.subplots()
ax.barh(names,values)
ax.set_xlabel("Number of Songs")
ax.set_xlim(0,21)
st.pyplot(fig)
plt.close(fig)
st.write("This graph shows how many of the 20 songs feature each instrument, based on approximate instrument classifications.")
st.header("Instrument Use by Genre")
if "genre" not in st.session_state:
    st.session_state.genre="Psychedelic Rock"
selected=st.selectbox("Choose a genre:",genres,key="genre")
genreCounts={}
for instrument in instruments:
    genreCounts[instrument]=0
for song in music[selected]:
    for instrument in song["Instruments"]:
        genreCounts[instrument]=genreCounts[instrument]+1
chart=pd.DataFrame({"Instrument":instruments,"Count":list(genreCounts.values())})
chart=chart.set_index("Instrument")
st.line_chart(chart,y_label="Number of Songs")
st.write("Selected genre:",selected)
st.subheader("Songs Included")
for song in music[selected]:
    st.write(song["Song"],"-",song["Artist"])
# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
st.header("Music Survey Results")
file=open("data.csv","r")
reader=csv.DictReader(file)
responses=[]
for row in reader:
    responses.append(row)
file.close()
st.subheader("Favorite Music Genres")
genres=["Psychedelic Rock","Funk","Jazz","Hip-Hop","Indie Rock"]
genreTotals=[0,0,0,0,0]
for row in responses:
    for i in range(len(genres)):
        if row["Category"]==genres[i]:
            genreTotals[i]=genreTotals[i]+1
fig2,ax2=plt.subplots()
ax2.bar(genres,genreTotals)
ax2.set_title("Favorite Music Genres")
ax2.set_xlabel("Genre")
ax2.set_ylabel("Number of Responses")
plt.xticks(rotation=35)
fig2.tight_layout()
st.pyplot(fig2)
plt.close(fig2)
st.write("This graph shows how many people selected each genre in the survey.")
st.header("Instrument Importance Ratings")
if "csv_genre" not in st.session_state:
    st.session_state["csv_genre"]="All Genres"
if "csv_min" not in st.session_state:
    st.session_state["csv_min"]=1
options=["All Genres","Psychedelic Rock","Funk","Jazz","Hip-Hop","Indie Rock"]
st.selectbox("Choose a survey genre:",options,key="csv_genre")
st.slider("Minimum rating:",1,10,key="csv_min")
ratings=[]
for row in responses:
    genre=row["Category"]
    rating=int(row["Value"])
    if st.session_state["csv_genre"]=="All Genres" or genre==st.session_state["csv_genre"]:
        if rating>=st.session_state["csv_min"]:
            ratings.append(rating)
if len(ratings)>0:
    numbers=[]
    for i in range(len(ratings)):
        numbers.append(i+1)
    fig3,ax3=plt.subplots()
    ax3.plot(numbers,ratings,marker="o")
    ax3.set_title("Instrument Importance Ratings")
    ax3.set_xlabel("Response Number")
    ax3.set_ylabel("Rating (1-10)")
    ax3.set_ylim(0,11)
    st.pyplot(fig3)
    plt.close(fig3)
else:
    st.write("No responses found.")
st.subheader("Rating Statistics")
if len(ratings)>0:
    mean=statistics.mean(ratings)
    median=statistics.median(ratings)
    col1,col2=st.columns(2)
    with col1:
        st.metric("Mean Rating",round(mean,2))
    with col2:
        st.metric("Median Rating",round(median,2))
else:
    st.write("No ratings available.")