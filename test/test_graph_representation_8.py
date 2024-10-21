import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_multiple_nodes_one_dependency():
    sd = SortableDigraph()
    sd.add_node("A")
    sd.add_node("B")
    sd.add_node("C")
    sd.add_edge("A", "B")
    sd.add_edge("A", "C")
    result = sd.top_sort()
    assert result == ["A", "B", "C"] or result == ["A", "C", "B"]
    