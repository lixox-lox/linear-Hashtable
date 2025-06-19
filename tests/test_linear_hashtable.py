import importlib.util
import pathlib
import pytest

# Load the module using its file path because the filename contains a hyphen
MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "linear-Hashtable.py"
_spec = importlib.util.spec_from_file_location("linear_hashing", MODULE_PATH)
linear_hashing = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(linear_hashing)
LinearHashing = linear_hashing.LinearHashing

class Data:
    def __init__(self, key):
        self.key = key


def test_insert_and_search_basic():
    lh = LinearHashing(5)
    assert lh.insert(1) is True
    assert lh.search(1) is True
    # inserting duplicate key should fail
    assert lh.insert(1) is False
    # searching for absent key returns False
    assert lh.search(2) is False


def test_insert_with_object_and_delete():
    lh = LinearHashing(5)
    obj = Data(3)
    assert lh.insert(obj) is True
    assert lh.search(3) is True
    # delete using the same object
    assert lh.delete(obj) is True
    assert lh.search(3) is False


def test_locate_and_delete_gaps_filled():
    lh = LinearHashing(5)
    lh.insert(1)
    lh.insert(6)  # collides with key 1 (since 6 % 5 == 1)
    assert lh.locate(1) == 1
    assert lh.locate(6) == 6
    # deleting 1 should trigger gap filling, keeping key 6 reachable
    assert lh.delete(1) is True
    assert lh.search(6) is True
    assert lh.locate(6) == 6
    with pytest.raises(KeyError):
        lh.locate(1)


def test_type_errors():
    lh = LinearHashing(5)
    with pytest.raises(TypeError):
        lh.insert("a")
    lh.insert(2)
    with pytest.raises(TypeError):
        lh.search("a")
    with pytest.raises(TypeError):
        lh.locate("a")
    with pytest.raises(TypeError):
        lh.delete("a")
