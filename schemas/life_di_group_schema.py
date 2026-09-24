# schemas/life_di_groups_schema.py
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class GroupRequest(BaseModel):
    groupNumber: str = Field(
        ...,
        pattern=r"^\d+$",
        examples=["303191"],
        min_length=3,
        description="A numeric group number with at least 3 digits"
    )

class ContactInformation(BaseModel):
    division_information: Dict[str, Any]
    eoi_primary_contact: Optional[Dict[str, Any]] = None
    eoi_secondary_contact: Optional[Dict[str, Any]] = None
    comments_subgroup: Optional[str] = None
  
class LifeDIGroupResponse(BaseModel):
    group_information: Dict[str, Any]
    contact_information: List[ContactInformation]
    eligibility: List[Dict[str, Any]]
    product_information: Dict[str, Any]
   
    
    
