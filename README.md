# Using pip package manager

## Commands
```bash
    Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev
   
   Install a particular dependency
   $ pipenv install [DEPENDENCY_NAME]

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.

```

## Pipfile
- this is a replacement to 'requirements.txt'
- pipfile stores all your dependencies and run scripts
```Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[scripts] // running 'pipenv run [SCRIPT] will run the script'
start="python3 app.py"
test="python3 ./test/tests.py"
linus="echo omruti gave away his real PC for a chromebook"

[packages] // running  'pipenv install' will install the packages listed below
flask = "*"
flask-cors = "*"
dnspython="*"

[dev-packages]

[requires]
python_version = "3.6"
```

## Setup pip environment

```bash
# initialize project
$ pipenv --python [PYTHON_VERSION]

# install any dependencies needed for project
$ pipenv install [DEPENDENCY]

# setup run script replace [MAIN_FILE] w/ your main python file
$ echo "" >> Pipfile
$ echo "[scripts]" >> Pipfile
$ echo '"start="python3 [MAIN_FILE]'>> Pipfile

# start your program
$ pipenv run start
```

## NPM reference 
|                    | npm (NodeJS)                    | pipenv (Python)                  |
|--------------------|---------------------------------|----------------------------------|
| Dependency file    | package.json                    | Pipfile                          |
| Lock file          | package.lock.json               | Pipfile.lock                     |
| Initalize Project  | npm init                        | pipenv --python [PYTHON_VERSION] |
| Install Dependency | npm install [DEPENDENCY] --save | pipenv install [DEPENDENCY]      |
| Install            | npm install                     | pipenv install                   |
| Run                | npm run [SCRIPT]                | pipenv run [SCRIPT]              |