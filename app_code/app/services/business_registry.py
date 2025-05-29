import os

class BusinessRegistry:
    def validate_documents(self, file_paths: list[str]) -> bool:
        return all(path.lower().endswith('.pdf') and os.path.isfile(path) for path in file_paths)
