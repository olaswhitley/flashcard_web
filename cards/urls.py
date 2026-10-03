from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deck/<int:id>", views.deck, name="deck"),
    path("deck/create", views.create_deck, name="create-deck"),
    path("deck/<int:id>/delete/", views.delete_deck, name="delete_deck"),
    path("deck/<int:id>/add/", views.add_card, name="add_card"),
]