from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60) # 이름
    location = models.CharField(max_length=60) # 위치
    active = models.BooleanField(default=True)


    def __str__(self):
        # header name
        return self.name
    
class Book(models.Model): # Book Product
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name = "books")
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    shipping_cost = models.IntegerField()

    # positiveIntegerField : 양수
    quantity = models.PositiveIntegerField()

    def __str__(self):
        # book의 name(책 제목)과 Author class의 name(작가명)으로 가져옴
        return f"{self.name} by {self.author.name}"