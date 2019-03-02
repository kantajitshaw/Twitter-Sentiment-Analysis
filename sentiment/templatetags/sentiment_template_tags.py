from django import template
from sentiment.models import Search
from sentiment_analyzer.settings import DEBUG
from sentiment_analyzer.utils import get_trends_list_from_ip, get_client_ip

register = template.Library()


@register.inclusion_tag('sentiment/recents.html')
def get_recent_searches():
    return {'recent': Search.objects.all().order_by("-date")[:5]}
    # return {'recent': Search.objects.all().order_by("-date").distinct("keyword")[:5]}


@register.inclusion_tag('sentiment/trends.html', takes_context=True)
def get_recent_trends(context):
    if DEBUG:
        return {'trends': get_trends_list_from_ip()}
    else:
        return {'trends': get_trends_list_from_ip(get_client_ip(context["request"]))}
