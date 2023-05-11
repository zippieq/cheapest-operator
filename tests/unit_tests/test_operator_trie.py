import pytest
from utils.operator_trie import OperatorTrie

@pytest.fixture
def trie():
    return OperatorTrie()

def test_update(trie):
    # Test updating a word that doesn't exist in the trie
    trie.update('123', 'Operator1', 0.5)
    assert trie.search('123') == (0.5, 'Operator1', '123')

    # Test updating a word that already exists in the trie with a lower cost
    trie.update('123', 'Operator2', 0.3)
    assert trie.search('123') == (0.3, 'Operator2', '123')

    # Test updating a word that already exists in the trie with a higher cost
    trie.update('123', 'Operator3', 0.6)
    assert trie.search('123') == (0.3, 'Operator2', '123')

def test_search(trie):
    trie.update('123', 'Operator1', 0.5)
    trie.update('12', 'Operator2', 0.3)
    trie.update('234', 'Operator3', 0.2)

    # Test searching for a number that exists in the trie
    assert trie.search('123') == (0.5, 'Operator1', '123')

    # Test searching for a number that is a prefix of a word in the trie
    assert trie.search('12') == (0.3, 'Operator2', '12')

    # Test searching for a number that doesn't exist in the trie
    assert trie.search('456') == (None, None, '45')

def test_update_from_csv(trie):
    csv_data = [
        'Operator1:\n',
        '123,0.5\n',
        '12,0.3\n',
        'Operator2:\n',
        '234,0.2\n',
        'Operator3:\n',
        '456,0.6\n',
    ]
    trie.update_from_csv(csv_data)

    assert trie.search('123') == (0.5, 'Operator1', '123')
    assert trie.search('12') == (0.3, 'Operator1', '12')
    assert trie.search('234') == (0.2, 'Operator2', '234')
    assert trie.search('456') == (0.6, 'Operator3', '456')
