from pydantic import BaseModel, Secret
from rya.config import ConfigMaker


class ConfigModel(BaseModel):
    """An example configuration model"""

    url: str = "https://example.org"
    api_token: Secret[str] = "555-2368"


ConfigMaker.add_model(ConfigModel)
