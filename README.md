# RSPack

<p align="center">
  <a href="https://www.python.org/downloads/" title="Python Version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a href="https://github.com/clitic/rspack"><img src="https://img.shields.io/github/repo-size/clitic/rspack.svg" alt="Repository Size"></a>
</p>

pack resource files to a python script

## Installations

```bash
pip install https://github.com/clitic/rspack/archive/master.zip
```

## Usage

1. Create a file named **rspacker.py** in root directoray of program.

```python
from rspack import PackResource

packed_container = PackResource("rspacked.py") # packed file
# add resources by relative path only
packed_container.add("README.md") # add files
packed_container.add_dir("images") # add dir
```

```bash
$ python rspacker.py
```

2. To unpack all resources, prepend below snippet to any script.

```python
from rspacked import packed_resources

for packed_file in packed_resources.values():
    packed_file.unpack()
```

More detailed [example](examples/file_operation/README.md).

## Some More Snippets

1. To unpack all resources in root directoray of program, prepend below snippet to any script.

```python
import os
from rspacked import packed_resources

script_dir = os.path.dirname(os.path.abspath(__file__))

for path, packed_file in packed_resources.items():
    packed_file.unpack(os.path.join(script_dir, path), restorepath=False)
```

2. To delete unpacked resources, postpend below snippet to any script.

```python
for packed_file in packed_resources.values():
    packed_file.delete()
```

## Quick Links

- [CHANGELOG.md](CHANGELOG.md)

## License

© 2021 clitic

This repository is licensed under the MIT license. See LICENSE for details.
