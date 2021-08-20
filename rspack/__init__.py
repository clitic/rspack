import os
import shutil
import tempfile


class PackResource():

    def __init__(self, pyfilepath, chunksize: int=8192, verbose: bool=True):
        self.pyfilepath = pyfilepath
        self.chunksize = chunksize
        self.verbose = verbose

        with open(self.pyfilepath, "w") as python_file:
            python_file.write("from rspack import UnPackResource\n\n")
            python_file.write(r"packed_resources = {}" + "\n\n")

    def add(self, filepath):
        with open(self.pyfilepath, "a") as python_file:
            with open(filepath, "rb") as resource_file:
                python_file.write("bytes_data = [")

                byte_d = resource_file.read(self.chunksize)
                while byte_d != b"":
                    python_file.write(f"\t{byte_d}," + "\n")
                    byte_d = resource_file.read(self.chunksize)

                python_file.write("]\n\n")
                python_file.write(f'packed_resources["{filepath}"] = UnPackResource("{filepath}", bytes_data)\n\n')
    
    def add_dir(self, dirpath):
        for path, _, files in os.walk(dirpath):
            for file in files:
                if self.verbose:
                    print(os.path.join(path, file))

                self.add(os.path.join(path, file))

class UnPackResource():

    def __init__(self, filepath, bytes_data):
        self.filepath = filepath
        self.bytes_data = bytes_data
        self.is_restored = False
        self.is_deleted = False
        self.tempfilepath = ""
        self.is_temp_unpack = False

    def delete(self):
        os.remove(self.tempfilepath) if self.is_temp_unpack else os.remove(self.filepath)
        self.is_deleted = True
    
    def clean(self):
        if not self.is_deleted:
            self.delete()

        if self.is_restored:
            shutil.rmtree(os.path.dirname(self.filepath))

    def _restore(self):
        dir_struct = os.path.dirname(self.filepath)

        if not os.path.exists(dir_struct):
            os.makedirs(dir_struct)
            self.is_restored = True

    def _write_bytes(self, filepath):
        with open(filepath, "wb") as f:
            for byte_d in self.bytes_data:
                f.write(byte_d)

    def unpack(self, filepath=None, restorepath=True) -> str:
        if filepath is None:
            filepath = self.filepath

        if os.path.dirname(filepath) != "" and restorepath:
            self._restore()

        self._write_bytes(filepath)
        return filepath
    
    def temp_unpack(self) -> str:
        _, self.tempfilepath = tempfile.mkstemp()
        self._write_bytes(self.tempfilepath)
        self.is_temp_unpack = True
        return self.tempfilepath
