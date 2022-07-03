from distutils.core import setup

setup(name='steamer',
      version='0.1',
      packages=['steamer'],
      install_requires=[
            'vdf',
      ],
      scripts=['bin/steamer'],
      )
