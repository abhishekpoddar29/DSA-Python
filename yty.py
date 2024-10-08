from pytube import YouTube


YouTube('https://www.youtube.com/watch?v=hOHKltAiKXQ').streams.first().download()