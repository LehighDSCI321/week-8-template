import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_multiple_starting_nodes():
    sd = SortableDigraph()
    sd.add_node("A")
    sd.add_node("B")
    sd.add_node("C")
    sd.add_edge("A", "C")
    sd.add_edge("B", "C")
    result = sd.top_sort()
    assert result.index("A") < result.index("C")
    assert result.index("B") < result.index("C")
    
    