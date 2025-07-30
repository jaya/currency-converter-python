#!/usr/bin/env bash

echo "Iniciando aplicação FastAPI no ambiente: $ENV"

if [ "$ENV" = "dev" ]; then
  echo "Rodando em modo desenvolvimento (uvicorn)"
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

elif [ "$ENV" = "dev-debug" ]; then
  echo "Rodando em modo debug com debugpy"
  pip install debugpy -t /tmp
  python3 /tmp/debugpy --listen 0.0.0.0:5678 --wait-for-client \
    -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

else
  echo "Rodando em modo produção com gunicorn"
  gunicorn app.main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers "${AMOUNT_WORKERS:-4}" \
    --threads "${AMOUNT_THREADS:-2}" \
    --bind 0.0.0.0:8000 \
    --timeout "${TIMEOUT:-60}"
fi
