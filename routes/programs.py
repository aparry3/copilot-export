from flask import Blueprint, request

from utils import generate_pdf

programs_api = Blueprint('programs_api', __name__)

@programs_api.route('/api/v1/programs', methods=['POST'])
def post():
    program = request.json
    export_object = generate_pdf(program.get('program_id'))
    return export_object
