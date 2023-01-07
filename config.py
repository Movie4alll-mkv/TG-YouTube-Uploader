import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8")

    APP_ID = int(os.environ.get("APP_ID", "6534707"))

    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")
    
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "@animecolony")
