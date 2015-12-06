import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'RPi',
    ]

setup(name='pypinsobj',
      version='0.1',
      description='wrapper for RPi',
      classifiers=[
        "Programming Language :: Python",
        ],
      author='bchoward',
      author_email='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      """,
      )

