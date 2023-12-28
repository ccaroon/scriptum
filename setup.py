from setuptools import setup
import scriptum.version

setup(
    name='scriptum',
    version=scriptum.version.VERSION,
    packages=['scriptum'],
    package_dir={'scriptum': 'scriptum'},
    install_requires=[
        'adventurelib >= 1.2.1',
        'colorama >= 0.4.6',
        'pyfiglet >= 1.0.2',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'scriptum=scriptum.main:cli',
    #     ],
    # },
)
