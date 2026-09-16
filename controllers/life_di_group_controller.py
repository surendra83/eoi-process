# controllers/life_di_group_controller.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.life_di_group_schema import GroupRequest
from fastapi import Request
from services.life_di_group_service import LifeDIGroupService
from core.logger import app_logger
from core.exceptions import APIException

class LifeDiGroupController:
    @staticmethod
    def get_life_di_group_details( db: Session, request: GroupRequest):
        service = LifeDIGroupService(db)
        if not request.groupNumber.isdigit():
            raise APIException(status_code=400, messages="groupNumber must be a numeric value")
            
        try:
            groupId = int(request.groupNumber)
            result = service.get_life_di_group_serv(groupId)
            if not result:
                raise APIException(
                    status_code=404,
                    messages=f"Record not found for groupNumber={groupId}"
                )

            return result
        except ValueError:
            raise APIException(status_code=400,messages="groupNumber must be a numeric value")
