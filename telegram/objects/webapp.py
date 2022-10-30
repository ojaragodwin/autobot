from .base import BaseObject

class WebAppData(BaseObject):
    def __init__(self,
        data,
        button_text,
    ):

        self.data = data
        self.button_text = button_text


class WebAppInfo(BaseObject):
    def __init__(self,
        url,
    ):
        self.url = url 
