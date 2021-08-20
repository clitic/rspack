# File Operation Example

Suppose you have a text file as resource called it **some_text.txt** which is required by your program. Here the program is in **main.py** file with the following  contents.

```python
with open("some_text.txt") as f:
    print(f.read())
```

To pack any resource file, first create a packer file which can pack different resource files to python file. Here it is named **rspacker.py**.

```python
from rspack import PackResource

packed_container = PackResource("rspacked.py") # this file will store packed resources
packed_container.add("some_text.txt") # use relative paths only
```

After creating rspacker.py run it once.

```bash
$ python rspacker.py
```

To work with the packed resource, write some more code in **main.py**.

```python
# rspacked.py is auto generated file by rspacker.py
from rspacked import packed_resources # packed resources import

# the key here is path provided in rspacker.py
packed_file = packed_resources["some_text.txt"] # select resource through path
packed_file.unpack() # unpack resource

with open("some_text.txt") as f:
    print(f.read())

packed_file.delete() # delete resource if not required any more
```

Now copy **main.py** and **rspacked.py** to any path and run it. **some_text.txt** is no longer required to be present in program directoray. It would be unpacked in current working directory.

```bash
$ python main.py
```