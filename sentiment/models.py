from django.db import models


class Search(models.Model):

    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Search"
        verbose_name_plural = "Searches"

    def __str__(self):
        return "%s - %s" % (self.keyword, self.date)


class Tweet(models.Model):

    search_id = models.ForeignKey(Search, on_delete=models.CASCADE)
    tweet_text = models.TextField()
    cleaned_text = models.TextField()
    polarity = models.FloatField(default=0)
    subjectivity = models.FloatField(default=0)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"

    def __str__(self):
        return "%s (polarity: %f, subjectivity: %f)" % (self.tweet_text, self.polarity, self.subjectivity)
