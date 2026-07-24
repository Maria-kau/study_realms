from django.contrib.auth.models import User
from django.test import TestCase

from .models import Avatar, Profile
from .services.avatrs import avatars_available


class AvatarAvailabilityTests(TestCase):
    def test_only_avatars_from_the_selected_character_gender_are_available(self):
        user = User.objects.create_user(username="teste", password="12345678")
        profile = Profile.objects.create(
            user=user,
            genero_personagem="feminino",
            classe="cavaleiro",
            level=10,
        )

        Avatar.objects.create(
            nome="Avatar Feminino",
            genero="feminino",
            classe="mago",
            level_minimo=1,
        )
        Avatar.objects.create(
            nome="Avatar Masculino",
            genero="masculino",
            classe="cavaleiro",
            level_minimo=1,
        )

        available_avatars = avatars_available(profile)

        self.assertTrue(available_avatars.filter(nome="Avatar Feminino").exists())
        self.assertFalse(available_avatars.filter(nome="Avatar Masculino").exists())

    def test_empty_character_gender_falls_back_to_default_avatar_gender(self):
        user = User.objects.create_user(username="teste2", password="12345678")
        profile = Profile.objects.create(
            user=user,
            genero_personagem="",
            classe="iniciante",
            level=1,
        )

        Avatar.objects.create(
            nome="Avatar Masculino",
            genero="masculino",
            classe="iniciante",
            level_minimo=1,
        )
        Avatar.objects.create(
            nome="Avatar Feminino",
            genero="feminino",
            classe="iniciante",
            level_minimo=1,
        )

        available_avatars = avatars_available(profile)

        self.assertTrue(available_avatars.filter(nome="Avatar Masculino").exists())
        self.assertFalse(available_avatars.filter(nome="Avatar Feminino").exists())
