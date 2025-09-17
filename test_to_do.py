import json
from to_do import read_json, write_json, create_new, mark_done
import builtins

def test_write_and_read_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data = {"Task1": {"description": "x", "is_done": False}}
    write_json(data)
    read = read_json()
    assert read == data

def test_create_new_creates_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    inputs = iter(["My Task", "A short desc"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    create_new()
    data = read_json()
    assert "My Task" in data
    assert data["My Task"]["description"] == "A short desc"
    assert data["My Task"]["is_done"] is False

def test_mark_done_marks(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data = {"T": {"description": "d", "is_done": False}}
    write_json(data)
    inputs = iter(["T"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    mark_done()
    data2 = read_json()
    assert data2["T"]["is_done"] is True
