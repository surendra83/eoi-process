from sqlalchemy import text
from sqlalchemy.orm import Session

class SearchGroupPolicyRepository:

    @staticmethod
    def search_group_policy_repo(db: Session):
        query = text("""
                SELECT
                    TS_GROUP_POLICY_NUMBER AS groupNumber,
                    TS_GROUP_NAME AS groupName,
                    COUNT(*) AS policyCount
                FROM ULD_LIFE_DI
                WHERE TS_GROUP_TERM_DATE IS NULL
                AND TS_GROUP_POLICY_NUMBER IS NOT NULL
                AND TS_GROUP_NAME IS NOT NULL
                GROUP BY
                    TS_GROUP_POLICY_NUMBER,
                    TS_GROUP_NAME
                ORDER BY policyCount DESC
              """)
        result = db.execute(query)
        rows = result.mappings().all()
        return [dict(row) for row in rows]
