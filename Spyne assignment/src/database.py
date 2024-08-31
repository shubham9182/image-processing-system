import sqlite3
import uuid
from datetime import datetime

DATABASE = 'image_processing.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            serial_number INTEGER,
            product_name TEXT,
            input_image_urls TEXT,
            output_image_urls TEXT,
            request_id TEXT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            request_id TEXT PRIMARY KEY,
            status TEXT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            completion_time TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_request(request_id, csv_data):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    for row in csv_data:
        c.execute('''
            INSERT INTO products (serial_number, product_name, input_image_urls, request_id, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row['serial_number'], row['product_name'], row['input_image_urls'], request_id, datetime.now(), datetime.now()))
    c.execute('''
        INSERT INTO requests (request_id, status, created_at, updated_at)
        VALUES (?, ?, ?, ?)
    ''', (request_id, "Processing", datetime.now(), datetime.now()))
    conn.commit()
    conn.close()

def update_request(request_id, output_urls):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        UPDATE products
        SET output_image_urls = ?
        WHERE request_id = ?
    ''', (','.join(output_urls), request_id))
    c.execute('''
        UPDATE requests
        SET status = ?, updated_at = ?, completion_time = ?
        WHERE request_id = ?
    ''', ("Completed", datetime.now(), datetime.now(), request_id))
    conn.commit()
    conn.close()

def get_request_status(request_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        SELECT status FROM requests WHERE request_id = ?
    ''', (request_id,))
    status = c.fetchone()
    conn.close()
    return status[0] if status else None
