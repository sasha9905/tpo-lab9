# tpo-lab9 — CI для автотестов (ТПО)

Публичный репозиторий лабораторной работы № 9: запуск pytest в GitHub Actions.

## Структура
- `5/` — API-тесты (JSONPlaceholder)
- `6/` — unit-тесты Calculator
- `.github/workflows/run-tests.yml` — workflow

## Локально
```bash
pip install -r requirements.txt
pytest 5/ 6/ -v
```
