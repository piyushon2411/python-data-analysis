"""
PURPOSE OF SCRIPT - Scrap tweets based on a twitter search term, Create a excel file with all the tweets
INSTRUCTIONS - Please read the comments to understand the code and edit
"""

# import necessary libraries
import tweepy  # To work with Twitter Library, install with "pip install tweepy"
import pandas as pd # Import the Panda Library for datam manupulation, install with "pip install pandas"

# Create a list of search terms
searchTerm = '#cricketquiz'

# Connect with the Twitter API
auth = tweepy.OAuthHandler('s0ba7YZeOqVjDKLhv7cVWXgWr',
                           'sgY67Bu1rJhQvd9kENQ64Yc5eilmgKOB0S0h8Utm4lHy1p5HNM')
auth.set_access_token('3237144762-vLhtAwKNY2YHopf0Uu1cmdMElGuS3MLUapdVHUl',
                      '0CYgEixWKhlAgSYG7PHM9ocOpAKbNX2eWzPWaaeiBmR2H')

api = tweepy.API(auth)

# Read tweets from home timeline
#public_tweets = api.home_timeline()
public_tweets = api.search(searchTerm)
tweets_text = []
for tweet in public_tweets:
    tweets_text.append(tweet.text)

# dataframe Tweets columns
df = pd.DataFrame({'Tweets': tweets_text})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('scrappedtweets.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Searched Tweets', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

""" # Declare CSV file variable
filename = "tweets.csv"
header = ("tweets")
data = [public_tweets]

# Create CSV file
def writer(header, data, filename):

    with open(filename, "w", newline="") as csvfile:
        tweets = csv.writer(csvfile)
        tweets.writerow(header)
        for x in data:
            tweets.writerow(x)

writer(header, data, filename)
 """