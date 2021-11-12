# hitbctf-client
This library allows accessing the status endpoint as described in the HITB+ CyberWeek PRO CTF 2021 Rules

For usage information check out the `hitb_client/client.py`, the code should not be too hard to understand.

## Request caching
You can optionally cache requests using a redis backend. This makes sense if you have limited bandwidth and start a large amount of processes in parallel or frequently call the functions, since each function equates an HTTP request to the endpoint.

To enable redis caching setup a redis listening on `localhost:6379` and set the environment variable `export HITB_CLIENT_CACHE=1`. You can adjust the default TTL of 5 seconds by setting e.g. `HITB_CLIENT_CACHE_EXPIRY=15`.

## Usage example
The library is not available on pypi.org, instead it can be installed using
```
pip3 install git+https://github.com/ENOFLAG/HITB-client.git
```

An example program might look as follows:
ToDo