"""
Strip text between BEGIN and END
"""


import re
import sys


BEGIN = '$\s+# BEGIN$'
END = '$\s+# END$'

in_text = sys.stdin.read()


sys.stdout.write(re.sub(r'({}).*?({})'.format(BEGIN, END), r'\1\2', in_text, flags=re.MULTILINE | re.DOTALL))
