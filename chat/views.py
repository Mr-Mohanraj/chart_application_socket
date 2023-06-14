from django.shortcuts import render
from .models import User

def index(request):
    print(request.POST)
    if request.method == "POST":
        user = User(username=request.POST["user"], roomName=request.POST['room'])
        user.save()
        cont = {"user_name":user.username, "room_name":user.roomName}
        return render(request, 'chat/room.html', context=cont)
    else:
        return render(request, 'chat/index.html')

def room(request, room_name, user_name):
    user = User.objects.filter(roomName=room_name)
    if user.exists():
        return render(request, 'chat/room.html', {
            "user_name":user_name,
            'room_name': room_name
        })
    else:
        return render(request, 'chat/room.html', {
            "error":"please provide the username and room name exiting one"
        })