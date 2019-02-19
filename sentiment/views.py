from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from html import escape

# Create your views here.
from sentiment.analyzer import analyze


def index(request):
    if request.method == 'POST':
        query_text = request.POST.get('query')
        result = analyze(query_text)
        polarities = []
        subjectivities = []
        labels = []
        for item in result:
            polarities.append(item[1].polarity)
            subjectivities.append(item[1].subjectivity)
            labels.append(item[0])
            # labels.append("\"" + escape(item[0], quote=False) + "\"")
        result_dict = {"polarities": polarities, "subjectivities": subjectivities, "labels": labels}
        return render(request, 'sentiment/index.html', context={"result": result_dict})
        pass
    else:
        return render(request, 'sentiment/index.html')
