from django.contrib import admin
from betterYouApp.models import UserProfile, Challenge, LikedChallenge, CompletedChallenge

admin.site.register(UserProfile)
admin.site.register(Challenge)
admin.site.register(LikedChallenge)
admin.site.register(CompletedChallenge)
