import json

def convert_to_json(data):
    """Convert any data format into a JSON format."""
    try:
        # check if data is string
        if isinstance(data, str):
            return json.loads(data)
        # check if data is xml
        elif data.tag == 'note':
            return {
                'to': data.find('to').text,
                'from': data.find('from').text, 
                'heading': data.find('heading').text,
                'body': data.find('body').text,
            }
    except Exception as e:
        raise e