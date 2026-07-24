from biblioteca_realms.models import LibraryContent
# Criar conteúdo
def create_content(**dados):
    return LibraryContent.objects.create(**dados)


# Atualizar conteúdo
def update_content(conteudo, **dados):

    for campo, valor in dados.items():
        setattr(conteudo, campo, valor)

    conteudo.save()

    return conteudo


# Buscar conteúdo pelo ID
def get_content(content_id):
    return LibraryContent.objects.get(id=content_id)


# Listar todos os conteúdos
def list_contents():
    return LibraryContent.objects.all()


# Excluir conteúdo
def delete_content(conteudo):
    conteudo.delete()