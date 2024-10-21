import subprocess
import re
import pytest

from student_code import SortableDigraph

def test_empty_graph():
    sd = SortableDigraph()
    assert sd.top_sort() == []
