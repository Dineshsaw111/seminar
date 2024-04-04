import pandas as pd
from googleapiclient.discovery import build
from sqlalchemy import create_engine, inspect
import os
import extract

def tranform_youtube_data():
    response, videos_response,video_ids = extract.fetch_youtube_data()

    DataList = []

    for item in videos_response['items']:
        video_id = item['id']
        video_title = response['items'][video_ids.index(video_id)]['snippet']['title']
        video_likes = item['statistics'].get('likeCount', 0)
        video_views = item['statistics'].get('viewCount', 0)
        data = {
            "Video Title": video_title,
            "Video ID": video_id,
            "Likes": video_likes,
            "Views": video_views
        }
        DataList.append(data)

        print(f"Video Title: {video_title}")
        print(f"Video ID: {video_id}")
        print(f"Likes: {video_likes}")
        print(f"Views: {video_views}")
        print("--------------")

    df_new = pd.DataFrame(DataList)
    return df_new
# tranform_youtube_data()    



