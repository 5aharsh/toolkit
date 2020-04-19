from setuptools import setup

setup(
    name='toolkit',
    version='0.1',
    py_modules=['modules.hash', 'modules.tasks', 'modules.wget', 'modules.server'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        toolkit=main:toolkit
    ''',
)