from django.core.serializers import serialize
from django.http import Http404
from django.shortcuts import render
from .serializers import DeckSerializer, FlashCardSerializer
from .models import DeckModel, FlashCardModel
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class DeckView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        decks = DeckModel.objects.filter(user=request.user)
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeckDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk, user):
        try:
            return DeckModel.objects.get(pk=pk, user=user)
        except DeckModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        deck = self.get_object(pk, request.user)
        serializer = DeckSerializer(deck)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        deck = self.get_object(pk, request.user)
        serializer = DeckSerializer(deck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        deck = self.get_object(pk, request.user)
        deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FlashCardView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        cards = FlashCardModel.objects.filter(deck__user =request.user)
        serializer = FlashCardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FlashCardSerializer(data=request.data)
        if serializer.is_valid():
            deck = DeckModel.objects.get(pk=serializer.data['deck'].pk)
            if deck.user != request.user:
                return Response({'error':'not allowed'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashCardDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, id, user):
        try:
            return FlashCardModel.objects.get(id=pk, user=user)
        except FlashCardModel.DoesNotExist:
            raise Http404

    def get(self, request, id):
        card = FlashCardModel.objects.get(id=id, user=request.user)
        serializer = FlashCardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        card = FlashCardModel.objects.get(id=id, user=request.user)
        serializer = FlashCardSerializer(card , data=request.data)
        if serializer.is_valid():
            deck = DeckModel.objects.get(id=serializer.validated_data['deck'].id)
            if deck.user != request.user:
                return Response({'error':'not allowed'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        card = FlashCardModel.objects.get(id=id, user=request.user)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)