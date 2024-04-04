from googleapiclient.discovery import build

def fetch_youtube_data():
    api_key = 'AIzaSyCb5fsXkz_8Sizg1L2xHTI40ME7lfeXSvY'
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        type='video',
        maxResults=50, 
        q='sentdex'  
    )

    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]

    videos_request = youtube.videos().list(
        part='statistics',
        id=','.join(video_ids)
    )

    videos_response = videos_request.execute()

    print(videos_response)
    return response, videos_response,video_ids

#fetch_youtube_data()