from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # データ削除
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # チーム作成
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # ユーザー作成
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

        # アクティビティ作成
        Activity.objects.create(user='Iron Man', type='run', duration=30)
        Activity.objects.create(user='Captain America', type='swim', duration=45)
        Activity.objects.create(user='Batman', type='cycle', duration=60)
        Activity.objects.create(user='Superman', type='fly', duration=120)

        # リーダーボード作成
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=180)

        # ワークアウト作成
        Workout.objects.create(name='Pushup', description='Do 20 pushups')
        Workout.objects.create(name='Situp', description='Do 30 situps')
        Workout.objects.create(name='Run', description='Run for 10 minutes')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
