# rspacked.py is auto generated file by rspacker.py
from rspacked import packed_resources # packed resources import

# the key here is path provided in rspacker.py
packed_file = packed_resources["some_text.txt"] # select resource through path
packed_file.unpack() # unpack resource

with open("some_text.txt") as f:
    print(f.read())

packed_file.delete() # delete resource if not required any more
