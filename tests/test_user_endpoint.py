import pytest
from rest_api_testing import BaseApiTest
from rest_api_testing.auth import oauth_scopes

@oauth_scopes('user:read')
class TestUserEndpoint(BaseApiTest):
    
   async def test_unauthenticated_request(self):
        """Test unauthenticated request."""
        request = await self.unauthenticated_request()
        response = request.get("/users/1")
        await response.should_have.status_code(200)
        await response.should_have.json_path("id", exists=True)
        await response.should_have.json_path("name", exists=True)
        await response.should_have.json_path("email", exists=True)
        await response.should_have.json_path("age", exists=True)
        await response.should_have.json_path("phone", exists=True)