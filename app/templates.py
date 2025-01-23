"""This Module contains chat templates"""

NOTES_TEMPLATE = """
Provide an answer to the user prompt using the notes mentioned in the Notes JSON. If you can't find an answer in the notes, return frendly error message.

User Prompt:
{prompt}

Notes:
{notes}
"""
