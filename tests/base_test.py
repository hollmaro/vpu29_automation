import pytest

class BaseTest:
    @pytest.fixture(scope='function', autouse=True)
    def display_test_name(self, request):
        print(f'\n-------------Running test: {request.node.name}')
        yield
        print(f'\n-------------Test: {request.node.name} finished')
