# Anime Recommendation System
This project is an Anime Recommendation System that leverages both popularity-based and collaborative filtering methods to suggest anime based on user preferences and ratings. It utilizes Python libraries such as Pandas, NumPy, scikit-learn, and Flask to create an efficient and interactive recommendation engine.

# Datasets
The project uses datasets from Kaggle, which include information about anime titles, user ratings, and user details. These datasets provide valuable insights into user behavior and preferences, enabling the creation of accurate recommendation systems.

## Dataset link 
https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?rvi=1

# Features
* Popularity-Based Recommendation System
* Analyzes the number of ratings and the average rating for each anime.
* Filters anime with more than 250 ratings and sorts them by average rating to recommend the most popular anime.
  
# Collaborative Filtering Based Recommendation System
* Filters users who have rated more than 100 anime and anime with more than 100 ratings.
* Creates a pivot table and uses cosine similarity to find similar anime.
* Provides recommendations based on the similarity of anime titles.
# Dynamic Web Application
* Built with Flask to provide an interactive interface for users.
* Allows users to get recommendations based on popularity or collaborative filtering.
* Displays anime details, including title, studio, image URL, number of ratings, and average rating.
