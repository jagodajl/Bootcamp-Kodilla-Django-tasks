# maths/views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
#
#
# def math(request):
#     return HttpResponse("Tu będzie matma")
#
#
# def add(request, a, b):
#     a, b = int(a), int(b)
#     wynik = a + b
#     t = loader.get_template("maths/operation.html")
#     c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
#     return HttpResponse(t.render(c))
#
#
# def sub(request, a, b):
#     a, b = int(a), int(b)
#     return HttpResponse(a - b)
#
#
# def mul(request, a, b):
#     a, b = int(a), int(b)
#     return HttpResponse(a * b)
#
#
# def div(request, a, b):
#     a, b = int(a), int(b)
#     if b == 0:
#         return HttpResponse("Nie dziel przez 0")
#     return HttpResponse(a / b)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )


def sub(request, a, b):
    a, b = int(a), int(b)
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )


def mul(request, a, b):
    a, b = int(a), int(b)
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )


def div(request, a, b):
    a, b = int(a), int(b)
    wynik = a / b
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )
