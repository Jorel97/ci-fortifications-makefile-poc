.PHONY: fortifications

PYTHON ?= python3

fortifications:
	$(PYTHON) tools/fortifications.py src tools

