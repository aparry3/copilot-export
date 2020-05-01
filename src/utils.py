from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from connection import db
from generators import Program as ProgramGenerator
from models import Program


def generate_pdf(program_id):
    db_program = db.programs.find_one({'_id': program_id})
    program = Program(**db_program)

    font_config = FontConfiguration()
    p = ProgramGenerator(program)

    css = CSS('stylesheets.css', font_config=font_config)
    HTML(string=p.render()).write_pdf(stylesheets=[css], font_config=font_config)
