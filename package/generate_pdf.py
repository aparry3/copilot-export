from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from connection import db
from generators import Program as ProgramGenerator
from models import Program


def generate_pdf(event, context):
    db_program = db.programs.find_one({'_id': '708f6b4b-13d3-4525-915d-bc4931f6c6ab'})
    program = Program(**db_program)

    font_config = FontConfiguration()
    p = ProgramGenerator(program)
    # with open('text.html', 'w') as html_file:
    #     html_file.write(p.render())
    css = CSS('stylesheets.css', font_config=font_config)
    HTML(string=p.render()).write_pdf('test.pdf', stylesheets=[css], font_config=font_config)

if __name__ == '__main__':
    generate_pdf(None, None)
