import runpy
import io
from contextlib import redirect_stdout

def test_major_output():
    f = io.StringIO()
    with redirect_stdout(f):
        runpy.run_path('major.py')
    assert f.getvalue().strip() == '3'