# import scrapetube

# videos = scrapetube.get_channel("@warma_ext")

# print(videos)

# for video in videos:
#     print(video['videoId']) 

import scrapetube
from os import system

videos = scrapetube.get_playlist("PLocX9XsW8zmgCRR6_5njSX7qfKUL2Rta6")

for video in videos:
    url = "https://www.youtube.com/watch?v="+video['videoId']
    print('youtube-download-cli "'+url+'" mp3')
    system('youtube-download-cli "'+url+'" mp3')
    print(video['title']['runs'][0]['text'])
    print('-------------')


