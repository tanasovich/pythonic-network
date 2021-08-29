from django.contrib.auth.models import User
from django.utils import timezone

from .models import Profile


class LastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            try:
                profile: Profile = Profile.objects.get(user=request.user.pk)
                profile.last_request = timezone.now()
                print(profile.last_request)
                profile.save()
            except Profile.DoesNotExist:
                profile = Profile(user=request.user, last_request=timezone.now())
                print(profile.last_request)
                profile.save()

        return response
