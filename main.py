from flask import Flask, render_template
import feedparser

myURLs = ["http://feeds.bbci.co.uk/news/business/rss.xml",
          "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
          "http://feeds.bbci.co.uk/news/technology/rss.xml",
          "http://www.wsj.com/xml/rss/3_7085.xml",
          "http://www.wsj.com/xml/rss/3_7031.xml",
          "http://www.wsj.com/xml/rss/3_7455.xml",
          "http://www.wsj.com/xml/rss/3_7014.xml"]

keywords = {"security",
            "Security",
            "hacker",
            "hackers",
            "Hacker",
            "Hackers",
            "banking",
            "Banking",
            "Berlin"}

app = Flask(__name__)

@app.route('/')
def index():
    entriesFiltered = []
    for url in myURLs:
        entries = feedparser.parse(url).entries
        for story in entries:
            if any(keyword in story['summary'] for keyword in keywords):
                entriesFiltered.append(story)
                
    return render_template("index.html", entries = entriesFiltered)

if __name__ == '__main__':
  app.run()
