import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from stack import Stack

def test_stack_push_pop():
    s = Stack()
    s.push(10)
    assert s.pop() == 10

def test_stack_empty_pop():
    s = Stack()
    assert s.pop() is None
