# -*- coding: utf-8 -*-

import os
os.environ['KAGGLE_CONFIG_DIR'] = '/content'

!chmod 600 /content/kaggle.json

!kaggle datasets download -d jiashenliu/515k-hotel-reviews-data-in-europe

!unzip \*.zip && rm *.zip

import string
import pandas as pd
import numpy as np
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

df = pd.read_csv('Hotel_Reviews.csv')
df.head()

df.info()

df.columns=[x.lower() for x in df.columns]

df.columns

drop_columns = ['additional_number_of_scoring',
                'review_date', 'reviewer_nationality',
                'negative_review', 'review_total_negative_word_counts',
                'total_number_of_reviews', 'positive_review',
                'review_total_positive_word_counts',
                'total_number_of_reviews_reviewer_has_given',
                'reviewer_score', 'days_since_review']
df1 = df.drop(columns = drop_columns, axis = 1)
df1.head()

df1.isna().sum()

df1.dropna(inplace = True)

print('Duplicated data:', df1.duplicated().sum())

df1.drop_duplicates(keep = 'first', inplace = True)

hotel=list(df1['hotel_name'].unique())
len(hotel)

# Inherently, there are "H tel" in the dataset
df1[df1['hotel_name'].str.contains("H tel")]['hotel_name'].unique()

#impute the word "H tel" to "Hotel"
df1['hotel_name']=df['hotel_name'].apply(lambda x:x.replace('H tel','Hotel'))

# Replacing "United Kingdom with "UK"
df1['hotel_address'] = df1['hotel_address'].str.replace("United Kingdom", "UK")

# Split the address and pick the last word in the address to identify the country
df1["countries"] = df1['hotel_address'].apply(lambda x: x.split(' ')[-1])
print(df1['countries'].unique())

exclude = set(string.punctuation)
def clean(x):
    return set([''.join(ch for ch in i.lower() if ch not in exclude).strip() for i in x[2:][:-2].split(',')])

# applying to clean the tags and assigning them to a new column
df1['tags'] = df1['tags'].map(clean)

# global variable
tag_sum_list = []

def get_tag_sum_elems(tag_sum_string):
    global tag_sum_list # use the global variable
    # extend the global variable with this_list
    tag_sum_list.extend(tag_sum_string)
    return True

for i in df1['tags']:
    get_tag_sum_elems(i)

tag_sum_set = set(tag_sum_list)
tag_sum_set

df1.head()

print(df1.shape)

# Function to remove the 'submitted from a mobile device' tag from the tags set
def remove_tag(tags_set):
    tags_set.discard("submitted from a mobile device")
    return tags_set

# Apply the function to the 'tags' column
df1['tags'] = df1['tags'].apply(remove_tag)

def recommend_hotel(input_description, data=df1):
    # Preprocess the input
    input_description = input_description.lower()
    words = word_tokenize(input_description)
    stop_words = stopwords.words('english')
    lemm = WordNetLemmatizer()
    filtered = [lemm.lemmatize(word) for word in words if word not in stop_words and word.isalpha()]

    # Extract words from the input description as potential location identifiers
    potential = set(filtered)

    # Prepare the data
    data['processed_address'] = data['hotel_address'].apply(lambda x: set(word_tokenize(x.lower())))
    data['processed_tags'] = data['tags'].apply(lambda x: set(word_tokenize(x.lower())) if isinstance(x, str) else set())

    # Compute similarity based on tags and check for location match in address
    cos = []
    for index, row in data.iterrows():
        tag_intersection = row['processed_tags'].intersection(potential)
        address_intersection = row['processed_address'].intersection(potential)
        # Increase similarity score for matches in address to prioritize location match
        cos.append(len(tag_intersection) + len(address_intersection))

    data['similarity'] = cos
    data = data.sort_values(by=['similarity', 'average_score'], ascending=[False, False])
    data = data.drop_duplicates(subset='hotel_name', keep='first')
    data.reset_index(drop=True, inplace=True)

    return data[['hotel_name', 'hotel_address', 'average_score']].head()

input_description = input("What do you need?\n")
recommendation = recommend_hotel(input_description)
recommendation

input_description = input("What do you need?\n")
recommendation = recommend_hotel(input_description)
recommendation