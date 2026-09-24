# controllers/life_di_group_controller.py
import uuid
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
            raise APIException(status_code=400, messages="Invalid groupNumber")

        groupId = int(request.groupNumber)    
        try:   
            result = service.get_life_di_group_serv(groupId)
            if not result:
                app_logger.bind(
                    log_id=str(uuid.uuid4()),
                    request_body=request.dict() if request else None
                ).warning(f"No record found for groupNumber={groupId}")
                raise APIException(
                    status_code=404,
                    messages=f"Record not found for groupNumber={groupId}"
                )
            app_logger.bind(
                log_id=str(uuid.uuid4()),
                request_body=request.dict() if request else None,
                execute_method="get_life_di_group_details"
            ).info(f"Record found for groupNumber={groupId}")
            return result
        except ValueError:
            app_logger.bind(
                log_id=str(uuid.uuid4()),
                request_body=request.dict() if request else None,
                execute_method="get_life_di_group_details"
            ).error(f"Invalid groupNumber={request.groupNumber}")
            raise APIException(status_code=400,messages="Invalid groupNumber")
