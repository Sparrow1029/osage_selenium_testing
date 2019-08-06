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
These tests currently only use Firefox with `geckodriver`, so you will need to install that for your system. Instructions can be found here.

Now you should be ready to go!
run the tests with `pytest -v --capture=no BasicTest.py`
