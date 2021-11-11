from distutils.core import setup

setup(
    name='hitbctf_client',
    version='0.1',
    description='Python library to develop exploits with the HITBCTF status API',
    packages=['hitbctf_client'],
    install_requires=[
        'requests',
        'requests-cache',
        'redis'
    ],
)
