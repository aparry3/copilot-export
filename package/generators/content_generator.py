import os
from  jinja2 import Environment, FileSystemLoader, select_autoescape

class ContentGenerator:

    template_base = os.path.join(os.path.dirname(__file__), '..', 'templates')
    _template = 'base.html'

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader(self.template_base)
        )
        self.template = self.env.get_template(self._template)

    def template(self):
        return os.path.join(self.template_base, self._template)

    def render(self):
        return self.template.render(self.template_vars)
