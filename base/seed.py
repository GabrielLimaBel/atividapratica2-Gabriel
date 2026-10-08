from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome="Alisson São Fernando", pais="Atlantida")
    autor2 = Autor(nome="Lucivania Rodrigues", pais="Alemanha")
    autor3 = Autor(nome="Manel da Cunha", pais="Espanh")

    # TODO: crie pelo menos 6 livros.
    livro1 = Livro(titulo="Biblia", ano=0, autor=autor1, disponivel=True)
    livro2 = Livro(titulo="Fharenrait", ano=2001, autor=autor2, disponivel=True)
    livro3 = Livro(titulo="Valorant o Livro", ano=2020, autor=autor3, disponivel=False)
    livro4 = Livro(titulo="resonancia suprema", ano=2015, autor=autor2, disponivel=True)
    livro5 = Livro(titulo="Romerito e a barba", ano=2026, autor=autor3, disponivel=True)
    livro6 = Livro(titulo="Calika", ano=2019, autor=autor1, disponivel=False)

    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    session.add_all([autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()
