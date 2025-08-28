import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from src.main import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"