from flask import Blueprint, request, jsonify
from utils import validate_csv, generate_request_id
from database import save_request, get_request_status
from worker import process_images_async

upload_api = Blueprint('upload_api', __name__)
status_api = Blueprint('status_api', __name__)

@upload_api.route('/api/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    csv_data = validate_csv(file)
    if not csv_data:
        return jsonify({"error": "Invalid CSV format"}), 400

    request_id = generate_request_id()
    save_request(request_id, csv_data)
    process_images_async(request_id, csv_data)

    return jsonify({"request_id": request_id}), 202

@status_api.route('/api/status', methods=['GET'])
def check_status():
    request_id = request.args.get('request_id')
    status = get_request_status(request_id)
    if not status:
        return jsonify({"error": "Request ID not found"}), 404
    return jsonify({"status": status}), 200
