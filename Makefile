BOOTSTRAP_URL=http://downloads.buildout.org/2/bootstrap.py

.PHONY: default project clean very-clean

default: bin/buildout
	python bin/buildout

bin/buildout: bootstrap.py
	mkdir -p var/
	python bootstrap.py -v 2.1.1

bootstrap.py:
	wget $(BOOTSTRAP_URL)

# Destroys existing test database and creates a new one
db:
	rm -f var/db/*.db
	python bin/django syncdb --noinput
	python bin/django migrate
	python bin/django loaddata project/fixtures/*_dev_data.yaml

clean:
	find ./ -name *.pyc -delete

very-clean: clean
	@# This may vary depending where buildout sticks stuff.
	rm -f bootstrap.py
	rm -rf bin/
	rm -rf var/
