import subprocess
import re
import pytest

from student_code import SortableDigraph,VersatileDigraph

def test_inheritance_and_methods():
    sd = SortableDigraph()
    # Ensure inheritance
    assert isinstance(sd, VersatileDigraph)
    
    # Ensure only specified methods are implemented in SortableDigraph
    expected_methods = ['__init__', 'top_sort']
    actual_methods = [method for method in dir(sd) 
                      if callable(getattr(sd, method)) 
                      and method in expected_methods]
    
    assert sorted(expected_methods) == sorted(actual_methods)