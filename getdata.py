import pandas as pd
from bs4 import BeautifulSoup
import datetime
import analyze_comments
#Reference to local html file containing youtube history
html_doc = "history/mini_file.html"

html_file = open(html_doc,"r")

soup = BeautifulSoup(html_file, 'html.parser')

try:
    old_data = pd.read_csv('cleaned_links_with_data.csv')
except:
    old_data = pd.DataFrame(columns=['title','link','date','sentiment'])

#maximum depth
maxlen = 10000
i = 0
minnum = len(old_data)

#Parse the various containers to extract title and watch date and video url.
for entry in soup.findAll('div', class_ = "mdl-grid"):
    if(maxlen!= None and i>maxlen):
        break
    if(i<minnum):
        i+=1
    else:
        try:
            tag = entry.find('a')
            timestring = tag.next_sibling.next_sibling.next_sibling.next_sibling[:-4]
            timestring = timestring.replace('Sept','Sep')
            element = datetime.datetime.strptime(timestring,"%d %b %Y, %H:%M:%S")
            timestamp = datetime.datetime.timestamp(element)
            
            link = tag['href']
            analysis = analyze_comments.analyse(tag['href'])
            content = tag.contents[0]
            print(content,link,timestamp,analysis)
            ndf = pd.DataFrame([[content,link,timestamp,analysis]],columns=['title','link','date','sentiment'])
            old_data = old_data.append(ndf)
            #print(textdata[-2])
        except:
            print("not able to retrieve link and title, skipping entry")
        old_data.to_csv("cleaned_links_with_data.csv")
        print('updating ', i, 4227)
        i+=1



