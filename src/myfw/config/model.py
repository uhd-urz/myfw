from pydantic import BaseModel, Secret


class ConfigModel(BaseModel):
    """An example configuration model"""

    url: str = "https://example.org"
    api_token: Secret[str] = "555-2368"


# ConfigModel is registered in __pre_init__.register_config_model
