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
