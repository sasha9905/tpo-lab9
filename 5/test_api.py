"""Автотесты REST API (requests + pytest), логика как в Postman."""
import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_get_user():
    r = requests.get(f"{BASE}/users/1", timeout=15)
    assert r.status_code == 200
    data = r.json()
    assert "id" in data and data["id"] == 1
    assert "email" in data and "@" in data["email"]
    assert "name" in data


def test_post_user():
    payload = {"name": "Alex Test", "username": "alext", "email": "alex@test.com"}
    r = requests.post(f"{BASE}/users", json=payload, timeout=15)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == payload["name"]
    assert "id" in data


def test_put_user():
    payload = {"id": 1, "name": "Updated", "username": "upd", "email": "u@test.com"}
    r = requests.put(f"{BASE}/users/1", json=payload, timeout=15)
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Updated"
    assert data["id"] == 1
