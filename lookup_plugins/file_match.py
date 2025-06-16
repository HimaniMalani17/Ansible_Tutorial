"""
    This lookup returns a list of files.
"""

import os
import re
from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):
    def run(self, terms, **kwargs):
        directory = terms[0]
        max_end = int(terms[1])

        if not os.path.isdir(directory):
            raise AnsibleError(f"Directory not found: {directory}")
        
        try:
            matched_files = []
            for fname in os.listdir(directory):
                match = re.search(r'\.(\d+)_(\d+)$', fname)
                # print(match)
                if match:
                    end = int(match.group(2))
                    if end < max_end:
                        matched_files.append(fname)
            return matched_files

        except Exception as e:
            raise AnsibleError(f"Error reading directory: {e}")
