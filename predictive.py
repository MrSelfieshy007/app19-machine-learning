import pandas

movies = pandas.read_csv('movies.csv')
credits = pandas.read_csv('credits.csv')
ratings = pandas.read_csv('ratings.csv')

"""Calculate a weighted rating

(WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C

v - number of votes for a movie

m - minimum  number of votes required

R - average rating of the movie

C - average rating across all movies

"""
m = movies["vote_count"].quantile(0.9)
C = movies["vote_average"].mean()
movies_filtered = movies.copy().loc[movies["vote_count"] >= m]

def weighted_rating(df,m=m,C=C):
    R = df["vote_average"]
    v = df["vote_count"]
    wr = ((v/v+m) * R) + (m / (v+m)* C)
    return wr

movies_filtered["weighted_rating"] = movies_filtered.apply(weighted_rating, axis=1)

movies_filtered.sort_values("weighted_rating", ascending=False)[["title", "vote_count", "vote_average", "weighted_rating"]].head(10)



