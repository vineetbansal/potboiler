from setuptools import setup, find_namespace_packages

setup(
    name='potboiler',
    version='0.1.0',
    description='Nothing useful in particular',
    url='https://github.com/vineetbansal/potboiler',
    author='Vineet Bansal',
    author_email='vineetb@princeton.edu',
    license='MIT',

    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    package_data={'potboiler': ['config.json']},

    zip_safe=True,
    test_suite='tests'
)
