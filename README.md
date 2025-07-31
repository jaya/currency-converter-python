### To run this project you MUST have

* [python3](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* [docker](https://docs.docker.com/engine/install/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [make](https://www.gnu.org/software/make/)

 you must export this env var to run migrations in your database this example uses the database define in the docker-compose
```shell
export DATABASE_URL=postgresql+psycopg2://postgres:example@localhost:5432/postgres
```

you must also export the currency_api_key
```shell
export CURRENCY_KEY=your_key
```
