import os
import pytest
import uuid
from rest_api_testing import BaseApiTest
from rest_api_testing.auth import oauth_scopes

@oauth_scopes("pingDirectory:users:write","pingDirectory:users:read", "pingDirectory:users:delete")
class TestUserEndpoint(BaseApiTest):
   
     endpointBase = "/sys-ping-directory-v1"
     endpoint = endpointBase + "/api/users"
     healthcheck = endpointBase + "/actuator/health"
     apiDocs = endpointBase + "/api/api-docs"
     current_dir = os.path.dirname(os.path.abspath(__file__))
     templates_dir = os.path.join(current_dir, "templates")
     os.makedirs(templates_dir, exist_ok=True)

     async def test_healthcheck(self):
          """Test healthcheck endpoint."""
          request = await self.authenticated_request()
          response = request.get(self.healthcheck)
          await response.should_have.status_code(200)
          await response.should_have.json_path("status", "UP")

     async def test_unauthenticated_request(self):
          """Test unauthenticated request."""
          request = await self.unauthenticated_request()
          response = request.get(self.endpoint)
          await response.should_have.status_code(401)

     async def test_get_api_spec(self):
          """Test retrieving the API specification."""
          request = await self.authenticated_request()
          response = request.get(self.apiDocs)
          await response.should_have.status_code(200)
          await response.should_have.json_path("openapi", "3.1.0")

     async def test_create_user_from_template(self):
          """Test creating a user from a template."""
          request = await self.authenticated_request()
          user_id = str(uuid.uuid4())
          user_data = self.render_template_with_csv(
               self.templates_dir + "\\user_creation_template.json.j2", 
               self.templates_dir + "\\user_creation_data.csv", 
               row_index=0, additional_context={"uid": user_id, "emailAddress": f"user-{user_id}@example.com"})
          response = request.post(self.endpoint, body=user_data)
          await response.should_have.status_code(201)
          await response.should_have.json_path("userId", user_id)
