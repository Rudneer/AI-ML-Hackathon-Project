import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies_data = pd.read_csv('movies_metadata.csv',low_memory=False)
movies_data.head()
movies_data.columns
from ast import literal_eval
movies_data['genres'] = movies_data['genres'].fillna('[]').apply(literal_eval)
movies_data['genres'] = movies_data['genres'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else[])
movies_data['genres'].head(2)
genre_split = movies_data.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
genre_split.head(6)
genre_split.name = 'Genre'
md = movies_data.drop('genres', axis=1).join(genre_split)
md.head()
links_small = pd.read_csv('links_small.csv', error_bad_lines= False)
links_small.head()
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
from pandas.api.types import is_numeric_dtype
is_numeric_dtype(md['id'])
md = md.drop([19730, 29503, 35587])
md['id'] = md['id'].astype('int')
md['id'].head(10)
md_new = md[md['id'].isin(links_small)]
md_new.shape
md_new_sample = md_new.sample(frac = 0.15,random_state=42)
md_new_sample.shape
md_new_sample['tagline'] = md_new_sample['tagline'].fillna('')
md_new_sample['description'] = md_new_sample['overview'] + md_new_sample['tagline']
md_new_sample['description'] = md_new_sample['description'].fillna('')
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),stop_words='english')
tfidf_matrix = tf.fit_transform(md_new_sample['description'])
tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim
pd.Series(md_new_sample.index, index=md_new_sample['title'])
md_new_sample = md_new_sample.reset_index()
titles = md_new_sample['title']
indices = pd.Series(md_new_sample.index, index=md_new_sample['title'])
def recommend(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]
recommend("Avatar").head(10)
