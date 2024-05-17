import pytest
from Node import Node
from Stack import Stack


node1 = Node()
node1.value = 1
node2 = Node()
node2.value = 2
node3 = Node()
node3.value = 3
node4 = Node()
node4.value = 4
node5 = Node()
node5.value = 5
node6 = Node()
node6.value = 6
node7 = Node()
node7.value = 7
node9 = Node()
node9.value = 9
node8 = Node()
node8.value = 8
node9 = Node()
node9.value = "test_str"
lista_nodes = [node1, node2, node3, node4, node5]

stack = Stack()


def test_peek():
    assert stack.isEmpty() == True
    assert stack.peek() == None


@pytest.mark.parametrize(
    "push,expected",
    [
        (node1, node1),
        (node2, node2),
        (node3, node3),
        (node4, node4),
        (node5, node5),
        (node6, node6),
        (node7, node7),
        (8, TypeError),
    ],
)
def test_push(push, expected):
    assert stack.push(push) == expected


def test_pop():
    assert stack.pop() == node7
    assert stack.Size() == 6
    assert stack.isEmpty() == False
    assert stack.peek() == node6
    assert stack.pop() == node6
    assert stack.pop() == node5
    assert stack.pop() == node4
    assert stack.pop() == node3
    assert stack.Size() == 2
    assert stack.pop() == node2
    assert stack.pop() == node1
    assert stack.pop() == None
    stack.push(node9)
    assert stack.peek().value == "test_str"
    assert stack.Size() == 1
