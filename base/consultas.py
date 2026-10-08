from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.

    stmt = select(Livro)

    for livro in session.execute(stmt).scalars().all():
        print(f"Titulo: {livro.titulo}, Autor: {livro.autor.nome}, Disponivel: {livro.disponivel}")




def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.

    stmt = select(Livro).where(Livro.disponivel == True)

    for livro in session.execute(stmt).scalars().all():
        print(f"Titulo: {livro.titulo}, Autor: {livro.autor.nome}, Disponivel: {livro.disponivel}")



def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.

    stmt = select(Livro).where(Livro.titulo.contains(trecho))

    for livro in session.execute(stmt).scalars().all():
        print(f"Titulo: {livro.titulo}, Autor: {livro.autor.nome}, Disponivel: {livro.disponivel}")




def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.

    stmt = select(Livro).join(Autor).where(Autor.nome == nome_autor)

    for livro in session.execute(stmt).scalars().all():
        print(f"TTitulo: {livro.titulo}, Autor: {livro.autor.nome}, Disponivel: {livro.disponivel}")
