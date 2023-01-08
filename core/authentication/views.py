import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.authentication.permissions import HasAdminPermission
# from messages_api.models import Message
# from messages_api.serializers import MessageSerializer

# Create your views here.
oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


# class MessageApiView(RetrieveAPIView):
#     serializer_class = MessageSerializer
#     text = None

#     def get_object(self):
#         return Message(text=self.text)


# class PublicMessageApiView(MessageApiView):
#     text = "This is a public message."


# class ProtectedMessageApiView(MessageApiView):
#     text = "This is a protected message."
#     permission_classes = [IsAuthenticated]


# class AdminMessageApiView(MessageApiView):
#     text = "This is an admin message."
#     permission_classes = [IsAuthenticated, HasAdminPermission]

@permission_classes([IsAuthenticated])
def index(request):
    return render(
        request,
        "index.html",
        context={"session": request.session.get("user"), "pretty": json.dumps(request.session.get("user"), indent=4)},
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("authentication:index")))


def login(request):
    return oauth.auth0.authorize_redirect(request, request.build_absolute_uri(reverse("authentication:callback")))


def logout(request):
    request.session.clear()
    params = {
        "returnTo": request.build_absolute_uri(reverse("authentication:index")),
        "client_id": settings.AUTH0_CLIENT_ID,
    }
    return redirect(f"https://{settings.AUTH0_DOMAIN}/v2/logout?" + urlencode(params, quote_via=quote_plus))
