from ZODB import DB
from ZODB.FileStorage import FileStorage
from pathlib import Path
from BTrees.OOBTree import OOBTree
from persistent.list import PersistentList
import json

# Connection
db_dir = Path("storage")
db_dir.mkdir(exist_ok=True)
db = DB(FileStorage(str(db_dir.joinpath("storage"))))
connection = db.open()

dump_obj = {}

for botKey in connection.root.storage.keys():
    dump_obj[botKey] = {}
    for key, value in connection.root.storage[botKey].items():
        if isinstance(value, OOBTree):
            dump_obj[botKey][key] = {}
            for treeKey, val in value.items():
                dump_obj[botKey][key][treeKey] = val
        elif isinstance(value, PersistentList):
            dump_obj[botKey][key] = [val for val in value]
        else:
            dump_obj[botKey][key] = value


with open("dump.json", "w") as fout:
    json.dump(dump_obj, fout, indent=4)