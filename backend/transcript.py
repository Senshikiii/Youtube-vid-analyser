#import the stuff and then call the function by storing it in a new var
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
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
    print(get_transcript('P62sLqal7w4'))


