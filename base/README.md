# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
O 'disponivel' diz se o livro pode ser emprestado ou não. Quando está True, ele está disponivel, quando vira False, já foi emprestado.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
O session.commit() salva a mudança no banco de dados. Sem ele, o python so altera o objeto na memória e a alteração não fica regitrada.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
a consulta que usa o relacionamento entre Livro e Autor é listar_livros_por_autor, em consultas.py. Ela junta Livro com Autor e filtra pelo nome do autor.