from traits.api import CInt
from automate.statusobject import AbstractSensor


class {{ cookiecutter.ext_name|capitalize }}Sensor(AbstractSensor):
    _status = CInt(0)

    def setup(self):
        pass

    def cleanup(self):
        pass
