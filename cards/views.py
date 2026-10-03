from django.shortcuts import render
from .models import Deck, Flashcard
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    if request.method == "POST":
        deck_form = NewDeckForm(request.POST)
        if deck_form.is_valid():
            deck_form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cards/create-deck.html",{
                "deck_form": deck_form
            })
    
    return render(request, "cards/create-deck.html", {
        "deck_form": NewDeckForm()
    })

def delete_deck(request, id):
    deck = Deck.objects.get(id=id)

    if request.method == "POST":
        deck.delete()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "cards/delete-deck.html", {
        "deck": deck
    })

def add_card(request, id):
    deck = Deck.objects.get(id=id)

    if request.method == "POST":
        card_form = NewCardForm(request.POST)

        if card_form.is_valid():
            new_card = card_form.save(commit=False)
            new_card.deck = deck
            new_card.save()
            return HttpResponseRedirect(reverse("deck", args=[id]))
        else:
            return render(request, "cards/add-card.html",{
                "card_form": card_form,
                "deck": deck,
            })
    
    return render(request, "cards/add-card.html", {
        "card_form": NewCardForm(),
        "deck": deck,
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

class NewCardForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = ["front", "back"]
        widgets = {
            "front": forms.TextInput(attrs={
                "placeholder": "Front",
            }),
            "back": forms.TextInput(attrs={
                "placeholder": "Back",
            })
        }