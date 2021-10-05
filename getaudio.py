import pandas as pd
import os
import random
df = pd.read_csv('cleaned_links_with_data.csv')
#For testing purposes, limit amount of audio downloaded
maxnum = 10000
limit = True
minnum = 0
i = 0
#print(df)
for entry in df.iterrows():
    if(limit and i>maxnum):
        break
    if(i>minnum and limit or not limit):
        print(entry[1]['link'])
        cmdstring = "ffmpeg -ss 10 -i $(youtube-dl -f 140 -g  " + entry[1]['link']+") -acodec copy -vcodec copy -t 10 audios/"+str(i)+".aac"
        print(cmdstring)
        os.system(cmdstring)
    i +=1

'''
other youtube dl commands i tried
youtube-dl -i --extract-audio --audio-format mp3  --postprocessor-args "-ss 00:01:50 -to 00:02:00" https://www.youtube.com/watch?v=NU9jx8vRW_E 
ffmpeg -ss 60 -i $(youtube-dl -f 140 -g  https://www.youtube.com/watch?v=aqz-KE-bpKQ) -acodec copy -vcodec copy -t 20 softboy.aac
youtube-dl -i --extract-audio --audio-format mp3 --external-downloader ffmpeg --external-downloader-args "-ss 00:01:00.00 -to 00:02:00.00" "https://www.youtube.com/watch?v=NU9jx8vRW_E"
'''