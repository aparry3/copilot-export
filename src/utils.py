import os

import boto3
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from connection import db
from generators import Program as ProgramGenerator
from models import Program

BASE_PATH = os.path.dirname(__file__)
s3 = boto3.resource('s3')

S3_BASE_URL = 'https://{bucket}.s3.amazonaws.com/{key}'

def generate_pdf(program_id):
    bucket = s3.Bucket('copilot-fitness')
    print(bucket.name)
    db_program = db.programs.find_one({'_id': program_id})

    program = Program(**db_program)

    p = ProgramGenerator(program)

    font_config = FontConfiguration()
    css = CSS(os.path.join(BASE_PATH, 'stylesheets.css'), font_config=font_config)
    pdf = HTML(string=p.render()).write_pdf(stylesheets=[css], font_config=font_config)

    obj = bucket.put_object(Body=pdf, Key=f'exports/{program_id}.pdf', ACL='public-read')

    print(obj)
    return {
        'url': 's3 url'
    }
