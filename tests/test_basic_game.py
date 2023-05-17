import os
from mpfmc.tests.MpfIntegrationTestCase import MpfIntegrationTestCase


class TestBasicGame(MpfIntegrationTestCase):

    def getConfigFile(self):
        return '../config.yaml'

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def get_platform(self):
        return 'smart_virtual'

    def test_flippers(self):
        # really this is just testing the everything loads without errors since
        # there's not much going on yet.
        assert 'left_flipper' in self.machine.flippers
        assert 'right_flipper' in self.machine.flippers
