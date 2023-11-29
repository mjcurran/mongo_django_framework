from django.shortcuts import render


def index(request):
    return render(request, "rh_app/index.html")


def room(request, room_name):
    return render(request, "rh_app/room.html", {"room_name": room_name})