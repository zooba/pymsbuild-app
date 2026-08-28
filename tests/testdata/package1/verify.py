import pathlib


ROOT = pathlib.Path(__file__).absolute().parent

assert (ROOT / "package1/package1.py").exists()
