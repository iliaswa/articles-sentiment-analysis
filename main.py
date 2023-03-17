from bs4 import BeautifulSoup
from textblob import TextBlob
import requests
import matplotlib.pyplot as plt

# Scrape the latest news articles from different sources
sources = ['https://www.bbc.com/news', 'https://edition.cnn.com/', 'https://www.nytimes.com/']
articles = []
for source in sources:
    r = requests.get(source)
    soup = BeautifulSoup(r.content, 'html.parser')
    headlines = soup.find_all('h3')
    descriptions = soup.find_all('p')
    #print(len(descriptions))
    for i in range(len(descriptions)):
        article = {}
        article['source'] = source
        article['headline'] = headlines[i].text
        article['description'] = descriptions[i].text
        articles.append(article)

# Perform sentiment analysis on each article
sentiments = []
for article in articles:
    blob = TextBlob(article['description'])
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)

# Visualize the overall sentiment using a pie chart
positive_sentiments = len([s for s in sentiments if s > 0])
neutral_sentiments = len([s for s in sentiments if s == 0])
negative_sentiments = len([s for s in sentiments if s < 0])
labels = ['Positive', 'Neutral', 'Negative']
sizes = [positive_sentiments, neutral_sentiments, negative_sentiments]
colors = ['yellowgreen', 'gold', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Overall Sentiment of Latest News Articles')
plt.show()
