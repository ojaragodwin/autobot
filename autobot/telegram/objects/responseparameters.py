from .base import BaseObject

class ResponseParameters(BaseObject):
    """
    Contains information about why a request was unsuccessful.

    Args:
        migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. 
        This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. 
        But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        
        retry_after (int): Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """

    __slots__ = (
        'migrate_to_chat_id', 
        'retry_after'
        )
    
    
    def __init__(self):
        self.migrate_to_chat_id = None
        self.retry_after = None