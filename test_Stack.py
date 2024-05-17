import pytest
from Node import Node
from cStack import Stack


stack = Stack()


def test_peek():
    assert stack.isEmpty() == True
    assert stack.peek() == None


@pytest.mark.parametrize(
    "push,expected",
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
)
def test_push(push, expected):
    assert stack.push(push).value == expected


def test_pop():
    assert stack.pop().value == 7
    assert stack.Size() == 6
    assert stack.isEmpty() == False
    assert stack.peek().value == 6
    assert stack.pop().value == 6
    assert stack.pop().value == 5
    assert stack.pop().value == 4
    assert stack.pop().value == 3
    assert stack.Size() == 2
    assert stack.pop().value == 2
    assert stack.pop().value == 1
    assert stack.pop() == None
    stack.push("test_str")
    assert stack.peek().value == "test_str"
    assert stack.Size() == 1
    assert type(stack.peek()) == Node
