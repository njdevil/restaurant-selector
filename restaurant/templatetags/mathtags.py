# Restaurant Selector v0.1
# https://github.com/njdevil/restaurant-selector
# ©2013 Modular Programming Systems Inc
# released as GPL 3

from django import template

register=template.Library()

@register.simple_tag
def add(val1, val2):
    return float(val1)+float(val2)

@register.simple_tag
def subtract(val1, val2):
    return val1-val2

@register.simple_tag
def multiply(val1, val2):
    return int(float(val1)*float(val2))

@register.simple_tag
def divide(val1, val2):
    return val1/float(val2)


@register.tag('add_all')
def add_all(parser,token):
    values=token.contents.split()
    return AddNode(*values[1:])

@register.tag('subtract_all')
def subtract_all(parser,token):
    values=token.contents.split()
    return SubtractNode(*values[1:])

@register.tag('multiply_all')
def multiply_all(parser,token):
    values=token.contents.split()
    return MultiplyNode(*values[1:])

@register.tag('divide_all')
def divide_all(parser,token):
    values=token.contents.split()
    return DivideNode(*values[1:])


class AddNode(template.Node):
    def __init__(self, *args):
        self.values=args
    def render(self,context):
        self.x=float(self.values[0])
        for val in self.values[1:]:
            self.x+=float(val)
        return self.x

class SubtractNode(template.Node):
    def __init__(self, *args):
        self.values=args
    def render(self,context):
        self.x=float(self.values[0])
        for val in self.values[1:]:
            self.x-=float(val)
        return self.x

class MultiplyNode(template.Node):
    def __init__(self, *args):
        self.values=args
    def render(self,context):
        self.x=float(self.values[0])
        for val in self.values[1:]:
            self.x*=float(val)
        return self.x

class DivideNode(template.Node):
    def __init__(self, *args):
        self.values=args
    def render(self,context):
        self.x=float(self.values[0])
        for val in self.values[1:]:
            self.x/=float(val)
        return self.x

