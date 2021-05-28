import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
		name = 'roobet',
		version = '0.0.1',		
		author = 'Drew Nicolette',
		author_email = 'nicolettedrew0@gmail.com',
		description = 'Python library for querying Roobet Crash games',
		long_description = 'Python library for querying Roobet Crash games',
        long_description_content_type='text/mardown',
		url="https://github.com/r3ap3rpy/udemy",
		license = 'MIT',
		packages = ['roobet'],
		zip_safe = False,
		include_package_data=True,
		install_requires=['hashlib','hmac'],
      	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	)