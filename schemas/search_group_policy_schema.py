from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class SearchGroupPolicy(BaseModel):
    groupNumber: str
    groupName: str
