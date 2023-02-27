import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "1695333"))
    API_HASH = os.environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5527448498:AAH-8panVukNPyY7AhBMhPBj-yjRSpqilzI') 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1016768333")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAZ3mUARGPfzi_Jovf6ryUN-hxQFS4kSDiDMWiAk2arhfBiANxF0paZIdG_hVl1FSuylVVAoIqSFboawt3YoSuG4AMLBq76tIYqed6yT0nZVX0o3GtKRxu-9QsDapLUC8eN8bTfn6wLwOcTrvrjJoXeomzvMQqrhaTNNDTLN25f77LHP-X5tlhvTqCPh0aLsdTxjHm49zd45yzfzmU6Z-tpobDKwDnJHVQ9Zoy7-mfuDiXkzsUfDLBblyvmRkopN5_oIx8uuBuIV_wNlr4pxcWC5Cb05E6WZsG5CPGKYq1mdoRYG-m-EXeN5CmkPgnZvweDQ6FaZFD-Cf-8oz1kK0UcluJSLAAAAAA8mqdNAA)
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001665685493"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@TheMediaForwardBot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
