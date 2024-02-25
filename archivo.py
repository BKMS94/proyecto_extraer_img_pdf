
class Archivo:
        def __init__(self,pdf_path = None):
                self.pdf_path = pdf_path.replace('/','\\\\')

        def __str__(self) -> str:
                return f'''pdf_path: {self.pdf_path}'''
