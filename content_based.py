import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pd.read_csv('movies.csv')



tfidf = TfidfVectorizer(stop_words='english')

movies['overview'] = movies['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(movies['overview'])

pd.DataFrame(tfidf_matrix.toarray(),columns=tfidf.get_feature_names())

tfidf_matrix.shape
