from django.shortcuts import render

def Welcome(request):
    return render(request,"index.html")
    # By default "get" request

def User(request):
    username = request.GET["username"]
    print(username)
    return render(request, "user.html",{'name':username})