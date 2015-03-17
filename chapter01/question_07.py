# coding: utf-8

from string import Template

def template_string(x, y, z):
    template = Template('$x時の$yは$z')
    return template.substitute(x=x, y =y, z=z)

def test_template_string():
    x=12
    y="気温"
    z=22.4
    assert template_string(x, y, z) == '12時の気温は22.4'

if __name__ == '__main__':
    x=12
    y="気温"
    z=22.4
    print(template_string(x, y, z))