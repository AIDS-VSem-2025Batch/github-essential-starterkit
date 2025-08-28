import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sourcefiles')))
from sourcefiles.main import reverse_string

def test_reverse_string():
    assert reverse_string.reverse_string("hello") == "olleh"