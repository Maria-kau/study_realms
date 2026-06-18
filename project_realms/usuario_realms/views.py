from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

from .models import Profile, Attributes, Progress, FixaUsuario


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        # =========================
        # USER BASIC DATA
        # =========================
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # =========================
        # PERFIL DO USUÁRIO
        # =========================
        genero_usuario = request.POST.get("genero_usuario")
        genero_personagem = request.POST.get("genero_personagem")

        objetivo = request.POST.get("objetivo")
        curso = request.POST.get("curso")

        nivel_escolar = request.POST.get("nivel_escolar")
        turno_escolar = request.POST.get("turno_escolar")

        tipo_vestibular = request.POST.getlist("tipo_vestibular")
        tipo_universidades = request.POST.getlist("tipo_universidade")
        materia_dificuldade = request.POST.getlist("materia_dificuldade")

        # =========================
        # HORAS (SAFE)
        # =========================
        try:
            horas_estudos = int(request.POST.get("horas_estudos") or 0)
        except:
            horas_estudos = 0

        # =========================
        # CLEAN LISTS
        # =========================
        tipo_vestibular = [
            v.strip().lower()
            for v in tipo_vestibular
            if v and v.strip()
        ]

        tipo_universidades = [
            u.strip()
            for u in tipo_universidades
            if u and u.strip()
        ]

        materia_dificuldade = [
            m.strip().lower()
            for m in materia_dificuldade
            if m and m.strip()
        ]

        # =========================
        # VALIDATIONS
        # =========================
        errors = []

        if User.objects.filter(username=username).exists():
            errors.append("Usuário já existe!")

        if len(username) < 3:
            errors.append("Usuário muito pequeno!")

        if " " in username:
            errors.append("Usuário não pode ter espaços!")

        if User.objects.filter(email=email).exists():
            errors.append("Email já cadastrado!")

        if password != confirm_password:
            errors.append("As senhas não coincidem!")

        if len(password) < 8:
            errors.append("Senha muito fraca!")

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, "usuario_realms/cadastro.html", {
                "data": request.POST
            })

        # =========================
        # CREATE USER
        # =========================
        try:
            with transaction.atomic():

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                # =========================
                # FICHA DO USUÁRIO (REAL DATA)
                # =========================
                FixaUsuario.objects.create(
                    user=user,
                    genero_usuario=genero_usuario,
                    objetivo=objetivo,
                    tipo_vestibular=tipo_vestibular,
                    tipo_universidades=tipo_universidades,
                    curso=curso,
                    nivel_escolar=nivel_escolar,
                    horas_estudos=horas_estudos,
                    turno_escolar=turno_escolar,
                    materia_dificuldade=materia_dificuldade
                )

                # =========================
                # PROFILE (RPG SYSTEM)
                # =========================
                Profile.objects.create(
                    user=user,
                    genero_personagem=genero_personagem,
                    energia="nenhuma",
                    classe="iniciante",
                    level=1,
                    xp=0
                )

                # =========================
                # ATTRIBUTES
                # =========================
                Attributes.objects.create(user=user)

                # =========================
                # PROGRESS INIT
                # =========================
                materias = [
                    "matematica", "fisica", "quimica", "biologia",
                    "historia", "geografia", "sociologia", "filosofia",
                    "literatura", "gramatica", "ingles", "espanhol"
                ]

                for m in materias:
                    Progress.objects.create(
                        user=user,
                        materia=m
                    )

                messages.success(request, "Conta criada com sucesso!")
                return redirect("login")

        except Exception as e:
            print("ERROR:", e)
            messages.error(request, "Erro ao criar conta.")
            return render(request, "usuario_realms/cadastro.html", {
                "data": request.POST
            })

    return render(request, "usuario_realms/cadastro.html")