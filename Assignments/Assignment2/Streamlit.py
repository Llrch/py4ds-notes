import streamlit as st
import pandas as pd
import plotly.express as px

# Render the Streamlit app first
st.set_page_config(
    page_title="The Use of Big Data for Understanding the Video Game Market",
    page_icon="🎮",
    layout="wide"
)

# Set the background color and font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        font-family: 'Helvetica', 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

paragraph_intro = "The use of Big Data in the video game industry has become increasingly important in recent years. With the rise of digital distribution and online gaming, companies have access to vast amounts of data on player behavior and preferences. By analyzing this data, companies can gain insights into player engagement, identify trends, and develop targeted marketing strategies. Additionally, data analysis can be used to inform game design decisions, leading to more engaging and successful games. This has resulted in a shift towards a data-driven approach to game development and marketing. In this context, the use of Big Data has the potential to revolutionize the video game industry and shape the future of gaming."

paragraph1 = "I had trouble finding a free dataset for Türkiye, so I decided to focus my project on analyzing global, Europe, North America, and Japan sales, using a dataset I already had. I may explore Türkiye in the future, but for now, not having access to the right dataset could hinder my project's success. If companies face similar issues, they may need to create their own datasets for specific needs."
paragraph2 = "If I had access to a Türkiye dataset, I planned to analyze the correlation between the country's economy and the popularity of certain video games globally, but not in Türkiye. For example, I wanted to explore why the Zelda series, popular globally, is not as popular in Türkiye due to limited Nintendo console users."
paragraph3 = "The dataset I selected combines sales and scores, allowing me to conduct regionalized analyses, important for my project's goals. This saves me time from merging separate datasets, making it beneficial to my project."

paragraph4 = "Firstly, we can see what the most popular games are for some regions that have global sales greater than 10 million. We need to consider that these sales are cumulative data until 2016. So, newer games have less sales. We will make our analysis with respect to this important information."

paragraph5 = "We can see that, except from Japan and Other countries, Wii Sports is the most sold game. So, why is that? Let's take a look."
paragraph6 = "In Japan, Pokémon has a massive following and has been a cultural phenomenon for over two decades. This popularity is likely due to the franchise's origins in Japan and its ability to appeal to a wide audience, including children and adults. In contrast, Wii Sports may not have had the same cultural relevance in Japan, despite its success in other regions."
paragraph7 = "As for the Other countries (such as Middle East), Grand Theft Auto (GTA) is popular because of its open-world gameplay and its ability to allow players to experience a world that they may not be able to in real life. Additionally, the series' gritty and mature themes, which include crime and violence, may appeal to some audiences in the region."

paragraph8 = "Firstly, it is evident that North America's sales generate the largest portion of sales in terms of numbers. This can be attributed to the fact that the United States has the world's largest economy, which is the primary reason for this situation. Additionally, this trend can also be observed in countries outside of the USA, EU, and Japan, where both sales numbers and economies are relatively lower."
paragraph9 = "Secondly, it is apparent that the most popular genre in every region, except Japan, is action games. However, in Japan, RPGs (role-playing games) take the lead as the most popular genre. This is because Japanese gaming culture has developed around a strong affinity for role-playing games. Furthermore, unlike other countries, Japanese gamers generally have less interest in shooter games. Therefore, it can be concluded that if a video game company intends to target the Asian market, they should prioritize producing RPGs rather than shooters."
paragraph10 = "Lastly, it is evident that globally, genres such as strategy, adventure, puzzle, simulation, and fighting are not as popular compared to action and RPG genres."

# Render the header with an emoji
st.title("The Use of Big Data for Understanding the Video Game Market 🎮📈")
st.write(paragraph_intro)
st.write("Let's dive into the data.")

# Render section: Most Popular (Sold) Games
st.header("Most Popular (Sold) Games")
st.write(paragraph4)
st.info("You can change between regions by using the dropdown.")

# Load the dataset
df = pd.read_csv("Assignments/Assignment2/Video_Games_Sales_as_at_22_Dec_2016.csv")

# Create a new dataframe with sales data grouped by game and region
sales_df = df.groupby(["Name"])[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].sum().reset_index()

# Filter the dataframe based on global sales
sales_df = sales_df[sales_df['Global_Sales'] >= 10]

# Sort the dataframe by global sales in descending order
sales_df = sales_df.sort_values("Global_Sales", ascending=False).reset_index(drop=True)

# Create a new dataframe with sales data grouped by genre and region
genre_sales = df.groupby(["Genre"])[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].sum().reset_index()

genre_sales = genre_sales.sort_values("Global_Sales", ascending=False).reset_index(drop=True)

# Define the dropdown options for regions
region_options = {
    'Global Sales': 'Global_Sales',
    'North America Sales': 'NA_Sales',
    'Europe Sales': 'EU_Sales',
    'Japan Sales': 'JP_Sales',
    'Other Sales': 'Other_Sales'
}

# Create the first dropdown menu for the bar chart
dropdown1 = st.selectbox('Select a region', list(region_options.keys()), index=1)

# Create the initial bar chart with fading colors
fig1 = px.bar(
    sales_df,
    y=region_options[dropdown1],
    x='Name',
    title="Most Sold Video Games until 2016 (larger than 10 million) - Sales by Game",
    labels={region_options[dropdown1]: 'Sales (million)'},
    color=region_options[dropdown1],
    color_continuous_scale="Viridis"
)

# Create a layout for the plots
col1, col2, col3 = st.columns(3)

with col1:
    # Render the first plot with the bar chart
    st.plotly_chart(fig1)

with col3:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write(paragraph5)
    st.write(paragraph6)
    st.write("Japan is embracing its own culture. In that case, a game can be developed based on newly popularized concepts within their culture.")

st.write(paragraph7)

st.header("Most Popular (Sold) Genres")
st.write("Now, we will look for the most popular genres in different regions.")
st.info("You can change between regions by using the dropdown.")

# Define the dropdown2 options for regions
region_options2 = {
    'North America Sales': 'NA_Sales',
    'Europe Sales': 'EU_Sales',
    'Japan Sales': 'JP_Sales',
    'Other Sales': 'Other_Sales'
}

# Create the second dropdown menu for the bar chart
dropdown2 = st.selectbox('Select a region', list(region_options2.keys()), key='region_dropdown')

fig2 = px.scatter(
    genre_sales,
    x="Genre",
    y=region_options2[dropdown2],
    size="Global_Sales",
    color="Global_Sales",
    labels={'x': 'Genre', 'y': 'Sales (million)'}
)

# Update the scatter plot based on the selected region
fig2.update_traces(
    marker=dict(line=dict(width=0.5, color='darkgray')),
    hovertemplate='<b>Genre</b>: %{x}<br><b>Sales</b>: %{y:.2f} million<br><b>Global Sales</b>: %{marker.size:.2f} million<br><extra></extra>'
)

# Define the color scale for fading
fig2.update_layout(coloraxis=dict(colorscale='Bluered'))

# Create a layout for the plots
col4, col5, col6 = st.columns(3)

with col4:
    # Display the scatter plot
    st.plotly_chart(fig2)

with col6:
    st.write("\n")
    st.write("\n")
    st.write(paragraph8)
    st.write(paragraph9)

st.write(paragraph10)