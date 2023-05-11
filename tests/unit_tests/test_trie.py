import pytest
from utils.trie import OperatorTrie

@pytest.fixture
def trie():
    return OperatorTrie()

def test_update(trie):
    trie.update("123", "Operator 1:", 0.5)
    trie.update("12", "Operator 2:", 0.2)
    trie.update("1234", "Operator 3:", 0.8)

    assert trie.search("123") == (0.5, "Operator 1:", "123")
    assert trie.search("124") == (0.8, "Operator 3:", "12")
    assert trie.search("1") == (0.2, "Operator 2:", "1")

def test_search(trie):
    trie.update("123", "Operator 1:", 0.5)
    trie.update("12", "Operator 2:", 0.2)
    trie.update("1234", "Operator 3:", 0.8)

    assert trie.search("123") == (0.5, "Operator 1:", "123")
    assert trie.search("124") == (0.8, "Operator 3:", "12")
    assert trie.search("1") == (0.2, "Operator 2:", "1")
    assert trie.search("12345") == (None, None, "1234")
