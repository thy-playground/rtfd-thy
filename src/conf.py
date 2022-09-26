# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conf_global import *

project = "Thy's Notes"
project_copyright = '2022, Thierry Humphrey'
author = 'Thierry Humphrey'

intersphinx_mapping_enabled = (
    'py3',
    'pydevguide',
    'rtfd',
    'sphinx',
)
intersphinx_mapping = {k: v for k, v in intersphinx_mapping.items() if k in intersphinx_mapping_enabled}

