from pymsbuild import *
from pymsbuild_app import TARGETS


METADATA = {
    "Name": "package1",
    "Version": "1.0",
}


PACKAGE = Package(
    "package1",
    PyFile("package1.py"),
    LiteralXML(f'<Import Project="{TARGETS / "app.targets"}" />'),
)
