from src.stack import Stack


def test_stack_push_pop():
    s = Stack()
    s.push(10)
    assert s.pop() == 10
