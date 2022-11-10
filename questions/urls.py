from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename="questions")
router.register(r'answers', views.AnswerViewSet, basename="answers")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]