import pytest
from cTrie import Trie, TrieNode
from cQueue import Queue


t = Trie()


def test_insert():
    assert t.insert("Coco") == None
    assert t.insert("MacaCo") == None
    assert t.insert("Istambul") == None
    assert t.insert("join team") == None
    assert t.insert("join team maconcha") == None
    assert t.insert("juca me la pasa fisherman") == None
    assert t.insert("kill the fish") == None


@pytest.mark.parametrize(
    "prefix,expected",
    [
        ("coc", False),
        ("miaca", True),
        ("isTa", False),
        ("Estud", True),
        ("fish", False),
        ("the", False),
        ("kill t", True),
        ("team", False),
        ("join", False),
    ],
)
def test_search(prefix, expected):
    assert t.search_prefix(prefix) != expected


def test_get_words():
    assert t.get_words("fis") == ["fish", "fisherman"]
    assert t.get_words("mac") == ["macaco", "maconcha"]
    assert t.get_words("jo") == ["join"]
