import csv
import uuid

def validate_csv(file):
    try:
        csv_data = []
        reader = csv.DictReader(file.stream)
        for row in reader:
            csv_data.append({
                'serial_number': row['S. No.'],
                'product_name': row['Product Name'],
                'input_image_urls': row['Input Image Urls']
            })
        return csv_data
    except Exception as e:
        print(f"Error validating CSV: {e}")
        return None

def generate_request_id():
    return str(uuid.uuid4())
