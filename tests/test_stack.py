from src.stack import Stack

def test_stack():
    s=Stack()
    s.push(10)
    assert s.pop() == 10
    