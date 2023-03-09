import json

from django.core import serializers
from django.shortcuts import render
from django.utils.safestring import  mark_safe

from .models import Message

def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):

    messages = Message.objects.all()
    data = serializers.serialize("json", messages)

    context = {
        'room_name': room_name,
        'messages': data,
    }
    return render(request, 'chat/room.html', context)
