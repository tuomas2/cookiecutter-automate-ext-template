from traits.api import CInt
from automate.actuators import FloatActuator


class {{ cookiecutter.ext_name|capitalize }}Actuator(FloatActuator):
    _status = CFloat(0.0)

    def setup(self):
        pass

    def cleanup(self):
        pass

    def _status_changed(self):
        pass
