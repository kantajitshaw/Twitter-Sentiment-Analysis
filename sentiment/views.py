from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from sentiment.analyzer import analyze


def index(request):
    if request.method == 'POST':
        query_text = request.POST.get('query')
        print("Query: ", str(query_text), len(query_text))
        result = analyze(query_text)
        return render(request, 'sentiment/index.html', context={"result": result})
        pass
    else:
        return render(request, 'sentiment/index.html')
