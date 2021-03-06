from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from html import escape
from sentiment.analyzer import analyze
from sentiment.models import Search, Tweet
from sentiment_analyzer.utils import get_client_ip


def index(request):
    client_ip = get_client_ip(request)

    if request.method == 'POST':
        query_text = request.POST.get('query').replace('#', '')
        result = analyze(query_text)
        search = Search()
        search.keyword = query_text
        search.save()

        polarities = []
        subjectivities = []
        labels = []
        for item in result:
            polarities.append(item[1].polarity)
            subjectivities.append(item[1].subjectivity)
            labels.append(item[0])
            tweet = Tweet()
            tweet.search_id = search
            tweet.tweet_text = item[0]
            tweet.polarity = item[1].polarity
            tweet.subjectivity = item[1].subjectivity
            print(tweet)
            tweet.save()

        result_dict = {"polarities": polarities, "subjectivities": subjectivities, "labels": labels}
        return render(request, 'sentiment/index.html', context={"result": result_dict, 'text': query_text})
        pass
    else:
        return render(request, 'sentiment/index.html')


def about(request):
    return render(request, 'sentiment/about.html')
