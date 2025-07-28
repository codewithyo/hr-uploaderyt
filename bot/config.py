import os


class Config:

    BOT_TOKEN = os.environ.get("8293399742:AAEeOrAoDTd2qkwoyhfd5YOnC9dHNo_bVIM")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("28583543"))

    API_HASH = os.environ.get("24fd6e53b6034ccbda0bfd62dfd47ad3")

    CLIENT_ID = os.environ.get("180064799903-ihosiokdglohin0giqr0pg872j5i76t7.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "7990155194,7612404009")

    AUTH_USERS = [BOT_OWNER, 7990155194] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "by HR")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("unlisted") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
