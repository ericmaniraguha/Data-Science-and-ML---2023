
import pickle
from IPython import get_ipython
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')

# loading dataset
data_movies = pd.read_csv('./tmdb_5000_movies.csv')
data_credits = pd.read_csv('./tmdb_5000_credits.csv')

# merge two dataset into one
data_movies = data_movies.merge(data_credits, on='title')


def recommend(movie):
    movie_index = data_movies[data_movies['title'] ==
                              movie].index[0]  # fetching the movie index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(data_movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')  # set title of movie recommender

option = st.selectbox('Select your movie: ', data_movies['title'].values)

# create a recommend button on the page
if st.button('Recommender'):
    recommendations = recommend(option)
    for i in recommendations:

        st.write(i)
