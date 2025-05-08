import json
from typing import Any

class ImportExport:
    def __init__(self, file_path: str):
        if not file_path.endswith('.json'):
            raise ValueError("File must have a .json extension")
        self.file_path = file_path

    def read_json(self) -> str | dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            return f'Error reading JSON: {e}'

    def write_json(self, obj: Any) -> str:
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(obj, f, indent=4)
                return 'JSON file written successfully'
        except OSError as e:
            return f'Error writing JSON: {e}'
