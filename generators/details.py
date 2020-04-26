from . import ContentGenerator


class Details(ContentGenerator):
    _template = 'details.html'

    def __init__(self, details):
        super(Details, self).__init__()
        self.template_vars = {
            'details': details
        }
