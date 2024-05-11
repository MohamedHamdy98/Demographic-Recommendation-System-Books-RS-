import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Books Recommendation System",
    page_icon=":books",
    layout="wide",
    initial_sidebar_state="expanded")

# Load the dataset
@st.cache_data
def load_data():
    path = r'C:/Users/Mohamed Hamde/OneDrive - Culture and Science City/Desktop/Clean Code AI/streamLite/recommendation_system/data_books.csv'
    books = pd.read_csv('data_books.csv')
    return books

books = load_data()


# Create a Streamlit app
st.header(':books: :orange[Books Recommendation System]',divider='rainbow')

# Display some random books
st.subheader('Some Random Books:')
# st.dataframe(books.sample(5))
st.data_editor(
    books.sample(5),
    column_config={
        "Image-URL-S": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)
st.divider()

# Get recommendations for a top 10 books
def get_recommendations(books, n):
    n = int(n)
    #Sort books based on score calculated above
    books = books.sort_values('weighted_rating', ascending=False)
    #Print the top 10 movies
    return books[['Image-URL-L','Book-Title', 'Book-Author', 'Publisher', 'weighted_rating']].head(n)

with st.sidebar:
    st.header(':book: :orange[Demographic Filtering]', divider='rainbow')
    # User input for recommendation
    number_of_books = st.number_input('Enter a number of top books:', 1)
    # Get recommendations
    btn_get_rec = st.button('Get Recommendations')
    # the code on github

    

if btn_get_rec:
    recommendations = get_recommendations(books, number_of_books)
    st.subheader('Recommended Books:')
    st.data_editor(
        recommendations,
        column_config={
            "Image-URL-L": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        use_container_width=True,
        hide_index=True,
    )
