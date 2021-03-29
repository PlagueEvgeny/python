from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import DialogMemebers


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def members(request, members_pk):
    member = DialogMemebers.objects.filter(member_id=members_pk)
    context = {
        'member': member,
        'page_title': 'Диалог'
    }
    return render(request, 'mainapp/members.html', context)
