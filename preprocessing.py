import pandas as pd
import warnings

warnings.filterwarnings('ignore')
# Get Data set

columns_names = ["user_id", "item_id", "rating", "timestamp"]
df = pd.read_csv('ml-100k/u.data', sep='\t', names=columns_names)

movies_title = pd.read_csv("ml-100k/u.item", sep='\|', header=None, encoding="ISO-8859-1")
movies_title = movies_title.loc[:, :1]

movies_title.columns = ['item_id', 'title']

df = pd.merge(df, movies_title, on='item_id')


df.groupby('title').mean()['rating'].sort_values(ascending=False).head()
df.groupby('title').count()['rating'].sort_values(ascending=False)
ratings = pd.DataFrame(df.groupby('title').mean()['rating'])

ratings["num of ratings"] = pd.DataFrame(df.groupby('title').count()['rating'])
ratings.sort_values(by='rating', ascending=False)

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')


def recommend_movies(movie_name):
    movie_user_ratings = moviemat[movie_name]
    similar_to_movie = moviemat.corrwith(movie_user_ratings)

    corr_movie = pd.DataFrame(similar_to_movie, columns=['correlation'])
    corr_movie.dropna(inplace=True)

    corr_movie = corr_movie.join(ratings['num of ratings'])
    recommendation = corr_movie[corr_movie['num of ratings'] > 100].sort_values('correlation', ascending=False)

    return recommendation
