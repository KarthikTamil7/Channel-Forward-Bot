import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
    APP_ID = int(os.environ.get("APP_ID", "11973721"))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1391556668 5162208212 5239847373").split())
    CHANNEL1_ID = os.environ.get("CHANNEL1_ID", "-1001342411240:-1001518309911")
    CHANNEL1_NAME = os.environ.get("CHANNEL1_NAME", "URL Uploader's Log")
    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")
    CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")
    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")
    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")
    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")
    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")
    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")
    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
    CHANNEL_ID = os.environ.get("CHANNEL_ID")
    CHANNEL_NAME = os.environ.get("CHANNEL_NAME")
