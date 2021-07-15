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
        try:
            self._storage = _connection.root.storage[str(type(botClass))]
        except AttributeError:
            # Initialize storage
            _connection.root.storage = OOBTree()
            _connection.root.storage[str(type(botClass))] = OOBTree()
            transaction.commit()
            self._storage = _connection.root.storage[str(type(botClass))]
        except KeyError:
            _connection.root.storage[str(type(botClass))] = OOBTree()
            transaction.commit()
            self._storage = _connection.root.storage[str(type(botClass))]
    
    def __getitem__(self, key) -> Any:
        return (self._storage[key] if self._storage.has_key(key) else None)

    def __setitem__(self, key, value) -> None:
        self._storage[key] = value
        transaction.commit()
    
    def __delitem__(self, key) -> None:
        del self._storage[key]
        transaction.commit()

# Close on exit
atexit.register(lambda: __db.close())
