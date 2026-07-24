# ==========================================================
# IMPORTS
# ==========================================================
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

from .models import (
    Profile,
    Attributes,
    Progress,
    FixaUsuario,
    Avatar
)
from .services.player_date import get_player_data
from .services import (
    avatars_available,update_class
)

def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        # =========================
        # USER BASIC DATA (SAFE)
        # =========================
        username = (request.POST.get("username") or "").strip()
        email = (request.POST.get("email") or "").strip()
        password = (request.POST.get("password") or "").strip()
        confirm_password = (request.POST.get("confirm_password") or "").strip()

        # =========================
        # PERFIL DO USUÁRIO
        # =========================
        genero_usuario = (request.POST.get("genero_usuario") or "").strip()
        genero_personagem = (request.POST.get("genero_personagem") or "").strip()

        objetivo = (request.POST.get("objetivo") or "").strip()
        curso = (request.POST.get("curso") or "").strip()

        nivel_escolar = (request.POST.get("nivel_escolar") or "").strip()
        turno_escolar = (request.POST.get("turno_escolar") or "").strip()

        tipo_vestibular = request.POST.getlist("tipo_vestibular")
        tipo_universidade = request.POST.getlist("tipo_universidades")
        materia_dificuldade = request.POST.getlist("materia_dificuldade")

        # =========================
        # HORAS SAFE
        # =========================
        try:
            horas_estudos = int(request.POST.get("horas_estudos") or 0)
        except ValueError:
            horas_estudos = 0

        # =========================
        # CLEAN LISTS
        # =========================
        tipo_vestibular = [v.strip().lower() for v in tipo_vestibular if v and v.strip()]
        tipo_universidade = [u.strip() for u in tipo_universidade if u and u.strip()]
        materia_dificuldade = [m.strip().lower() for m in materia_dificuldade if m and m.strip()]

        genero_choices = {choice[0] for choice in FixaUsuario.GENERO_USUARIO_CHOICES}
        objetivo_choices = {choice[0] for choice in FixaUsuario.OBJETIVO_CHOICES}
        nivel_choices = {choice[0] for choice in FixaUsuario.NIVEL_ESCOLAR_CHOICES}
        turno_choices = {choice[0] for choice in FixaUsuario.TURNO_ESCOLAR_CHOICES}

        if genero_usuario not in genero_choices:
            genero_usuario = "masculino"

        if objetivo not in objetivo_choices:
            objetivo = "outro"

        if nivel_escolar not in nivel_choices:
            nivel_escolar = "1_em"

        if turno_escolar not in turno_choices:
            turno_escolar = "flexivel"

        if genero_personagem not in {choice[0] for choice in Profile.GENERO_PERSONAGEM_CHOICES}:
            genero_personagem = "masculino"

        # =========================
        # VALIDATIONS
        # =========================
        errors = []

        # obrigatórios primeiro
        if not username:
            errors.append("Usuário é obrigatório!")

        if not email:
            errors.append("Email é obrigatório!")

        if not password:
            errors.append("Senha é obrigatória!")

        if not confirm_password:
            errors.append("Confirmação de senha é obrigatória!")

        # só continua se já tem algo
        if username and len(username) < 3:
            errors.append("Usuário muito pequeno!")

        if username and " " in username:
            errors.append("Usuário não pode ter espaços!")

        if username and User.objects.filter(username=username).exists():
            errors.append("Usuário já existe!")

        if email and User.objects.filter(email=email).exists():
            errors.append("Email já cadastrado!")

        # senha só valida se existir
        if password:
            if len(password) < 8:
                errors.append("Senha muito fraca!")

            if not any(c.isupper() for c in password):
                errors.append("A senha deve conter pelo menos uma letra maiúscula.")

            if not any(c.islower() for c in password):
                errors.append("A senha deve conter pelo menos uma letra minúscula.")

            if not any(c.isdigit() for c in password):
                errors.append("A senha deve conter pelo menos um número.")

            caracteres = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
            if not any(c in caracteres for c in password):
                errors.append("A senha deve conter pelo menos um caractere especial.")

        if password and confirm_password and password != confirm_password:
            errors.append("As senhas não coincidem!")

        # =========================
        # RETURN ERRORS
        # =========================
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


                FixaUsuario.objects.create(
                    user=user,
                    genero_usuario=genero_usuario,
                    objetivo=objetivo,
                    tipo_vestibular=tipo_vestibular,
                    tipo_universidade=tipo_universidade,
                    curso=curso,
                    nivel_escolar=nivel_escolar,
                    horas_estudos=horas_estudos,
                    turno_escolar=turno_escolar,
                    materia_dificuldade=materia_dificuldade
                )


                profile = Profile.objects.create(
                    user=user,
                    genero_personagem=genero_personagem,
                    energia="nenhuma",
                    classe="iniciante",
                    level=1,
                    xp=1,
                    
                )

                # avatar
                try:
                    if genero_personagem == "masculino":
                        avatar_padrao = Avatar.objects.get(
                            nome="Noah",
                            genero="masculino",
                            classe="iniciante"
                        )
                    else:
                        avatar_padrao = Avatar.objects.get(
                            nome="kiara",
                            genero="feminino",
                            classe="iniciante"
                        )
                except Avatar.DoesNotExist:
                    avatar_padrao = Avatar.objects.filter(
                        genero=("masculino" if genero_personagem == "masculino" else "feminino"),
                        classe="iniciante"
                    ).first()

                if avatar_padrao:
                    profile.avatar = avatar_padrao

                profile.save()

                attributes = Attributes.objects.create(user=user)
                update_class(profile, attributes)

                materias = [
                    "matematica", "fisica", "quimica", "biologia",
                    "historia", "geografia", "sociologia", "filosofia",
                    "literatura", "gramatica", "ingles", "espanhol"
                ]

                for m in materias:
                    Progress.objects.create(user=user, materia=m)

                messages.success(request, "Conta criada com sucesso!")
                return redirect("login")

        except Exception as e:
            print("ERROR:", e)
            messages.error(request, f"Erro ao criar conta: {e}")
            return render(request, "usuario_realms/cadastro.html", {
                "data": request.POST
            })

    return render(request, "usuario_realms/cadastro.html")

# ==========================================================
# LOGIN
# ==========================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Preencha todos os campos!")
            return redirect("login")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("home")

        messages.error(request, "Usuário ou senha inválidos!")
        return redirect("login")

    return render(request, "usuario_realms/login.html")
# ==========================================================
# RESET PASSWORD (VERSÃO MAIS SEGURA)
# ==========================================================
def reset_password(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        new_password = request.POST.get("new_password", "")
        confirm_password = request.POST.get("confirm_password", "")
        # =========================
        # SENHAS DIFERENTES
        # =========================
        if new_password != confirm_password:
            messages.error(
                request,
                "As senhas não coincidem!"
            )
            return redirect("reset_password")
        # =========================
        # BUSCA USUÁRIO
        # =========================
        try:
            user = User.objects.get(
                username=username
            )
        except User.DoesNotExist:
            messages.error(
                request,
                "Usuário não encontrado!"
            )
            return redirect("reset_password")
        # =========================
        # VERIFICA EMAIL
        # =========================
        if user.email != email:
            messages.error(
                request,
                "Email incorreto!"
            )
            return redirect("reset_password")
        # =========================
        # VALIDA SENHA
        # =========================
        if len(new_password) < 8:
            messages.error(request, "A senha deve ter pelo menos 8 caracteres.")
            return redirect("reset_password")

        if not any(c.isupper() for c in new_password):
            messages.error(request, "A senha deve conter uma letra maiúscula.")
            return redirect("reset_password")

        if not any(c.islower() for c in new_password):
            messages.error(request, "A senha deve conter uma letra minúscula.")
            return redirect("reset_password")

        if not any(c.isdigit() for c in new_password):
            messages.error(request, "A senha deve conter um número.")
            return redirect("reset_password")

        caracteres = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

        if not any(c in caracteres for c in new_password):
            messages.error(request, "A senha deve conter um caractere especial.")
            return redirect("reset_password")
        # =========================
        # ALTERA SENHA
        # =========================
        user.set_password(new_password)
        user.save()
        messages.success(
            request,
            "Senha alterada com sucesso!"
        )

        return redirect("login")
    return render(
        request,
        "usuario_realms/reset_password.html"
    )
# ==========================================================
# PERFIL
# ==========================================================

@login_required
def perfil(request):

    context = get_player_data(request.user)

    return render(
        request,
        "usuario_realms/perfil.html",
        context
    )
# ==========================================================
# LOGOUT
# ==========================================================
@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return redirect("login")

# ==========================================================
# ESCOLHER AVATAR
# ==========================================================
# ==========================================================
# PÁGINA ESCOLHER AVATAR
# ==========================================================

@login_required
def avatar_view(request):

    profile = request.user.profile
    avatars = avatars_available(profile)

    return render(
        request,
        "usuario_realms/avatar.html",
        {
            "avatars": avatars
        }
    )
# ==========================================================
# SALVAR AVATAR
# ==========================================================

@login_required
def escolher_avatar(request):
    if request.method != "POST":
        return redirect("perfil")

    profile = request.user.profile
    avatar_id = request.POST.get("avatar")

    try:
        # Buscamos diretamente na tabela Avatar, mas filtrando pelo ID, 
        # pelo gênero do personagem e pelo nível mínimo permitido!
        avatar = Avatar.objects.get(
            id=avatar_id,
            genero=profile.genero_personagem,
            level_minimo__lte=profile.level
        )

    except Avatar.DoesNotExist:
        messages.error(
            request,
            "Avatar inválido ou não disponível para o seu nível/gênero."
        )
        return redirect("avatar") # Redireciona para a página de listagem (ajuste o nome da rota se necessário)

    # Se passou na validação, salva o avatar no perfil
    profile.avatar = avatar
    profile.save()

    messages.success(
        request,
        "Avatar atualizado com sucesso!"
    )

    return redirect("perfil")