Write all your code in the `solutions/` directory. Use `make exercises` to
generate the problems.

To mimic existing packages that need to be mocked, adding a fake package to the
`shims/` directory will make it importable so you can do `import requests`
within your exercises.


Using Python 3
--------------

With Virtualenvrapper:

    mkvirtualenv --py=python3.4 you-mock-me

Here's what my personal Python environment looks like:

    $ python --version
    Python 3.4.0
    $ which python
    /home/crc/env/you-mock-me/bin/python
