from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from maths.models import Math, Result
from maths.forms import ResultForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    print(f'****%%%%%%%***{wynik}')

    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c
    )


def sub(request, a, b):
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='sub', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c
    )


def mul(request, a, b):
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnozenie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='mul', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c
    )


def div(request, a, b):
    if int(b) == 0:
        wynik = "Error"
        messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")

    else:
        wynik = a / int(b)

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c)


@login_required
def maths_list(request):
    maths = Math.objects.all()
    paginator = Paginator(maths, 5)
    page_number = request.GET.get('page')
    maths = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths}
    )


def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/details.html",
        context={"math": math}
    )


def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)
        print(f'*******{form}')
        if form.is_valid():
            if form.cleaned_data['error'] == '':
                form.cleaned_data['error'] = None
            print(f'****%%%%%%%***{form.cleaned_data}')

            Result.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name="maths/results.html",
        context={
            "results": results,
            "form": form
        }
    )


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        maths = Math.objects.filter(operation__contains=searched)

        return render(request,
                      'maths/search.html',
                      {'searched': searched,
                       'maths': maths})
    else:
        return render(request,
                      'maths/search.html',
                      {})