from datetime import datetime

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Word
from .serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).order_by('word')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer)

    def get_by_word(self, request, word):
        try:
            exact_word = Word.objects.get(word=word)
            serializer = self.get_serializer(exact_word)
            return Response(serializer.data)
        except Word.DoesNotExist:
            raise Http404("Word does not exist")

    def get_single_word(self, request):
        single_word = Word.objects.order_by('?').first()
        if single_word:
            serializer = self.get_serializer(single_word)
            return Response(serializer.data)
        else:
            return Response({"message": "No words available"}, status=status.HTTP_404_NOT_FOUND)