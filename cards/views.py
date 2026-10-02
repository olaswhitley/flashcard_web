from django.shortcuts import render
from .models import Deck, Flashcard
from django import forms
from django.forms import ModelForm

# Create your views here.

def index(request):
    return render(request, "cards/index.html", {
        "decks": Deck.objects.all()
    })

def deck(request, id):
    deck = Deck.objects.get(id=id)
    cards = deck.flashcards.all()

    return render(request, "cards/deck.html", {
        "deck": deck,
        "cards": cards
    })

def create_deck(request):
    return render(request, "cards/create-deck.html", {
        "deck_form": NewDeckForm()
    })

# Forms
class NewDeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Name",
            }),
        }