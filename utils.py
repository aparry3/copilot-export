from datetime import datetime
import os

import boto3
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from config import app
from connection import db
from generators import Program as ProgramGenerator
from models import Program

BASE_PATH = os.path.dirname(__file__)
s3 = boto3.resource('s3',
    aws_access_key_id=app.config.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=app.config.get('AWS_SECRET_ACCESS_KEY')
)


def generate_pdf(program_id):
    bucket = s3.Bucket('copilot-fitness')

    db_program = db.programs.find_one({'_id': program_id})
    program = Program(**db_program)

    p = ProgramGenerator(program)

    font_config = FontConfiguration()
    css = CSS(os.path.join(BASE_PATH, 'stylesheets.css'), font_config=font_config)
    pdf = HTML(string=p.render()).write_pdf(stylesheets=[css], font_config=font_config)

    obj = bucket.put_object(Body=pdf, Key=f'exports/{program_id}.pdf', ACL='public-read')

    export_doc = {
        'url': app.config.get('S3_BASE_URL').format(bucket=obj.bucket_name, key= obj.key),
        'uploaded': datetime.now()
    }

    db_program = db.programs.find_one_and_update(
        {'_id': program_id},
        {'$set': {'export': export_doc}},
        {'new': True}
    )

    return export_doc
