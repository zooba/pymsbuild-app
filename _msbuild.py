import os

from pymsbuild import *


METADATA = {
    "Metadata-Version": "2.2",
    "Name": "pymsbuild-app",
    "Version": "0.0.1",
    "Author": "Steve Dower",
    "Author-email": "steve.dower@python.org",
    "Project-url": [
        "Homepage, https://github.com/zooba/pymsbuild-app",
        "Report bug, https://github.com/zooba/pymsbuild-app/issues",
    ],
    "Summary": "A pymsbuild extension for building launchable app packages.",
    "Description": File("README.md"),
    "Description-Content-Type": "text/markdown",
    "Keywords": "build,pep-517,msbuild,packaging,app,Windows",
    "Classifier": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Compilers",
        "Topic :: Utilities",
    ],
    "Requires-Dist": [
        "pymsbuild>=1.2.2a1",
        "entrypoints",
    ],
    "WheelTag": "py3-none-any",
}


PACKAGE = Package(
    "",
    Package(
        "pymsbuild_app",
        PyFile("pymsbuild_app/*.py"),
        File("pymsbuild_app/targets/*", name="targets/*"),
    ),
    File("entry_points.txt", IncludeInDistinfo=True),
)


def init_METADATA():
    version = os.getenv("BUILD_BUILDNUMBER")
    ghref = os.getenv("GITHUB_REF")
    if ghref:
        version = ghref.rpartition("/")[2]
    if version:
        METADATA["Version"] = version
