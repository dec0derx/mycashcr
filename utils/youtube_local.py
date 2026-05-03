import os
import yt_dlp


def download_single_video(url, destination_path="/tmp/"):
    """
    Download a single YouTube video as MP3.
    """
    assert os.path.exists(destination_path), f"Invalid path '{destination_path}'"

    # Output file path
    out_path = os.path.join(destination_path, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": out_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"✅ MP3 downloaded to: {destination_path}")


# Example usage:
download_single_video(input("Enter YouTube video URL: "), destination_path="/Users/franz/Music")