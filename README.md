# Playwright-lemoncheesecake-ui-tests
UI tests for AMAZON Wishlist using Lemoncheesecake + Playwright + Python.

## Pre-requisites
* python3

## Setup
Install and create virtualenv (This step should be executed only when setting up the project for the first time)

* Install virtualenv

```bash
$ python3 -m pip install --user virtualenv 
```

* Create virtualenv

```bash
$ python3 -m venv env
```

* Activate the virtual environment:

```bash
$ source env/bin/activate
```

* Install dependencies for setting up tests:

```bash
$ pip install -r requirements.txt
```

* Install Playwright:

```bash
$ PLAYWRIGHT_BROWSERS_PATH=$VIRTUAL_ENV/pw-browsers python -m playwright install
```
 To install MS Edge Browser:

```bash
$ PLAYWRIGHT_BROWSERS_PATH=$VIRTUAL_ENV/pw-browsers python -m playwright install msedge
```

* Set Python Path to the current directory:

```bash
$ export PYTHONPATH="<path to your current directory>"
```

* To Check if PYTHONPATH is set correctly to the current directory:

```bash
$ echo $PYTHONPATH 
```

PYTHONPATH should not be blank and should be your current directory.

## Execute tests:
* Make the changes in the config file for actual values.
Add username and password

Make the appropriate changes to base URL,username and password fields in config.ini file.
By default, the tests will not run in headless mode. If you choose to run otherwise, change the value to "yes".

* To execute the tests:
```bash
$ lcc run
```

* To view the reports on console after you ran the tests:
```bash
$ lcc report
```

* To view the report in browser:
```bash
$ firefox report/report.html
```

* To run a single test:
```bash
$ lcc run <test_file_name>
```
e.g. lcc run test_wishlist

* To debug:
```bash
$ PWDEBUG=1 lcc run
```
or 
```bash
$ PWDEBUG=1 lcc run <test_file_name>
```

By default, the tests will run with Tracing mode as "Yes" . If you choose to run otherwise, change the value to "no".

* To use Tracing functionality:
```bash
$ playwright show-trace trace.zip
```

By default, the tests will run with Screen recording mode as "Yes" . If you choose to run otherwise, change the value to "no".

* To use Test code generator:
```bash
$ playwright codegen <URL TO BE AUTOMATED>
```

Deactivate virtualenv:
```bash
$ deactivate
```
