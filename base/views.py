from rest_framework import viewsets
from .models import UserProfile, StartupProfile
from .serializers import UserProfileSerializer, StartupProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class StartupProfileViewSet(viewsets.ModelViewSet):
    queryset = StartupProfile.objects.all()
    serializer_class = StartupProfileSerializer

# startup_finder/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import StartupProfile
from .serializers import StartupProfileSerializer

@api_view(['GET'])
def search_startups(request):
    skills = request.query_params.get('skills', '').split(',')
    country = request.query_params.get('country', '')

    # Filter startups based on skills and optional country match
    startups = StartupProfile.objects.filter(
        Q(skills_required__icontains=skills) |
        Q(description__icontains=skills)
    )

    if country:
        startups = startups.filter(address__icontains=country)

    serializer = StartupProfileSerializer(startups, many=True)
    return Response(serializer.data)
