from flask import Blueprint, abort, send_from_directory
from app_utils import *
import logging
import os

download_bp = Blueprint('download', __name__)
logger = logging.getLogger(__name__)
FILES_DIRECTORY = '/tmp/'

@download_bp.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    # Optional: Validate filename to prevent directory traversal attacks
    file_path = os.path.join(FILES_DIRECTORY, filename)
    if not os.path.isfile(file_path):
        abort(404, description="File not found")
    return send_from_directory(FILES_DIRECTORY, filename, as_attachment=True)
