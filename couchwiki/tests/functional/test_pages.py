from couchwiki.tests import *

class TestPagesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='pages', action='index'))
        # Test response...
