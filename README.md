# fastapi-tests

python -m pip install fastapi uvicorn httpx pytest
npm install

uvicorn api:app --host 0.0.0.0 --port 8000

second terminal:
python -m pytest -v

python -m pytest tests/test_api.py -v

npx newman run postman/orders.postman_collection.json