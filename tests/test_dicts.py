from utils.dicts import get_val


def test_dicts_alone():
    data = {"vcs": "mercurial"}
    assert get_val(data, "vcs") == 'mercurial'
    assert get_val(data, "vcs", "git") == 'mercurial'

def test_dicts_empty():
    assert get_val({}, "vcs", "git") == 'git'
    assert get_val({}, "vcs", "bazaar") == 'bazaar'

def test_dicts_many():
    data = {"abc": "abc_value", "def": "def_value"}
    assert get_val(data, "abc") == "abc_value"
    assert get_val(data, "def") == "def_value"
    assert get_val(data, "bce") == "git"
    assert get_val(data, "bce", "bazaar") == "bazaar"
