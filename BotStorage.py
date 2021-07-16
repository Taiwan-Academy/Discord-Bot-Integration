from typing import Any
from ZODB import DB
from ZODB.FileStorage import FileStorage
from pathlib import Path
from BTrees.OOBTree import OOBTree
import atexit
import transaction
from Singleton import Singleton

# Connection
__db_dir = Path("storage")
__db_dir.mkdir(exist_ok=True)
__db = DB(FileStorage(str(__db_dir.joinpath("storage"))))
_connection = __db.open()

class BotStorage(metaclass=Singleton):
    def __init__(self, botClass) -> None:
        self._storageKey = str(type(botClass))
        try:
            _connection.root.storage[self._storageKey]
        except AttributeError:
            # Initialize storage
            _connection.root.storage = OOBTree()
            _connection.root.storage[self._storageKey] = OOBTree()
            transaction.commit()
        except KeyError:
            _connection.root.storage[self._storageKey] = OOBTree()
            transaction.commit()
    
    def __getitem__(self, key) -> Any:
        return (_connection.root.storage[self._storageKey][key] if _connection.root.storage[self._storageKey].has_key(key) else None)

    def __setitem__(self, key, value) -> None:
        _connection.root.storage[self._storageKey][key] = value
        transaction.commit()
    
    def __delitem__(self, key) -> None:
        del _connection.root.storage[self._storageKey][key]
        transaction.commit()

# Close on exit
atexit.register(lambda: __db.close())
