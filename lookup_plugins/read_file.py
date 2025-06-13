import sys
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, **kwargs):
        file_path = terms[0]
        content = self.read_file(file_path)
        return [content]

    def read_file(self, file_path):
        with open (file_path, 'r') as file:
            return file.read()

