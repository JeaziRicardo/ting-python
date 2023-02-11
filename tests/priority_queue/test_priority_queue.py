from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue({"qtd_linhas": 10})
    pq.enqueue({"qtd_linhas": 2})
    pq.enqueue({"qtd_linhas": 11})
    pq.enqueue({"qtd_linhas": 3})

    assert len(pq.high_priority) == 2
    assert len(pq.regular_priority) == 2
    assert len(pq) == 4

    assert pq.search(0) == {"qtd_linhas": 2}

    assert pq.dequeue() == {"qtd_linhas": 2}
    assert len(pq) == 3

    with pytest.raises(AssertionError):
        assert pq.search(0) == {"qtd_linhas": 9}
    with pytest.raises(IndexError):
        pq.search(5) == {"qtd_linhas": 2}
