import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv(
    r'C:\Users\ASUS\Pandas-Data-Science-Tasks\multilingual_mobile_app_reviews_2025.csv')

# Clean the data
df.dropna(subset=['review_text'], inplace=True)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['user_country'] = df['user_country'].fillna('Undefined')
df['user_gender'] = df['user_gender'].fillna('UnKnown')
df['app_version'] = df['app_version'].fillna('Undefined')

# Chart plotting function


def plot_bar(data, title, xlabel, ylabel, rotation=0, kind='bar', figsize=(10, 6)):
    data.plot(kind=kind, figsize=figsize, title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if rotation:
        plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()


# Data analysis
average_rating_per_app = df.groupby(
    'app_name')['rating'].mean().sort_values(ascending=False)
rating_by_language = df.groupby('review_language')[
    'rating'].mean().sort_values(ascending=False)
rating_by_country = df.groupby('user_country')[
    'rating'].mean().sort_values(ascending=False)
rating_by_category = df.groupby('app_category')[
    'rating'].mean().sort_values(ascending=False)
rating_by_gender = df.groupby('user_gender')[
    'rating'].mean().sort_values(ascending=False)
rating_by_age = df.groupby('user_age')['rating'].mean()

# Visualizations
plot_bar(average_rating_per_app, 'Average Rating per App',
         'Average Rating', 'App Name', kind='barh', figsize=(10, 12))
plot_bar(rating_by_category, 'Average Rating by App Category',
         'App Category', 'Average Rating', rotation=45)
plot_bar(rating_by_gender, 'Average Rating by Gender',
         'Gender', 'Average Rating')
plot_bar(rating_by_age, 'Average Rating by Age',
         'Age', 'Average Rating', kind='line')
