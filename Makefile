PYTHON=`which python`
NAME=`python setup.py --name`
VERSION=`python setup.py --version`
SDIST=dist/$(NAME)-$(VERSION).tar.gz
VENV=/tmp/venv

all: check source

dist: source 

source:
	$(PYTHON) setup.py sdist

install:
	$(PYTHON) setup.py install

check:
	find . -name \*.py | grep -v "^test_" | xargs pylint --errors-only --reports=n
	# pep8
	# pyntch
	# pyflakes
	# pychecker
	# pymetrics

clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST dist build *.egg-info deb_dist
	find . -name '*.pyc' -delete

