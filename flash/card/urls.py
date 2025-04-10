from django.urls import path
from .views import DeckView, DeckDetailView, FlashCardView, FlashCardDetailView
app_name = 'card'
urlpatterns = [
    path('decks/', DeckView.as_view(), name='deck'),
    path('decks/<int:id>/', DeckDetailView.as_view(), name='deck_detail'),
    path('cards/', FlashCardView.as_view(), name='flashcards'),
    path('cards/<int:id>/', FlashCardDetailView.as_view(), name='card_detail'),

]