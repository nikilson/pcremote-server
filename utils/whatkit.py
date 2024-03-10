import webbrowser as web
import requests


def playonyt(topic):
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count - 5] == "/results":
        return "No videos found."
    else:
        return "https://www.youtube.com" + lst[count - 5]

    # print("Videos found, opening most recent video")
    # web.open("https://www.youtube.com"+lst[count-5])
def play_on_yt(song):
    song = (song.lower()).replace("play","")
    link = playonyt(song)
    web.open(link, new=0, autoraise=True)
