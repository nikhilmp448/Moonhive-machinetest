# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path not in [reverse('login')]:
            return redirect('login')  # Redirect to the login page

        response = self.get_response(request)
        return response
