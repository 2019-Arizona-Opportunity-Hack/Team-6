import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
import csv
def json_to_csv(json_data, name):
    emp_data = json_data
    # open a file for writing
    employ_data = open(name+".csv", 'w+', encoding="utf-8")
    # create the csv writer object
    csvwriter = csv.writer(employ_data)
    count = 0

    for emp in emp_data:

          if count == 0:

                 header = emp.keys()

                 csvwriter.writerow(header)

                 count += 1

          csvwriter.writerow(emp.values())

    employ_data.close()
def CountFrequency(my_list):

    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    with open('mycsvfile.csv', 'w+') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, freq.keys())
        w.writeheader()
        w.writerow(freq)
def twitter_wordcloud(topic):
    #Connect to Twitter
    APP_KEY = "oRzHEj2WJ38N2nfAOA20SFrsP"
    APP_SECRET = "9qGfPGM9KxDje3GiMLslThC3oHHmc9VWu368J6imV2NNJQcQ0q"
    TWITTER_ACCESS_TOKEN = '1168919777940660224-aGUI9TmVvkg2Ll2VDUb6a5VDkCyeEb'
    TWITTER_ACCESS_TOKEN_SECRET = 'l2Fdu6rNYGpTgomMvE5aBYWJmBPIv0bOQ8ui2oltrpWjJ'
    twitter = Twython(app_key=APP_KEY,app_secret= APP_SECRET,oauth_token=TWITTER_ACCESS_TOKEN, oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    #Get tweets from topic
    user_timeline=twitter.search(q=topic+" science", count=1000)
    user_timeline= user_timeline["statuses"]
    json_to_csv(user_timeline, topic)
    #Extract textfields from tweets
    raw_tweets = []
    for tweets in user_timeline:
        raw_tweets.append(tweets['text'])

    #Create a string form of our list of text
    raw_string = ''.join(raw_tweets)
    no_links = re.sub(r'http\S+', '', raw_string)
    no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
    no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)

    words = no_special_characters.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
    words = [w.lower() for w in words]
    words = [w for w in words if w not in STOPWORDS]
    words = [w for w in words if w != topic]
    CountFrequency(words)
    mask = np.array(Image.open('circle.jpg'))

    wc = WordCloud(background_color="white", max_words=2000, mask=mask)
    clean_string = ','.join(words)
    wc.generate(clean_string)

    f = plt.figure(figsize=(50,50))
    """f.add_subplot(1,2, 1)
    plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.title('Original Stencil', size=40)
    plt.axis("off")
    f.add_subplot(1,2, 2)"""
    plt.imshow(wc, interpolation='bilinear')
    plt.title('Generated Cloud', size=50)
    plt.axis("off")
    plt.savefig("templates/assets/img/"+topic+".png")

twitter_wordcloud("star wars")
