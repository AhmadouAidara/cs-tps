from algo.tp1_hash_tables.implementations import ListContainer, SetContainer
from algo.tp1_hash_tables.hashtable import (
    HashTableContainer,
    ResizingHashTableContainer,
    LinkedListHashTableContainer,
)
import random
def _smoke(c):
    xs = list(range(200))
    random.shuffle(xs)
    for x in xs:
        c.add(x)
    assert all(x in c for x in xs)
    assert len(c) == len(set(xs))
    # duplicates do not increase size
    for x in xs[:50]:
        c.add(x)
    assert len(c) == len(set(xs))

def test_list_container():
    _smoke(ListContainer())

def test_set_container():
    _smoke(SetContainer())

def test_ht_fixed():
    _smoke(HashTableContainer(m=8))  # small m to force collisions

def test_ht_resizing():
    _smoke(ResizingHashTableContainer(m=4, max_load=0.75))

def test_ht_linked():
    _smoke(LinkedListHashTableContainer(m=8))