from setuptools import setup, find_packages

setup(
    name='animals',
    version='1.2.0',
    description='Animal database',
    url='https://github.com/uchicago-python/animals',
    author='The Animal development team',
    author_email='animal-dev@googlegroups.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    #install_requires=['plants'],
    package_data={
        'animals': ['animal_data.csv'],
    },
)
