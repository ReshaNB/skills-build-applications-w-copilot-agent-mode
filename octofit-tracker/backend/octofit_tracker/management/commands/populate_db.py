from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], workout=workouts[0], date=timezone.now(), duration_minutes=30, score=50)
        Activity.objects.create(user=users[1], workout=workouts[1], date=timezone.now(), duration_minutes=45, score=80)
        Activity.objects.create(user=users[2], workout=workouts[0], date=timezone.now(), duration_minutes=25, score=40)
        Activity.objects.create(user=users[3], workout=workouts[1], date=timezone.now(), duration_minutes=60, score=100)

        # Create leaderboard
        for idx, user in enumerate(users, 1):
            total_score = sum(a.score for a in user.activities.all())
            Leaderboard.objects.create(user=user, total_score=total_score, rank=idx)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
