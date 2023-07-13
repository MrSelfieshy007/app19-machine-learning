from sklearn.metrics.pairwise import linear_kernel
similarity_matrix = linear_kernel(tfidf_matrix,tfidf_matrix)

#Find the most similar movies to a certain movie

movie_title = "John Carter"

idx = movies.loc[movies['title'] == movie_title].index[0]

scores = list(enumerate(similarity_matrix[idx]))

scores = sorted(scores,key=lambda x:x[1], reverse=True)

movie_indices = [tpl[0] for tpl in scores[1:4]]

list(movies['title'].iloc[movie_indices])

#actual code

def similar_movies(movie_title,nr_movies):
    idx = movies.loc[movies['title'] == movie_title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores,key=lambda x:x[1], reverse=True)
    movie_indices = [tpl[0] for tpl in scores[1:nr_movies+1]]
    similar_titles = list(movies['title'].iloc[movie_indices])
    return similar_titles

#call the function
similar_movies("Kung Fu Panda 3",3)
