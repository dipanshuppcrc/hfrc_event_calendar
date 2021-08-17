from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hfrc_event_calendar/__init__.py
from hfrc_event_calendar import __version__ as version

setup(
	name="hfrc_event_calendar",
	version=version,
	description="HFRC Event Calendar",
	author="ppcrc",
	author_email="nikhil.bk@jaansi.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
