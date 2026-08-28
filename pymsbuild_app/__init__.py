from pathlib import Path


TARGETS = Path(__file__).absolute().parent / "targets"


def build(buildstate):
    "Build a launchable app package."
    buildstate.target = "App"
    return buildstate.build()


__all__ = ["TARGETS", "build"]
