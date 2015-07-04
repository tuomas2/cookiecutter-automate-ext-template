from automate import *

def test_{{ cookiecutter.ext_name }}(sysloader):
    class mysys(System):
        p1 = {{ cookiecutter.ext_name|capitalize }}Sensor()
        a1 = {{ cookiecutter.ext_name|capitalize }}Actuator()
    s = sysloader.new_system(mysys, services=[{{ cookiecutter.ext_name|capitalize }}Service()])

    assert not s.p1.status
    # and maybe some other relevant tests
