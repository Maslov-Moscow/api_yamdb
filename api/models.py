from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import math

from django.db import models



class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='category_titles')
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genres, blank=True)

    def __str__(self):
        return self.name



# Review и comments на основе моделей из проекта yatube
class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")
    title = models.ForeignKey(Titles, on_delete=models.CASCADE, related_name="review_title")
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comment_reviews")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)


class Rate(models.Model):
    title = models.ForeignKey(Titles, on_delete=models.CASCADE, related_name="rate_title")
    rate = models.FloatField(validators=[MinValueValidator(1.0),
                                         MaxValueValidator(10.0)])
    count = models.IntegerField()

    def rate_update(self, score):
        final_score = math.fsum([(self.rate * self.count), score]) / sum([self.count, 1])

        self.rate = final_score
        self.count += 1
        self.save()

    def __str__(self):
        return '%s: %.3d' % (self.title, self.rate)
