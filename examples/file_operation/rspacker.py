from rspack import PackResource

packed_container = PackResource("rspacked.py") # this file will store packed resources
packed_container.add("some_text.txt") # use relative paths only
