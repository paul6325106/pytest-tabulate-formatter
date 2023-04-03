from setuptools import setup


def get_readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='paul6325106.pytest-tabulate-formatter',
    version='1.0.dev0',
    description='Example pytest formatter which produces reports using Tabulate',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    packages=[
        'paul6325106.pytesttabulateformatter'
    ],
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        'pytest',
        'tabulate'
    ],
    extras_require={
        'lint': [
            'mypy',
            'pycodestyle'
        ]
    },
    entry_points={
        'pytest11': [
            'pytest-tabulate-formatter = paul6325106.pytesttabulateformatter.plugin',
        ]
    },
    zip_safe=False
)
