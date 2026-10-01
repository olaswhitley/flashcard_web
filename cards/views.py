from django.shortcuts import render
from .models import Deck, Flashcard

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
    return render(request, "cards/create_deck.html")