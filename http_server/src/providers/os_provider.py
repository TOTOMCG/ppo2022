import os
import platform
import ctypes


class OSProvider:

    def get_home(self):
        if platform.system() == "Windows":
            return os.environ.get("HOMEPATH")
        else:
            return os.environ.get("HOME")

    def isdir(self, path):
        return os.path.isdir(path)

    def mkdir_private_dir(self, *path):
        p = os.path.join(*path)
        if not self.isdir(p):
            os.makedirs(p)
            if platform.system() == "Windows":
                FILE_ATTRIBUTE_HIDDEN = 0x02
                ctypes.windll.kernel32.SetFileAttributesW(p, FILE_ATTRIBUTE_HIDDEN)