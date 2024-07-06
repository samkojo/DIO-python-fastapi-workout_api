# Projeto

## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI. É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER

![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Requisitos

- asdf
- Python (asdf)
- Poetry (asdf)
- Docker

## Funcionalidades (features)

- Atletas
  - [x] Consulta todas atletas
    - [ ] Permitir filtrar via parametros nome e cpf
    - [ ] Adicionar paginacao via parametros limit e offset
  - [x] Cria atleta
    - [ ] Retorno 303 caso campo unico ja exista com mesmo valor
  - [x] Consulta atleta via ID
  - [x] Alterar atleta via ID
  - [x] Deletar atleta via ID
- Categorias
  - [x] Consulta todas categorias
  - [x] Cria categoria
    - [ ] Retorno 303 caso campo unico ja exista com mesmo valor
  - [x] Consulta categoria via ID
- Centros de treinamento
  - [x] Consulta todos centros de treinamento
  - [x] Cria centros de treinamento
    - [ ] Retorno 303 caso campo unico ja exista com mesmo valor
  - [x] Consulta centros de treinamento via ID

## Execução da API

Instalar dependencias

```bash
make install
```

Sobe todos recursos necessarios e coloca API em funcionamento:

```bash
make run
```

## Execuções individuais

Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

## Referências

FastAPI: <https://fastapi.tiangolo.com/>

Pydantic: <https://docs.pydantic.dev/latest/>

SQLAlchemy: <https://docs.sqlalchemy.org/en/20/>

Alembic: <https://alembic.sqlalchemy.org/en/latest/>

Fastapi-pagination: <https://uriyyo-fastapi-pagination.netlify.app/>
