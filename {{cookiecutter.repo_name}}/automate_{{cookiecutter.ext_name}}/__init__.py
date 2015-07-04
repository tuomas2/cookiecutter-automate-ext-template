__author__ = '{{ cookiecutter.author_full_name }}'
__email__ = '{{ cookiecutter.author_email }}'
__version__ = '{{ cookiecutter.version }}'

from .{{ cookiecutter.ext_name }}_service import {{ cookiecutter.ext_name|capitalize }}Service
from .{{ cookiecutter.ext_name }}_actuators import {{ cookiecutter.ext_name|capitalize }}Actuator
from .{{ cookiecutter.ext_name }}_sensors import {{ cookiecutter.ext_name|capitalize }}Sensor
from .{{ cookiecutter.ext_name }}_callables import {{ cookiecutter.ext_name|capitalize }}Callable

extension_classes = [{{ cookiecutter.ext_name|capitalize }}Service,
                     {{ cookiecutter.ext_name|capitalize }}Actuator,
                     {{ cookiecutter.ext_name|capitalize }}Sensor,
                     {{ cookiecutter.ext_name|capitalize }}Callable,
                     ]
