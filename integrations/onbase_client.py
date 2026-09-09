import httpx

class OnBaseClient:

    async def publish_result(self,payload):
        
        async with httpx.AsyncClient() as client:

            response = await client.post("/publish",json=payload)
            return response.json()