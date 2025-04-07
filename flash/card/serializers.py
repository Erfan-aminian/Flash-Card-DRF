from rest_framework import serializers
from .models import DeckModel, FlashCardModel

class DeckSerializer(serializers.ModelSerializer):
 class Meta:
     model = DeckModel
     fields = ('id', 'name', 'description', 'created',)

class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardModel
        fields = ('id', 'question', 'answer', 'deck', 'created_at')

