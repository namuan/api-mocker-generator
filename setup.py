import sys
import os
import re
from setuptools import setup, find_packages

# 'setup.py publish' shortcut
if sys.argv[-1] == 'publish':
    os.system('rm -r dist/*')
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

# read the version number from source
version = re.search("^__version__\s*=\s*'(.*)'",
                    open('src/api_mocker_generator.py').read(), re.M).group(1)

# Get the long description from the relevant file
try:
    # in addition to pip install pypandoc, might have to: apt install -y pandoc
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError) as e:
    print("Error converting READMD.md to rst:", str(e))
    long_description = open('README.md').read()

setup(name='api-mocker-generator',
      version=version,
      description='Generates config and test data for API Mocker node module using Swagger/OpenAPI Spec.',
      long_description=long_description,
      keywords=['swagger', 'apis', 'testing', 'mock', 'server'],
      author='Nauman Leghari',
      author_email='nauman@docker-files.com',
      url='https://github.com/namuan/api-mocker-generator',
      install_requires=[],
      packages=find_packages(exclude=['pypandoc']),
      entry_points={
          "console_scripts": [
              'api-mocker-generator=src.api_mocker_generator:main'
          ]
      },
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ]
      )
