from django.contrib import admin

from sentiment.models import Tweet, Search


class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'date')


class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet_text', 'polarity', 'subjectivity')


admin.site.register(Search, SearchAdmin)
admin.site.register(Tweet, TweetAdmin)
