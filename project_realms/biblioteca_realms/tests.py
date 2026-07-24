import json

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from biblioteca_realms.models import LibraryContent, Module, Subject
from biblioteca_realms.views import (
    biblioteca,
    complete_content_view,
    content_update_views,
    subject_modules_view,
)


class BibliotecaViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", password="12345")
        self.subject = Subject.objects.create(nome="Matemática")
        self.other_subject = Subject.objects.create(nome="Física")
        self.module = Module.objects.create(nome="Módulo 1", materia=self.subject)
        self.content = LibraryContent.objects.create(
            user=self.user,
            titulo="Conteúdo de teste",
            descricao="Descrição",
            fonte="Fonte",
            materia=self.subject,
            modulo=self.module,
            categoria="video",
            dificuldade="medio",
            duracao=60,
        )

    def test_biblioteca_view_accepts_query_without_error(self):
        request = self.factory.get("/biblioteca/", {"q": "mat"})
        request.user = self.user

        response = biblioteca(request)

        self.assertEqual(response.status_code, 200)

    def test_content_update_views_updates_materia_using_id(self):
        request = self.factory.post(
            "/conteudo/atualizar/",
            {"materia": str(self.other_subject.id)},
        )
        request.user = self.user

        response = content_update_views(request, self.content.id)
        self.content.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.content.materia, self.other_subject)

    def test_complete_content_view_returns_module_and_subject_progress(self):
        request = self.factory.post(f"/conteudo/{self.content.id}/concluir/")
        request.user = self.user

        response = complete_content_view(request, self.content.id)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["module_progress"]["completed"], 1)
        self.assertEqual(data["subject_progress"]["completed"], 1)

    def test_subject_modules_view_renders_progress_bar_data(self):
        request = self.factory.get(f"/materia/{self.subject.id}/modulos/")
        request.user = self.user

        response = subject_modules_view(request, self.subject.id)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data-progress-key="module"')
        self.assertContains(response, 'data-progresso="0"')
        self.assertContains(response, 'style="width: 0%;"')
