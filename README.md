# Q
[![PyPI version](https://badge.fury.io/py/qlang.svg)](https://badge.fury.io/py/qlang)

NOTICE: This is work in progress

A concise, procedural programming language.

# Installation
To install Q from pip, use the command:

```
$ pip install qlang
```

If you want to use Q from a shell script, navigate to the directory where Q is installed and create a symbolic link:

```
ln -s ./cli.py q
```

# Usage
To use Q from a shell script:
```
$ q # run interactive shell
$ q <file> # run file
```

To use Q using the Python API:
```python
from q import run, run_text

run_text('<text>') # run text
run('<file>') # run file
```


# Example program

## Factorial
```java
F={$0>1?$0*F($0-1):1}
```
