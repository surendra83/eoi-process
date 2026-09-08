import httpx

class CirrusClient:

    async def get_policy(self,policy_id: str):

        async with httpx.AsyncClient() as client:

            response = await client.get(f"/policy/{policy_id}")

            return response.json()