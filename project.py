import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Matpltlip/netflix_fake_dataset.csv')

# Bar Chart
type_counts = data['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue' , 'orange'])
plt.title('Number of movies vs TV shows on Netflix')
plt.xlabel('Type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('Matpltlip/moviesVStvshows.jpg')
plt.show()

# Pie Chart
rating_counts = data['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index, autopct='%1.1f%%' , startangle=90 , colors=['skyblue' , 'gold' , 'violet'])
plt.title('Percentage of Content Rating')
plt.tight_layout()
plt.savefig('Matpltlip/Content_Rating_pie.jpg')
plt.show()

movie_count = data[data['type'] == 'Movie'].copy()
movie_count['duration_int'] = movie_count['duration'].str.extract(r'(\d+)').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_count['duration_int'] , bins=30 , color='purple', edgecolor='black')
plt.title('Distribution of movie Duration')
plt.xlabel('Duration(minutes)')
plt.ylabel('Number of movies')
plt.tight_layout()
plt.savefig('Matpltlip/Movies_duration_histogram.jpg')
plt.show()

release_counts = data['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index , release_counts.values , color='red')
plt.title('Release year VS Number of Shows')
plt.xlabel('Release year')
plt.ylabel('No of Shows')
plt.tight_layout()
plt.savefig('Matpltlip/release_year_scatter.jpg')
plt.show()

country_count = data['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title('Top 10 Countries by No of Shows')
plt.xlabel('No of shows')
plt.ylabel('country')
plt.tight_layout()
plt.savefig('Matpltlip/Countries.jpg')
plt.show()

content_by_year = data.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2,figsize=(12,5))

ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('No of Movies')

ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows released per year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('No of TV Shows')

fig.suptitle('Comparision of Movies & TV Shows Over year')
plt.tight_layout()
plt.savefig('Matpltlip/movies_tvshows_comparision.jpg')
plt.show()