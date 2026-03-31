#import the stuff and then call the function by storing it in a new var

# we need these new to break the url into pieces, we need the video id, not the entire url


from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
    from urllib.parse import urlparse, parse_qs # imports two tools from python's built in lib
    parsed = urlparse(url) 
    video_id = parse_qs(parsed.query)["v"][0] 
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    for transcript in transcript_list: # forgot to put the colon bahahahaha
        print(
        transcript.video_id, 
        transcript.language,
        transcript.is_generated,
    )
    fetched = transcript.fetch()
    text = " ".join ([snippet.text for snippet in fetched])
    return(text)


if __name__ == "__main__":
    print(get_transcript('https://www.youtube.com/watch?v=P62sLqal7w4'))


