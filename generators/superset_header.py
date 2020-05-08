from . import ContentGenerator

from .details import Details

SCHEMES = {
    'AMRAP': [
        {'title': 'Time', 'detail': 'duration'}
    ],
    'RFT': [
        {'title': 'Rounds', 'detail': 'sets'}
    ],
    'LADDER': [
        {'title': 'Step', 'detail': 'step'},
        {'title': 'Start', 'detail': 'start'},
        {'title': 'End', 'detail': 'end'}
    ],
    'EMOM': [
        {'title': 'Time', 'detail': 'duration'}
    ],
}

def get_details(scheme=None, details=None):
    if scheme is None:
        return []
    return [(o['title'], details.get(o['detail'])) for s in scheme for o in SCHEMES[s] if details.get(o['detail']) is not None]


class SupersetHeader(ContentGenerator):
    _template = 'superset_header.html'

    def __init__(self, scheme, details):
        super(SupersetHeader, self).__init__()
        self.template_vars = {
            'title': ', '.join(scheme) if scheme is not None and len(scheme) > 0 else 'SUPERSET',
            'details': Details(get_details(scheme, details))
        }
