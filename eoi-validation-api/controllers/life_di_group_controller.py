# controllers/life_di_group_controller.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.life_di_group_schema import GroupRequest
from fastapi import Request
from services.life_di_group_service import LifeDIGroupService
from core.logger import app_logger

class LifeDiGroupController:

    @staticmethod
    def get_life_di_group_details( db: Session, request: GroupRequest):
        service = LifeDIGroupService(db)
        if not request.groupNumber.isdigit():
            raise HTTPException(status_code=400, detail="groupNumber must be a numeric value")
            
        try:
            groupId = int(request.groupNumber)
            groupName = str(request.groupName)
            result = service.get_life_di_group_serv(groupId, groupName)
            if not result:
                raise HTTPException(
                    status_code=409,
                    detail=(
                        f"groupNumber={groupId} and groupName={groupName} are not identical each other"
                      )
                )

            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Record not found for groupNumber={groupId}"
                )

            return result
        except ValueError:
            raise HTTPException(status_code=400,detail="groupNumber must be a numeric value")
