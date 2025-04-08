from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class api_root(APIView):
    def get(self, request):
        return Response({
            'users': '/users/',
            'teams': '/teams/',
            'activity': '/activity/',
            'leaderboard': '/leaderboard/',
            'workouts': '/workouts/',
        })

class UserList(APIView):
    def get(self, request):
        return Response([])

class TeamList(APIView):
    def get(self, request):
        return Response([])

class ActivityList(APIView):
    def get(self, request):
        return Response([])

class LeaderboardList(APIView):
    def get(self, request):
        return Response([])

class WorkoutList(APIView):
    def get(self, request):
        return Response([])