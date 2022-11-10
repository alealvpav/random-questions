from random import randint

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question, Answer
from rest_framework import viewsets

from .serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        question = self.get_object()
        answers = question.answer_set.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def random(self, request):
        id = randint(1, self.queryset.count())
        question = self.queryset.get(pk=id)
        serializer = QuestionSerializer(question, many=False)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
