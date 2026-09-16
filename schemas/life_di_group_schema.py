# schemas/life_di_groups_schema.py
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class GroupRequest(BaseModel):
    groupNumber: str

class ContactInformation(BaseModel):
    division_information: Dict[str, Any]
    eoi_primary_contact: Optional[Dict[str, Any]] = None
    eoi_secondary_contact: Optional[Dict[str, Any]] = None
    comments_subgroup: Optional[str] = None
  
class LifeDIGroupResponse(BaseModel):
    group_information: Dict[str, Any]
    contact_information: List[ContactInformation]
    product_information: Dict[str, Any]
    sold_class_benefits_rates_information: List[Dict[str, Any]]
    eligibility: List[Dict[str, Any]]
    
    