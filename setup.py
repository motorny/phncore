from setuptools import setup, find_packages

packages = find_packages()


def parse_reqs():
    reqs_file = open('requirements.txt')
    return [str(req_line) for req_line in reqs_file]


setup(
    name='phncore',
    version='0.0.1',
    packages=packages,
    url='https://github.com/motorny/phncore',
    license='MIT',
    author='Motornyi Nikita',
    author_email='motorny.nikita@gmail.com',
    description='PHNode (Personal House Node) core package',
    install_requires=parse_reqs(),
    scripts=['phncore/bin/phncore.py',
             'phncore/core.py',
             ],
)
