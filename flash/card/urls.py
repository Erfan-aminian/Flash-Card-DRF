from django.urls import path
from .views import DeckView
app_name = 'card'
urlpatterns = [
    path('deck/', DeckView.as_view(), name='deck'),
]