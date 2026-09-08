# schemas/life_di_groups_schema.py
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class GroupRequest(BaseModel):
    groupNumber: str
    groupName: str

class ProductInformation(BaseModel):
    short_term_disability_std: Dict[str, Any]
    supplemental_dependent_life: Dict[str, Any]
    supplemental_life: Dict[str, Any]
    long_term_disability_ltd: Dict[str, Any]

class ContactInformation(BaseModel):
    division_information: Dict[str, Any]
    primary_contact: Dict[str, Any]
    secondary_contact: Dict[str, Any]
    comments_subgroup: Optional[str] = None
  
class LifeDIGroupResponse(BaseModel):
    group_information: Dict[str, Any]
    contact_information: List[ContactInformation]
    product_information: ProductInformation
    eligibility: List[Dict[str, Any]]
    sold_class_benefits_rates_information: List[Dict[str, Any]]
    evidence_of_insurability: Dict[str, Any]
    guaranteed_issue: Dict[str, Any]
    accidental_death_and_dismemberment: Dict[str, Any]
    life_insurance: Dict[str, Any]