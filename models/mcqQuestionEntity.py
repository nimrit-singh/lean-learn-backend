def mcqEntity(item):
    # Convert used field to boolean
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    
    return {
        "id": str(item.get("_id", "")),
        "class_": item.get("class_", ""),
        'subject': item.get("subject", ""),
        'topic': item.get("topic", ""),
        'question': item.get("question", ""),
        'options': item.get('options', []),
        'answers': item.get('answers', []),
        'resource': item.get('resource', []),
        'captions': item.get('captions', []),
        'used': bool(used_value)# Convert to boolean
    }

def mcqEntitys(items):
    return [mcqEntity(item) for item in items]