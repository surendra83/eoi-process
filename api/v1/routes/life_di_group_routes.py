import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status, Request
from sqlalchemy import  text
from typing import List
from database.session import get_db
from core.logger import app_logger
from schemas.life_di_group_schema import GroupRequest, LifeDIGroupResponse
from schemas.search_group_policy_schema import SearchGroupPolicy
   
from controllers.life_di_group_controller import LifeDiGroupController
from controllers.search_group_policy_controller import SearchGroupPolicyController

router = APIRouter(
    prefix="/sbm-eoi-automation",
    tags=["SBM EOI Automation"]
)

@router.get("/search-group-policy", response_model=List[SearchGroupPolicy])
def get_search_group_policy(request: Request, db: Session = Depends(get_db)):
    result = SearchGroupPolicyController.search_group_policy(db=db,request=request)
    return result

@router.post("/reports",response_model=LifeDIGroupResponse)
def get_details(group_request: GroupRequest, request: Request, db: Session = Depends(get_db)):
    app_logger.bind(
        log_id=str(uuid.uuid4()),
        request_body=group_request.dict() if group_request else None,
        execute_method="get_details"
    ).info(f"Request received for groupNumber={group_request.groupNumber}")
    result = LifeDiGroupController.get_life_di_group_details(db=db,request=group_request)
    return result   

