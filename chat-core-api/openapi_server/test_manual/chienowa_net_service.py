from openapi_server.services.chienowa_net_service import ChienowaNetService
from openapi_server.test_manual import BaseTestCase, ignore_warnings


class TestServiceForChienowaNetService(BaseTestCase):
    @ignore_warnings
    def test_01_get_aggregations(self):
        service = ChienowaNetService()
        ret_data = service.get_aggregations(4)
        print("Aggregations ->>>  ", ret_data)
