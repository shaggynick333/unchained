from django.contrib.auth import get_user.model

User = get_user_model()

random_user = User.objects.last()

#my followers
random_user.profile.followers.all()

#who i follow
random_user.is_following.all()