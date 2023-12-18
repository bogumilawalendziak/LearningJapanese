from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Word
from .serializers import WordSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def create(self, request):
        modified = {
            "word": request.data.get("word"),
            "definition": request.data.get("definition"),
            "example": request.data.get("example"),
            "translation": request.data.get("translation"),
            "pronunciation": request.data.get("pronunciation"),
        }

        word_instance = Word(modified)
        serializer = self.get_serializer(word_instance)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def createList(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
