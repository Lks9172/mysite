from django.db import models

#book:Wisesaying=1:n

class Book(models.Model):
    name = models.CharField(max_length=200)   #최대 길이를 정하고 작업 할시
    author = models.CharField(max_length=100)
    instroduce = models.CharField(max_length=200)

#그 책의 이름으로 인스턴스를 나타낸다.
    def __str__(self):
        return self.name

class Wisesaying(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()  #최대 길이를 정하기 애매할때

    def __str__(self):
        return self.text
