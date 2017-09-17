## Simulador de cotações | VC-X Solutions

A aplicação deve calcular qual a melhor opção de plano dentre os oferecidos pela Operadora X. Desta forma, a informação de entrada será o consumo de um acesso (número) Y, através dos valores de consumo de dados (MB), ligações (minutos) e consumo de sms (qtd).

## Run Docker environment

### Installing dependencies

- Install [docker-compose](https://docs.docker.com/compose/install)

### Initialize environment

```
shell
# docker-compose up
```
At this time the aplication will be available in http://localhost:8000

### Access system shell

```
shell
# docker-compose exec vcx bash
```

### Run tests

```
shell
# docker-compose exec vcx make test
```

## Run without Docker

### Installing dependencies

```
shell
# make install
```

### Initialize environment

```
shell
# python3 manage.py runserver
```
At this time the aplication will be available in http://localhost:8000

### Run tests

```
shell
# make test
```
