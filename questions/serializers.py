from rest_framework.serializers import ModelSerializer

from questions.models import Question, Answer


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ["question"]


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ["answer", "person", "question"]
