from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import DialogMemebers, Message


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def message(request, message_pk):
    messages = Message.objects.filter(id=message_pk)
    context = {
        'messages': messages,
        'page_title': 'Диалог'
    }
    return render(request, 'mainapp/message.html', context)
