from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

# @api_view()

class HelloNews(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        
        url = 'https://feeds.npr.org/1004/feed.json'
        response = requests.get(url)
        data = response.json()["items"]
        data.sort(key=lambda new: new["date_published"],reverse=True)
        return Response(data)
        