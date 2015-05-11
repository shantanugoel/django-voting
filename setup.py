from setuptools import setup, find_packages

# Dynamically calculate the version based on tagging.VERSION.
version_tuple = __import__('voting').VERSION
if version_tuple[2] is not None:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name='django-voting',
    version=version,
    description='Generic voting application for Django',
    author='Jonathan Buchanan',
    author_email='jonathan.buchanan@gmail.com',
    maintainer='Jannis Leidel',
    maintainer_email='jannis@leidel.info',
    url='http://github.com/jezdez/django-voting/',
    packages=[
        'voting',
        'voting.migrations',
        'voting.templatetags',
        'voting.tests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
