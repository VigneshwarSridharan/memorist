from app.database import get_cursor
import json


def get_all_notes():
    cursor = get_cursor()
    cursor.execute("SELECT id,content,metadata FROM notes")
    rows = cursor.fetchall()

    return [{
        "id": id,
        "content": content,
        "metadata": json.loads(metadata)
    } for id, content, metadata in rows]
