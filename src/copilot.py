from flask import Flask, request

from utils import generate_pdf

app = Flask(__name__)

@app.route('/api/v1/programs', methods=['POST'])
def post():
    program = request.json

    export_object = generate_pdf(program.get('program_id'))
    return export_object
