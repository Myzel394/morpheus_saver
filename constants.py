import os

from dotenv import load_dotenv
load_dotenv()

__all__ = [
    "CHANNEL_ID", "PLAYLIST_ID", "FAKE_NAMES", "NOTIFY_MESSAGE", "API_KEY", "CLIENT_SECRET", "CLIENT_ID", "SEARCH_AMOUNT"
]

CHANNEL_ID = "UCkZ3fSYruC0IXv6p34BHciQ"  # "The Morpheus Vlogs" channel
PLAYLIST_ID = "UUkZ3fSYruC0IXv6p34BHciQ"  # Uploads from "The Morpheus Vlogs"
# Removes based on lowercase authorDisplayName
FAKE_NAMES = [
    "the morpheus vlogs", "the morpheus-vlogs", "morpheus vlogs", "morpheus-vlogs", "morpheus", "the morpheus"
]
NOTIFY_MESSAGE = "ACHTUNG! Dies ist ein Fake-Account! Bitte meldet den Fake \"The Morpheus Vlogs\"-Kanal!"
SEARCH_AMOUNT = 900
API_KEY = os.getenv("API_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")