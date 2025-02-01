def formula_question_entity(item):
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    return {
        "id": str(item.get("_id", "")),
        "class_": item.get("class_", ""),
        'subject': item.get("subject", ""),
        'topic': item.get("topic", ""),
        'question': item.get("question", ""),
        "quantities": [
            {"name": q.get("name", ""), "symbol": q.get("symbol", ""), "isUnknown": bool(q.get("isUnknown", False))}
            for q in item.get("quantities", [])
        ],
        "formula": item.get("formula", []),
        "options": item.get("options", []),
        'answers': item.get('answers', []),
        'resource': item.get('resource', []),
        'used': bool(item.get('used', False)) 
    }

def formula_question_entitys(items):
    return [formula_question_entity(item) for item in items]