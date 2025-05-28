from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatGroup(models.Model):

    # this will be the chat group name 
    group_name = models.CharField(max_length=128,unique=True)

    # returns the chat group name while in the admin
    def __str__(self):
        return self.group_name
    
class GroupMessage(models.Model):
    # this sets the group the message will be in
    group = models.ForeignKey(
        ChatGroup,
        related_name="chat_messages",
        on_delete=models.CASCADE)
    
    # this sets the author of the message
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # this sets the messages text amount
    body = models.CharField(max_length=300)

    # this sets the date the message was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    # within the admin it will displat the newly created messages first
    class Meta:
        ordering = ['-created']