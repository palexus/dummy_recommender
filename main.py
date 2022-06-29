import pandas
from recommender import recommend_random


movies = pd.read_csv("data/movies.csv")

recommendations = recommend_random(None, movies=movies)

print(recommendations)
