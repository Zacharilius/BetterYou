from django.contrib import admin
from betterYouApp.models import UserProfile, Challenge, LikeChallenge, CompleteChallenges

admin.site.register(UserProfile)
admin.site.register(Challenge)
admin.site.register(LikeChallenge)
admin.site.register(CompleteChallenges)
