from django.shortcuts import render


def error403(request, *args, **kwargs):
    return render(request, "content/errors/403.html")


def error404(request, *args, **kwargs):
    return render(request, "content/errors/404.html")


def error500(request, *args, **kwargs):
    return render(request, "content/errors/500.html")
