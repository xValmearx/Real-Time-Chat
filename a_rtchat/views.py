from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ChatmessageCreateFrom

# Create your views here.

@login_required
def chat_view(request):

    # get the message group of the 
    chat_group = get_object_or_404(ChatGroup,group_name = 'public-chat')

    # get the last 30 messages within the group
    chat_messages = chat_group.chat_messages.all()[:30]

    # this gets the form to create new messages into out group chat app
    form = ChatmessageCreateFrom()

    # if the user it making a post
    if request.htmx:

        # select the form
        form = ChatmessageCreateFrom(request.POST)

        # check if the form is valid
        if form.is_valid:

            # define the message
            message = form.save(commit=False)

            # assign the messages author and group
            message.author = request.user
            message.group = chat_group

            # save the message
            message.save()

            context = {
                "message" : message,
                'user' : request.user
            }

            return render(request, "a_rtchat/partials/chat_message_p.html",context)

    # uses chat.html in templates/a_rtchat as the template
    return render(request, 'a_rtchat/chat.html',
                  {'chat_messages' : chat_messages, 'form' : form})

