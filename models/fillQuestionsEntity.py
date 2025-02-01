def fillquestionEntity(item):
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    return {
        "id": str(item.get("_id", "")),
        "class_": item.get("class_", ""),
        'subject': item.get("subject", ""),
        'topic': item.get("topic", ""),
        'question': item.get("question", ""),
        "choices": item.get("choices", []),
        'answers': item.get('answers', []),
        'resource': item.get('resource', []),
        'used': bool(used_value) 
         # Added used field
    }

def fillquestionEntitys(items):
    return [fillquestionEntity(item) for item in items]