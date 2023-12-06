from django.shortcuts import render

def get_about(request):
    title = "Первый открытый алгоритм для подбора рифм"
    context = {"title": title}
    return render(request, "about.html", context)
