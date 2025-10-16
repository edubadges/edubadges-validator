import os
from setuptools import find_packages, setup


# Build README info
short_description = 'A python module that performs verification for Open Badges.'
try:
    import pypandoc
    pypandoc.convert_file('README.md', 'rst', outputfile='README.rst')
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()
except (ImportError, RuntimeError, OSError):
    README = short_description

# import VERSION
try:
    execfile(os.path.join(os.path.dirname(__file__), 'openbadges/version.py'))
except NameError:
    exec(open(os.path.join(os.path.dirname(__file__), 'openbadges/version.py')).read())

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='openbadges',
    version=".".join(map(str, VERSION)),
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    license='Apache 2',
    description=short_description,
    long_description=README,
    url='https://github.com/IMSGlobal/openbadges-validator-core',
    author='IMS Global',
    author_email='openbadgesinfo@imsglobal.org',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Education',
        'Topic :: Utilities',
        'Intended Audience :: Developers'
    ],
    install_requires=[
        'aniso8601>=9.0.1',
        'Click == 6.7',
        'future>=0.18.3',
        'jsonschema==4.18.3',
        'language-tags==1.2.0',
        'openbadges-bakery==2.0.0',
        'pycryptodome==3.18.0',
        'pydux==0.2.2',
        'PyLD==1.0.5',
        'python-jose==3.3.1',
        'python-mimeparse==1.6.0',
        'pytz==2023.3',
        'requests >= 2.13',
        'requests_cache==1.1.0',
        'rfc3986==2.0.0',
        'validators==0.20.0',
    ],
    extras_require={
        'server':  ["Flask==0.12.1", 'gunicorn==19.7.1'],
    },
    entry_points="""
        [console_scripts]
        openbadges=openbadges.command_line:cli
    """
)
