## Selenium tests for [osagepartners.com](https://www.osagepartners.com)

### Set-up and requirements
Clone the repo and set up a Python virtual env

```bash
$ git clone git@github.com:Sparrow1029/osage_selenium_testing.git
$ cd osage_selenium_testing
```
I use `virtualenvwrapper`, but you can also use Python's native `virtualenv`
```bash
$ mkvirtualenv osage-tests --python=python3
...
(osage-tests) $ pip install -r requirements.txt
```
These tests currently only use Firefox with `geckodriver`, so you will need to install that for your system:
* Mac OSX:
Easiest is to use a package manager like Homebrew
   `brew install geckodriver`
* Linux (Ubuntu):
   `sudo apt install geckodriver`
* Windows (works with other systems as well):
   1. Navigate to Mozilla/geckodriver [release page](https://github.com/mozilla/geckodriver/releases)
   2. Download the proper release
   3. Unzip and install

Now you should be ready to go!
run the tests with `pytest -v --capture=no BasicTest.py`
