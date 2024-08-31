# API Documentation

## Upload API

### Endpoint

`POST /api/upload`

### Description

Accepts a CSV file and returns a unique request ID.

### Request

- File: CSV file containing product data and image URLs.

### Response

```json
{
  "request_id": "your-request-id"
}
```
