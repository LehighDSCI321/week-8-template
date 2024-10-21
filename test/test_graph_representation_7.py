import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_simple_directed_graph():
    sd = SortableDigraph()
    sd.add_node("A")
    sd.add_node("B")
    sd.add_edge("A", "B")
    assert sd.top_sort() == ["A", "B"]
