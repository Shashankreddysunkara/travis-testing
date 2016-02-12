import sys

from setuptools import setup
from setuptools.extension import Extension


if sys.platform.startswith("darwin"):
    # Do something different for mac
    pass


setup(
    name="travis_testing",
    version="0.0.1",
    url='http://github.com/CTPUG/pygame_cffi',
    license='MIT',
    description="A package for testing travis configurations.",
    long_description=open('README.rst', 'r').read(),
    packages=['thing'],
    include_package_data=True,
    scripts=[
    ],
    setup_requires=[
        'cffi>=1.0.3',
    ],
    ext_modules=[Extension('thing/test_lib/libtest', ['thing/test_lib/test.c'])],
    #cffi_modules=["thing/test_ffi.py:ffi"],
    install_requires=[
        'cffi>=1.0.3',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
