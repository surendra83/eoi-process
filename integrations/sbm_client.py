import httpx


class SBMClient:

    async def get_group(
            self,
            group_number: str
    ):

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"/groups/{group_number}"
            )

            return response.json()