from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)
    keyword = models.CharField(max_length=50, default="")

    def __str__(self):
        q_mark = "" if self.question[:-1] == "?" else "?"
        return f"{self.question}{q_mark}"


class Answer(models.Model):
    answer = models.TextField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    person = models.CharField(max_length=100, blank=True, default="Anonymous")

    def __str__(self):
        return f"\"{self.answer} ({self.person}).\""
