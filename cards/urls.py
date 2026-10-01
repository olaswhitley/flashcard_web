from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deck/<int:id>", views.deck, name="deck"),
    path("deck/create", views.create_deck, name="create_deck"),
]