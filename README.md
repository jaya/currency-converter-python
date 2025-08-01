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
to run migrations:
```shell
pip install -r requirements.txt
```
if you get a psycopg2 error it's require libpq-dev
```shell
apt install libpq-dev -y
```
to start the containers
```shell
docker-compose up -d
```
now run the migration
```shell
alembic upgrade head
```
now go to [http://localhost:8080/docs](http://localhost:8080/docs) and try the api through the swagger api or
```shell
curl -X 'POST' \
  'http://localhost:8080/transactions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "value": 10,
  "from_currency": "BRL",
  "to_currency": "USD",
  "user_id": 1
}'
```
for get transaction:
```shell
curl -X 'GET' \
  'http://localhost:4200/transactions?user_id=1' \
  -H 'accept: application/json'
```

### as a caveat i've included the kubernetes deployments.
just go to the deployment file on kubernetes/deployments line 72 and add you apikey base64 encoded
```shell
echo -n your_key | base64
```
```shell
kubectl apply -f kubernetes/
```
port forward the database
```shell
kubectl port-forward service/postgres-service 9000:8000
```
change your ENV VAR DATABASE_URL
```shell
export DATABASE_URL=postgresql+psycopg2://postgres:example@localhost:8000/postgres
```
run the migrations
```shell
alembic upgrade head
```
port forward the api
```shell
kubectl port-forward service/currency-converter-service 4200:8879
```
the service will be listen at 4200 port
