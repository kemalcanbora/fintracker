from pydantic import BaseModel
from typing import Optional, List


class CoinNewsModel(BaseModel):
    source: Optional[str]
    urls: Optional[List[str]]