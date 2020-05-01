
import pandas as pd


# ******* GLOBAL PARAMETERS *********** #
neighbor_size = 5
top_n = 10

movies = pd.read_table("ex6/Data/ml-1m/movies.dat", "::", engine="python", names=['MovieID', 'Title', 'Genres'])
ratings = pd.read_table("ex6/Data/ml-1m/ratings.dat", "::", engine="python",
                        names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
users = pd.read_table("ex6/Data/ml-1m/users.dat", "::", engine="python",
                      names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-Code'])

# merge all to one -> then make sample and use only this table
data_right = pd.merge(ratings, movies, on='MovieID')
data = pd.merge(users, data_right, on='UserID').sample(50000)  # todo adjust sample size
data = data[['UserID', 'MovieID', 'Title', 'Rating', 'Genres']]
print(data.head(10))  # to see the user IDs i could try
data_grouped_byUser = data.groupby("UserID")
user_list = list(data["UserID"].unique())
movie_list = list(data["MovieID"].unique())


def checkUserId(userId):
    if int(userId) in user_list:
        return True
    else:
        return False


def recommendations(userID):
    # todo calculate top 20 recommendations for user

    # The recommendations can be computed with your nearest‐neighbor algorithm or 
    # using some existing library that, e.g., implements a matrix factorization approach. 
    # For this  have a look at https://mc.ai/overview‐of‐matrix‐factorisation‐techniques‐using‐python‐2/ 

    pass