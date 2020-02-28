from setuptools import find_namespace_packages, setup

packages = [package for package in find_namespace_packages(where='./src',
                                                           include='gcs-fake-pii-file-creator.*')]

setup(
    name='gcs-fake-pii-file-creator',
    version='0.0.1',
    author='Marcelo Costa',
    author_email='mesmacosta@gmail.com',
    description='Library for creating CSV files in GCS with fake sensible data',
    platforms='Posix; MacOS X; Windows',
    packages=packages,
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    install_requires=(
        'pandas',
        'faker',
        'google-cloud-storage',
    ),
    setup_requires=(
        'pytest-runner',
    ),
    tests_require=(
        'pytest-cov',
    ),
    classifiers=(
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 3.7',
    ),
)
