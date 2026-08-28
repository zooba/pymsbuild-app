# pymsbuild-app

This is a [pymsbuild](https://pypi.org/project/pymsbuild) extension for
building launchable app packages.

## `_msbuild.py` configuration file

Define an application in your `_msbuild.py` file by assigning `APPLICATION` to
an instance of the `Application` type. This metadata will be used along with the
usual `PACKAGE` and `METADATA` variables to create your app.

```python
from pymsbuild import *
from pymsbuild.entrypoint import *
from pymsbuild_app import *

METADATA = {
    ...
}

PACKAGE = Package(
    "my_app",
    PyFile(r"my_app\main.py"),
    Entrypoint(
        "my_app",
        "my_app.main",
        "main",
        Icon(r"my_app\app.ico"),
        VersionInfo(ProductName="My App"),
    ),
)

APPLICATION = Application(
    "my_app",
    AppAlias("my_app"),
    AppDependency("other_package==1.0.0"),
    AppDependency(lockfile="pylock.toml"),
    AppDependency(lockfile="requirements.txt"),
)
```

## Usage

Regular builds ignore the `APPLICATION` data, and produce a launchable
application in the source tree.

Any app dependencies will need to have already been installed. The entrypoint
launches using the runtime environment used to build.

```powershell
$> python -m pymsbuild
$> .\my_app\my_app.exe
```

The `app` command added by this extension produces a full application layout.
Dependencies are downloaded and extracted into the application layout, and the
isolated environment is used by entrypoints.

```powershell
$> python -m pymsbuild app -d <output directory>
```

## Environment variables

* `%PYMSBUILD_APP_RUNTIME_LIBRARY%`: override the path to the Python DLL used by
  the built entrypoints (see [bundled runtime](#bundled-runtime) for more info)
* `%PYMSBUILD_APP_RUNTIME%`: override the install tag or name of the runtime
  package to bundle
* `%PYMSBUILD_APP_RUNTIME_URL%`: override the URL to the runtime package to
  bundle. Requries `%PYMSBUILD_APP_RUNTIME%` also be set to the library name

## Advanced topics

### Bundled runtime

On Windows, the default runtime for a built application is the [embeddable
package](https://docs.python.org/3/using/windows.html#windows-embeddable)
matching the version and architecture of the runtime used to build. It will be
installed using the Python install manager (effectively:
`py install %PYMSBUILD_APP_RUNTIME%`) and the specific paths read from the
package metadata.

On other platforms, the default runtime is assumed to be loadable from
`sysconfig.get_config_var("LDLIBRARY")`. Override `%PYMSBUILD_APP_RUNTIME%`
to use a different library name.

If `%PYMSBUILD_APP_RUNTIME_URL%` is specified on any platform, then it will be
downloaded and extracted as a relocatable bundled runtime. In this case,
`%PYMSBUILD_APP_RUNTIME%` is required to be the name of the library to load
(`LoadLibrary` or `dload`) from the bundled directory.
