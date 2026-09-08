from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.life_di_group_schema import GroupRequest
from fastapi import Request
from services.search_group_policy_service import SearchGroupPolicyService
from core.logger import app_logger

class SearchGroupPolicyController:
    @staticmethod
    def search_group_policy(db: Session, request: Request):
        service = SearchGroupPolicyService(db)
        result = service.search_group_policy_serv(request=request)
        return result