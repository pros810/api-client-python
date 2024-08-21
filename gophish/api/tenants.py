from gophish.models import Tenant
from gophish.api import APIEndpoint

class API(APIEndpoint):
    def __init__(self, api, endpoint='api/tenants/'):
        super(API, self).__init__(api, endpoint=endpoint, cls=Tenant)

    def get(self, tenant_id=None):
        """ Gets one or more tenants """

        return super(API, self).get(resource_id=tenant_id)

    def post(self, tenant):
        """ Creates a new tenant """

        return super(API, self).post(tenant)

    def put(self, tenant):
        """ Edits a tenant """

        return super(API, self).put(tenant)

    def delete(self, tenant_id):
        """ Deletes a tenant by ID """

        return super(API, self).delete(tenant_id)