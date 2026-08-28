import os
import pathlib
import shutil
import subprocess
import sys

import packaging
import pymsbuild


ROOT = pathlib.Path(__file__).absolute().parent.parent


PYTHONPATH = os.pathsep.join(
    str(s)
    for s in [
        ROOT,
        pathlib.Path(packaging.__spec__.origin).parent.parent,
        pathlib.Path(pymsbuild.__spec__.origin).parent.parent,
    ]
)


def run(*cmd, cwd=None, env=None):
    env = {
        **os.environ,
        "PYTHONPATH": PYTHONPATH,
        **(env or {}),
    }
    subprocess.check_call(cmd, cwd=cwd, env=env)


def test_build_package1(testdata, tmp_path):
    root = shutil.copytree(testdata / "package1", tmp_path / "package1")
    run(sys.executable, "-m", "venv", tmp_path, "--system-site-packages", "--without-pip")
    if sys.platform == "win32":
        env_exe = tmp_path / "Scripts" / "python.exe"
    else:
        env_exe = tmp_path / "bin" / "python"
    try:
        run(
            env_exe,
            "-m",
            "pymsbuild",
            "-v",
            "app",
            cwd=root,
            env={"PYMSBUILD_EXTENSION_COMMAND": "app=pymsbuild_app:build"},
        )
        run(env_exe, "verify.py", cwd=root)
    except Exception:
        print(*root.rglob("*"), sep="\n")
        raise
