from django.test import TestCase
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta


from .models import StudySession, Realm

from usuario_realms.models import Profile, Attributes

from usuario_realms.services.reward import reward_timer

from .services.realms import generate_realm

from .services.reset import reset_weekly_realm



class StudySessionModelTest(TestCase):


    def test_criar_sessao(self):

        user = User.objects.create_user(
            username="kau",
            password="12345678"
        )


        session = StudySession.objects.create(
            user=user,
            tipo="leitura",
            duracao=30,
            concluida=True,
            xp_ganho=20
        )


        self.assertEqual(
            session.user.username,
            "kau"
        )


        self.assertEqual(
            session.tipo,
            "leitura"
        )


        self.assertEqual(
            session.duracao,
            30
        )


        self.assertTrue(
            session.concluida
        )


        self.assertEqual(
            session.xp_ganho,
            20
        )



class RealmTest(TestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            username="teste",
            password="12345678"
        )



    def test_gerar_construcoes_com_tempo(self):

        generate_realm(
            self.user,
            60
        )


        realm = Realm.objects.get(
            user=self.user
        )


        self.assertEqual(
            realm.arvores,
            4
        )


        self.assertEqual(
            realm.casas,
            1
        )



class RewardTimerTest(TestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            username="timer_user",
            password="12345678"
        )


        Profile.objects.create(
            user=self.user
        )


        Attributes.objects.create(
            user=self.user
        )



    def test_timer_gera_recompensa(self):

        xp = reward_timer(
            self.user,
            "video_aula",
            60
        )


        self.assertEqual(
            xp,
            60
        )


        self.user.refresh_from_db()


        profile = self.user.profile


        self.assertGreater(
            profile.mana_xp,
            0
        )


        realm = self.user.realm


        self.assertEqual(
            realm.casas,
            1
        )



class RealmResetTest(TestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            username="reset_user",
            password="12345678"
        )



    def test_reset_semanal_reino(self):


        realm = Realm.objects.create(

            user=self.user,


            arvores=20,
            casas=5,
            especiais=2,
            castelos=1,


            total_arvores=100,
            total_casas=20,
            total_especiais=5,
            total_castelos=2,


            ultimo_reset=timezone.now() - timedelta(days=8)

        )


        reset_weekly_realm(
            realm
        )


        realm.refresh_from_db()



        self.assertEqual(
            realm.arvores,
            0
        )


        self.assertEqual(
            realm.casas,
            0
        )


        self.assertEqual(
            realm.especiais,
            0
        )


        self.assertEqual(
            realm.castelos,
            0
        )



        self.assertEqual(
            realm.total_arvores,
            100
        )


        self.assertEqual(
            realm.total_castelos,
            2
        )