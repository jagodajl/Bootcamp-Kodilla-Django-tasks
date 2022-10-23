from django.shortcuts import render


def welcome(request):
    return render(
        request=request,
        template_name="greetings/main.html",
        context=None)


def contact(request):
    return render(
        request=request,
        template_name="greetings/about.html",
        context=None)


def about(request):
    return render(
        request=request,
        template_name="greetings/contact.html",
        context=None)
