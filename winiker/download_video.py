

import yt_dlp

#video_url = "https://www.youtube.com/watch?v=69ffwl-8pCU"

def download_video(video_url):


    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best quality for video and audio
        'outtmpl': 'winiker/videos/%(title)s.%(ext)s',
        'postprocessors': [{  # Ensure the video is converted to mp4
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 format
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("Download Completed")
