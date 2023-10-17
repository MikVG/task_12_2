import pytest

from utils.dicts import get_val


@pytest.fixture
def dicts_fixture():
    return {"abc": "abc_value", "def": "def_value"}


def test_dicts_alone():
    data = {"vcs": "mercurial"}
    assert get_val(data, "vcs") == 'mercurial'
    assert get_val(data, "vcs", "git") == 'mercurial'

def test_dicts_empty():
    assert get_val({}, "vcs", "git") == 'git'
    assert get_val({}, "vcs", "bazaar") == 'bazaar'

def test_dicts_many(dicts_fixture):
    assert get_val(dicts_fixture, "abc") == "abc_value"
    assert get_val(dicts_fixture, "def") == "def_value"
    assert get_val(dicts_fixture, "bce") == "git"
    assert get_val(dicts_fixture, "bce", "bazaar") == "bazaar"
