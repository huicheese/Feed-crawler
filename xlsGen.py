import feedparser
import xlwt

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

book = xlwt.Workbook(encoding="utf8")
sheet = book.add_sheet("Filtered News")

ctrR = 0
ctrC = 0

for url in myURLs:
    entries = feedparser.parse(url).entries
    for story in entries:
        if any(keyword in story['summary'] for keyword in keywords):
            for storyKey in ['title', 'link', 'published','summary']:
                sheet.write(ctrR, ctrC, story[storyKey])
                ctrC += 1
            ctrR += 1
            ctrC = 0

book.save("filteredNews.xls")
print "Done!"
                                                
            
