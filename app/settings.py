import os
from pathlib import Path

# General info about the API
API_TITLE = "DeepFire"
API_DESCRIPTION = "A REST API for detecting the presence of fire in an image."
API_VERSION = "0.0.2"

# OPTIONAL: Share metadata about what users can request from the endpoints.
# These are intended shown on the UI, related only to a specific endpoint.
# Note: the value in the "name" field should match what goes in the
#       "tags" parameter of the corresponding app route in main.py!!
API_ENDPOINT_METADATA = (
    {
        "name": "",
        "description": "",
    },
)

# Tells the app how to find the config.yaml (for running ML inference)
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = os.path.join(BASE_DIR, "app", "config.yaml")

# Wraps all the API metadata as one dictionary
API_SETTINGS = {
    "title": API_TITLE,
    "description": API_DESCRIPTION,
    "version": API_VERSION,
    "openapi_tags": API_ENDPOINT_METADATA,
    "predictor_config_path": CONFIG_PATH,
}