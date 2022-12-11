from django.shortcuts import render
from django.http import request, HttpResponse
from django.template import loader
<<<<<<< HEAD
from .forms import StressVariantsForm, DepthTimeForm
=======
from .forms import StressVariantsForm
>>>>>>> 26e9964edea31fb01fb9c5e2190530ae0e3952f9
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def title(request):
    if request.method == "POST":
<<<<<<< HEAD
        # form = StressVariantsForm(request.POST)
        form_2 = DepthTimeForm(request.POST)
        if form_2.is_valid:
            HttpResponseRedirect("results/")
    else:
        form = StressVariantsForm()
        form_2 = DepthTimeForm()
    return render(request, "title.html", {"form": form, "form_2": form_2})
=======
        form = StressVariantsForm(request.POST)
        if form.is_valid:
            HttpResponseRedirect("results/")
    else:
        form = StressVariantsForm()
    return render(request, "title.html", {"form": form})
>>>>>>> 26e9964edea31fb01fb9c5e2190530ae0e3952f9


def results(request):
    table_of_results = list(request.POST.values())[1]
    return render(request, "results.html", {"table_of_results": table_of_results})
