from repositories.search_group_policy_repository import SearchGroupPolicyRepository
from core.logger import app_logger

class SearchGroupPolicyService:
    def __init__(self, db):
        self.db = db

    def search_group_policy_serv(self, request):
        return SearchGroupPolicyRepository.search_group_policy_repo(self.db)