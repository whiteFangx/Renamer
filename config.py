import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5436324303:AAHmj10QbHk5GWGxxsED9j3pIcjZMvjWtOQ")

    APP_ID = int(os.environ.get("APP_ID", 4783634))
    
    API_HASH = os.environ.get("API_HASH", "f6c33f46599246676f75e153b615dbbc")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600
    
    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DB_URI = os.environ.get("DATABASE_URL", "postgres://bglrqvyi:91CJdaAvuvD3dBOS88KVsfZuvsUO4t-a@heffalump.db.elephantsql.com/bglrqvyi")

    UPDATE_GROUP = os.environ.get("UPDATE_GROUP", "makima_bot_support")
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "makima_bot_updates")

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5728181854 6190130299 5481637577 1858995207").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
