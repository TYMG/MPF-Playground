import os
from mpf.tests.MpfTestCase import MpfTestCase


class TestBasicGame(MpfTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_single_player_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(.1)
        # game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)
        # playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)
        # but its not there yet
        self.assertEqual(0, self.machine.playfield.balls)

        self.advance_time_and_run(3)
        # player presses eject
        self.hit_and_release_switch("s_plunger")

        # after 3 its there
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_return")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)

        self.assertTextOnTopSlide("BALL 1    FREE PLAY")

    def test_flippers(self):
        self.assertModeRunning('attract')
        # really this is just testing the everything loads without errors since
        # there's not much going on yet.
        print(self)
        assert 'left_flipper' in self.machine.flippers
        assert 'right_flipper' in self.machine.flippers
        self.hit_switch_and_run("s_trough1", 1)
        self.hit_switch_and_run("s_trough2", 1)
