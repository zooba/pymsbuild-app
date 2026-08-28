# pymsbuild-app

This is a [pymsbuild](https://pypi.org/project/pymsbuild) extension for
building launchable app packages.

The extension adds an `app` command, which builds the `App` target:

```powershell
$> python -m pymsbuild app
```

Import `app.targets` from `pymsbuild_app.TARGETS` in the package definition to
provide the target:

```python
from pymsbuild import LiteralXML
from pymsbuild_app import TARGETS

PACKAGE = Package(
    "package",
    LiteralXML(f'<Import Project="{TARGETS / "app.targets"}" />'),
)
```
