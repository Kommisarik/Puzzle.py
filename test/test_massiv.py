from unittest import TestCase, main
import Sliding_game


class Massiv_test(TestCase):
    def test_check_win(self):
        correct_indices = list(range(15)) + [-1]
        self.assertEqual(IPG_game.check_win_for_test(correct_indices), True)
        pass

    def test_move_tile(self):
        clicked_index = 1
        empty_index = 14
        self.assertEqual(IPG_game.test_move_tile(clicked_index, empty_index), 1)
        pass

if __name__ == '__main__':
        main()