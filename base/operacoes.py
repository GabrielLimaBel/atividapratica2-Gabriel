from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""

    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.execute(stmt).scalars().first()

    if not livro:
        print("Livro não encontrado.")
        return

    if not livro.disponivel:
        print("Livro já está emprestado.")
        return

    livro.disponivel = False
    session.commit()


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""

    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.execute(stmt).scalars().first()

    if not session.execute(stmt).scalars().first():
        print("Livro não encontrado.")
        return

    if livro.disponivel:
        print("Livro já está disponível.")
        return

    livro.disponivel = True
    session.commit()
