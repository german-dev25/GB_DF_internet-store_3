import requests
from django.db import transaction
from social_core.exceptions import AuthForbidden


@transaction.atomic
def get_user_location_and_bio_git(backend, user, response, *args, **kwargs):
    resp = requests.get(
        "http://api.github.com/user",
        headers={"Authorization": "token %s" % response["access_token"]},
    )
    json = resp.json()

    user.city = json['location']
    user.profile.about = json['bio']
    user.save()

    if not json['location']:
        raise AuthForbidden("social_core.backends.github.GithubOAuth2")


@transaction.atomic
def get_user_location_and_bio_google(backend, user, response, *args, **kwargs):
    resp = requests.get(
        "http://api.github.com/user",
        headers={"Authorization": "token %s" % response["access_token"]},
    )
    json = resp.json()

    user.city = json['location']
    user.profile.about = json['bio']
    user.save()

    if not json['location']:
        raise AuthForbidden("social_core.backends.github.GithubOAuth2")
