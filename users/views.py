from django.shortcuts import render

from users.models import UserModel


def winners_view(request):
    winners = UserModel.objects.all()
    context = {
        'user_list' : winners
    }
    return render(request, 'users.html', context=context)