# we would like to define steps that are used in multiple scenarios
# the following does not work, because pytest_bdd.given seems to be file-aware:
#
# from .steps import *
#
# instead, we use pytest_plugins to make this work
pytest_plugins = ["nerdd_module.tests", "tests.steps"]
