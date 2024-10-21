import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_complex_graph():
    sd = SortableDigraph()
    nodes = ["shirt", "pants", "socks", "shoes", "belt", "jacket", "vest", "tie"]
    for node in nodes:
        sd.add_node(node)
    sd.add_edge("shirt", "pants")
    sd.add_edge("shirt", "vest")
    sd.add_edge("shirt", "tie")
    sd.add_edge("shirt", "jacket")
    sd.add_edge("vest", "jacket")
    sd.add_edge("socks", "shoes")
    sd.add_edge("pants", "belt")
    sd.add_edge("pants", "shoes")
    sd.add_edge("tie", "jacket")
    result = sd.top_sort()
    assert len(result) == len(nodes)
    assert result.index("shirt") < result.index("pants")
    assert result.index("shirt") < result.index("vest")
    assert result.index("shirt") < result.index("tie")
    assert result.index("shirt") < result.index("jacket")
    assert result.index("vest") < result.index("jacket")
    assert result.index("socks") < result.index("shoes")
    assert result.index("pants") < result.index("belt")
    assert result.index("pants") < result.index("shoes")
    assert result.index("tie") < result.index("jacket")

    