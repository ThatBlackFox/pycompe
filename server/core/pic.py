from PIL import Image
import pytesseract
from typing import List,Any
import os

class PicHandler():
    def __init__(self):
        try:
            self.exec = os.environ['TESS']
        except Exception as e:
            raise ModuleNotFoundError("EnvVarNotFound: Please declare the path to Tessaract in `TESS`")
    def getText(self,img:Any) -> str:
        pytesseract.pytesseract.tesseract_cmd = self.exec
        return pytesseract.image_to_string(Image.open(img.stream))
    def getMultiple(self,paths:List[str])-> List[str]:
        texts = []
        for path in paths:
            texts.append(self.getText(path))