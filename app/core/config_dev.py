import os
from pathlib import Path

from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig(BaseModel):
    


@dataclass
class LocalConfig(BaseConfig):
    GCP_DB_NAME: str = os.getenv("GCP_DB_NAME", "pan-api") + "-testing"
    GCP_TOKEN_DB: str = os.getenv("GCP_TOKEN_DB", "apikey") + "-testing"


@dataclass
class StagingConfig(BaseConfig):
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID", "cloud-run-staging-273104")
    GCP_BUCKET_NAME: str = os.getenv("GCP_BUCKET_NAME", "docsumo-pan-api-staging1")
    GCP_DB_NAME: str = os.getenv("GCP_DB_NAME", "pan-api") + "-staging"
    GCP_TOKEN_DB: str = os.getenv("GCP_TOKEN_DB", "apikey") + "-staging"


@dataclass
class TestingConfig(BaseConfig):
    GCP_DB_NAME: str = os.getenv("GCP_DB_NAME", "pan-api") + "-testing"
    GCP_TOKEN_DB: str = os.getenv("GCP_TOKEN_DB", "apikey") + "-testing"


@dataclass
class ProductionConfig(BaseConfig):
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID", "cloud-run-producation-273104")
    GCP_BUCKET_NAME: str = os.getenv("GCP_BUCKET_NAME", "docsumo-pan-api-prod")
    GCP_DB_NAME: str = os.getenv("GCP_DB_NAME", "pan-api") + "-prod"
    GCP_TOKEN_DB: str = os.getenv("GCP_TOKEN_DB", "apikey") + "-prod"


config_by_name = dict(
    staging=StagingConfig(),
    testing=TestingConfig(),
    prod=ProductionConfig(),
    local=LocalConfig(),
)
