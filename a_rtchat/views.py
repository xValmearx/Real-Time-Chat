from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def chat_view(request):

    # get the message group of the 
    chat_group = get_object_or_404(ChatGroup,group_name = 'public-chat')

    # get the last 30 messages within the group
    chat_messages = chat_group.chat_messages.all()[:30]

    # uses chat.html in templates/a_rtchat as the template
    return render(request, 'a_rtchat/chat.html',{'chat_messages' : chat_messages})

