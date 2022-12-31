import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "1695333"))
    API_HASH = os.environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1016768333")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://gtm:gtm@cluster0.8hyd72i.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAZ3mUAqtxZPNbgNr3x2WWAuR_s_RRezAmQPCgMvGw4Y9Tp4LUnlp30OGqvWALCN1vc_fxavmRgtfRFMPijmkajJL7Kiwsz2HPwmpLYmPFg1ypXhRCVgAcYfTWAEm48UTUY8741NTD7nQc8oECZt41hA8FwEkPNPe-8FwlrHpYIm6q3gjwNEDlaC4Qfjrwf4doh1582L5Cp_z186cgxynuLBjTHjr-RAD98ATtNpMxXD4bykcPR1sbezOMhnFfHHZAMhjbAFytDDumqupVS3TaxZCHfoaeU3w84gE3KTaQ2Fu4EKsxNlXoa4aMj16zvgTp7P_Ud6DNT58v5lFhkZnfqMLHlxgAAAAA8mqdNAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001525314409"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@TheMediaForwardBot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
