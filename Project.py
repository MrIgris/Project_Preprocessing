import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Accessing Data set
df = pd.read_csv("titles.csv")  
print(df)  
#Showing how many rows and columns in data set

print(df.shape)

#Accessing rows and columns 
rows=df.shape[0]
columns = df.shape[1]


print(f"There are {rows} rows and {columns} columns in the data set")

#Accessing a single type in a cloumns like we are getting shows and movies in the type column

show_count = df[df["type"]=="SHOW"].shape[0]
print(f"There are {show_count} shows in the dataset")

movie_count = df[df["type"]=="MOVIE"].shape[0]
print(f"There are {movie_count} movies in the dataset")


#information of the data what type of data it is and how many null vaules
print(df.info())


#cleaning the data
#Age verification null values changed to NO AC available

df["age_certification"].fillna("NO AC available", inplace=True)  
print(df.info())

#Description null values changed to Not_available

df["description"].fillna("Not_available", inplace=True)  
print(df.info())

#Seasons null values changed to "0"

df["seasons"].fillna(0.0, inplace=True)
print(df.info())

#changing imdb_scores null value with median of the values

df["imdb_score"].fillna(df["imdb_score"].median(), inplace=True)
print(df.info())

#changing imdb_votes null value with mean of the values

df["imdb_votes"].fillna(df["imdb_votes"].mean(), inplace=True)
print(df.info())

#changing imdb_popularity null value with max of the values

df["tmdb_popularity"].fillna(df["tmdb_popularity"].max(), inplace=True)
print(df.info())

#changing tmdb_score null values with min of the values

df["tmdb_score"].fillna(df["tmdb_score"].min(), inplace=True)
print(df.info())

#null values identification 
rows_with_null = df.isna().any(axis=1),
print("all null values")
print(rows_with_null)
#True shows null values and false has data

null_in_row_for_title = df[df["title"].isnull()]
print("null values in title")
print(null_in_row_for_title)

null_in_row_for_id= df[df["imdb_id"].isnull()]
print("null values in id column")
print(null_in_row_for_id)

#replacing imdb id values with tm0000

df["imdb_id"].fillna("Tm0000", inplace=True)
print(df.info())

#printing null values columns

for column in df:
    if df[column].isnull().any():
       print('{0} has {1} null values'.format(column, df[column].isnull().sum()))
       
       
#droping the title entry        
df.dropna(inplace=True)
print(df.info())

#Now using matplot library some plots

#countplot for the type column it shows how many entries are movies and shows
sns.countplot(x=df['type'])
plt.show()

#countplot for age certification

sns.countplot(x=df['age_certification'])
plt.show()

#using histrogram to check the increase in release of the movies in year

sns.histplot(df['release_year'], bins=30,kde=True)
plt.title("Distribution of Release Years")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.show()
       