import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

PACKAGE_TYPE = 'service'
PACKAGE_NAME = 'dbg_app'
PACKAGE_DESC = 'dbg_app'
PACKAGE_LONG_DESC = ''
PACKAGE_VERSION = '0.0.1'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        # default list of options for testing
        # https://docs.pytest.org/en/latest/logging.html
        self.pytest_args = (
            '--flake8 {0} tests '
            '--junitxml=.reports/{0}_junit.xml '
            '--cov={0} --cov=tests '
            '-p no:logging'.format(
                PACKAGE_NAME.replace('-', '_')
            )
        )

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup_requires = []

install_requires = [
    'aiocache==0.11.1',
    'aiohttp==3.7.3',
    'aiohttp-apispec==2.2.1',
    'aioredis==1.3.1',
    'anyascii==0.1.7',
    'apispec==3.3.2',
    'asgiref==3.3.1',
    'async-timeout==3.0.1',
    'attrs==20.3.0',
    'Babel==2.9.0',
    'backcall==0.2.0',
    'beautifulsoup4==4.8.2',
    'certifi==2020.12.5',
    'cffi==1.14.4',
    'chardet==3.0.4',
    'coreapi==2.3.3',
    'coreschema==0.0.4',
    'cryptography==3.3.1',
    'decorator==4.4.2',
    'Deprecated==1.2.10',
    'Django==3.0.11',
    'django-debug-toolbar==3.1.1',
    'django-environ==0.4.5',
    'django-extensions==3.0.9',
    'django-extra-views==0.13.0',
    'django-filter==2.4.0',
    'django-haystack==3.0',
    'django-model-utils==4.1.1',
    'django-modelcluster==5.1',
    'django-oscar==2.1',
    'django-oscar-api==2.1.1',
    'django-oscar-elasticsearch==2.0.3',
    'django-phone-verify==2.0.0',
    'django-phonenumber-field==3.0.1',
    'django-redis==4.12.1',
    'django-tables2==2.2.1',
    'django-taggit==1.3.0',
    'django-tinymce==3.2.0',
    'django-treebeard==4.3.1',
    'django-widget-tweaks==1.4.8',
    'djangorestframework==3.12.2',
    'djangorestframework-simplejwt==4.6.0',
    'draftjs-exporter==2.1.7',
    'drf-yasg==1.20.0',
    'easy-thumbnails==2.7.1',
    'elasticsearch==6.8.1',
    'et-xmlfile==1.0.1',
    'factory-boy==2.12.0',
    'Faker==5.0.0',
    'flake8==3.8.4',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==3.2.1',
    'gunicorn==20.0.4',
    'gdal==2.4.0',
    'hiredis==1.1.0',
    'html5lib==1.1',
    'idna==2.10',
    'inflection==0.5.1',
    'ipdb==0.13.4',
    'ipython==7.19.0',
    'ipython-genutils==0.2.0',
    'isort==5.6.4',
    'itypes==1.2.0',
    'jdcal==1.4.1',
    'jedi==0.17.2',
    'Jinja2==2.11.2',
    'l18n==2020.6.1',
    'MarkupSafe==1.1.1',
    'marshmallow==3.9.1',
    'marshmallow-dataclass==8.3.0',
    'mccabe==0.6.1',
    'multidict==5.1.0',
    'mypy-extensions==0.4.3',
    'nexmo==2.5.2',
    'openpyxl==3.0.5',
    'packaging==20.7',
    'parso==0.7.1',
    'pexpect==4.8.0',
    'phonenumbers==8.12.14',
    'pickleshare==0.7.5',
    'Pillow==8.0.1',
    'prompt-toolkit==3.0.8',
    'psycopg2-binary==2.8.6',
    'ptyprocess==0.6.0',
    'purl==1.5',
    'pycodestyle==2.6.0',
    'pycountry==20.7.3',
    'pycparser==2.20',
    'pyflakes==2.2.0',
    'Pygments==2.7.3',
    'PyJWT==1.7.1',
    'pyotp==2.4.1',
    'pyparsing==2.4.7',
    'pyprof2calltree==1.4.5',
    'pysolr==3.9.0',
    'python-dateutil==2.8.1',
    'python-dotenv==0.15.0',
    'pytz==2020.4',
    'PyYAML==5.3.1',
    'redis==3.5.3',
    'requests==2.24.0',
    'ruamel.yaml==0.16.12',
    'setproctitle==1.2.1',
    'six==1.15.0',
    'sorl-thumbnail==12.7.0',
    'soupsieve==2.0.1',
    'sqlparse==0.4.1',
    'swapper==1.1.2.post1',
    'tablib==3.0.0',
    'text-unidecode==1.3',
    'tqdm==4.54.1',
    'traitlets==5.0.5',
    'twilio==6.50.0',
    'typing-extensions==3.7.4.3',
    'typing-inspect==0.6.0',
    'ujson==4.0.1',
    'Unidecode==1.1.1',
    'uritemplate==3.0.1',
    'urllib3==1.25.11',
    'uvloop==0.14.0',
    'uWSGI==2.0.19.1',
    'uwsgidecorators-fallback==0.0.3',
    'wagtail==2.11.2',
    'wagtail-extendedsearch==1.0.4',
    'wcwidth==0.2.5',
    'webargs==5.5.3',
    'webencodings==0.5.1',
    'Werkzeug==1.0.1',
    'whitenoise==5.2.0',
    'Whoosh==2.7.4',
    'Willow==1.4',
    'wrapt==1.12.1',
    'xlrd==1.2.0',
    'XlsxWriter==1.3.7',
    'xlwt==1.3.0',
    'yarl==1.6.3',
]

extras_require = {
}

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flake8',
    'asynctest==0.7.1'
]

console_scripts = [
]

setup(
    name='{}'.format(PACKAGE_NAME),
    version=PACKAGE_VERSION,
    description=PACKAGE_DESC,
    long_description=PACKAGE_LONG_DESC,
    url='https://github.com/Air-Mark/{}'.format(PACKAGE_NAME),
    author="Mark Trifonov",
    author_email="air.t.mark@gmail.com",
    license="Nodefined",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Framework :: Aioamqp',
        'Framework :: Pytest',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Information Technology',
        'License :: Other/Proprietary License',
        'License :: UIS License',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
        'Topic :: UIS:: Microservices',
    ],
    zip_safe=False,
    packages=find_packages(exclude=['tests', 'examples', '.reports']),
    include_package_data=True,
    entry_points={'console_scripts': console_scripts},
    python_requires='>=3.7',
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    cmdclass={'test': PyTest},

)
