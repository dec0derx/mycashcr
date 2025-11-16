from django.shortcuts import render
from django.http import HttpResponse
from utils import youtube_bkp

def home(request):
    args = {"name": "Franz"}  
    return render(request, "winiker/home.html", args)

def downloader(request):
    args = {"name": "Franz"}  
    video_url = None
    if request.method == 'POST':
        video_url = request.POST.get('video_url')  # Capture the URL entered in the form
        print(video_url)    
        youtube_bkp.download_single_video(video_url, destination_path="/tmp/")
        return HttpResponse("Download is completed")
    return render(request, "winiker/downloader.html", args)

def combinepdf(request):
    return HttpResponse("combinepdf")
