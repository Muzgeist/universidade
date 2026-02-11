# Projeto Universidade

Modelagem em orientaçao a Objetos das Entidades Alunos, Cursos, e Turmas

# Caso de Uso

```mermaid
flowchart LR
    Usuario([secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Alunos))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes

```mermaid
classDiagram
    class Aluno{
        - Nome
        - Email
        - CPF
        - Telefone
        - Endereço
        - Matricula
        + Cadastrar()
        + Editar()
        + transferir()
    }

```

## Dependencias
- **VSCode**: IDE (Interface de Desenvolvimento)
- **Mermaid**: Linguagem para Confecçao de Diagramas em Documentos .md (Mark Down)
- **Material icon theme**: tema para Colorir as Pastas.
- **GIt lens**: Interface Grafica para o Versionamento git integrado ao VSCode