import logging
from django.shortcuts import render
from django.template.loader import render_to_string
from index.models import Comment
from utils import logs
# Create your views here.


def index(request):
    user_ip = get_user_ip(request=request)
    logs.logging.info(f"Traffic coming from: {user_ip}")

    if request.method == "POST":


        comment = Comment()
        comment.name = request.POST["name"]
        comment.comment = request.POST["feedback"]
        print(comment.name)
        comment.save()
        
    print(get_user_ip(request=request))
    return render(request, "index/index.html")

def feedback(request):
    feedback = "feedback test"
    return render(request, "index/feedback.html", {"feedback": feedback})


def get_user_ip (request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        # The header can contain a comma-separated list of IP addresses.
        user_ip = user_ip.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    return user_ip

             
