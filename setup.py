from distutils.core import setup

setup(
    name='hitb_client',
    version='0.1',
    description='Python library to develop exploits with the HITBCTF  API',
    packages=['hitb_client'],
    install_requires=[
        'requests',
        'requests-cache',
        'redis'
    ],
)
