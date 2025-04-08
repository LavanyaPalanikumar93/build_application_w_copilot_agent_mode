from django.core.management.base import BaseCommand 
from octofit.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        User.objects.create(id='1', email='student1@example.com', name='Student One')
        User.objects.create(id='2', email='student2@example.com', name='Student Two')

        # Populate teams
        Team.objects.create(id='1', name='Team Alpha', members=['1', '2'])

        # Populate activities
        Activity.objects.create(id='1', user_id='1', type='Running', duration=30, date='2025-04-07')
        Activity.objects.create(id='2', user_id='2', type='Cycling', duration=45, date='2025-04-07')

        # Populate leaderboard
        Leaderboard.objects.create(id='1', team_id='1', points=100)

        # Populate workouts
        Workout.objects.create(id='1', name='Push-ups', description='Do 20 push-ups')
        Workout.objects.create(id='2', name='Sit-ups', description='Do 30 sit-ups')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
