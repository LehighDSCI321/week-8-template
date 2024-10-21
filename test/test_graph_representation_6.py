import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_single_node():
    sd = SortableDigraph()
    sd.add_node("A")
    assert sd.top_sort() == ["A"]
