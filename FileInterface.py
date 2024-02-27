# Generic class interface for any file.
# Sam Pert
# 27/02/2024

class FileInterface:
    # (Sam) These two methods are to be overridden by any parent class.
    def read(self, fileName):
        pass
    def write(self, fileName):
        pass
