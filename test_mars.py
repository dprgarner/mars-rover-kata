from mars import Rover


class TestTurnLeft():
    def test_turns_left(self):
        rover = Rover((3, 3), 'N')
        rover.move(['l'])
        assert rover.direction == 'W'

    def test_turns_left_twice(self):
        rover = Rover((3, 3), 'N')
        rover.move(['l', 'l'])
        assert rover.direction == 'S'

    def test_turns_left_three_times(self):
        rover = Rover((3, 3), 'N')
        rover.move(['l', 'l', 'l'])
        assert rover.direction == 'E'

    def test_turns_left_four_times(self):
        rover = Rover((3, 3), 'N')
        rover.move(['l', 'l', 'l', 'l'])
        assert rover.direction == 'N'


class TestTurnRight():
    def test_turns_right(self):
        rover = Rover((3, 3), 'N')
        rover.move(['r'])
        assert rover.direction == 'E'

    def test_turns_right_twice(self):
        rover = Rover((3, 3), 'N')
        rover.move(['r', 'r'])
        assert rover.direction == 'S'

    def test_turns_right_three_times(self):
        rover = Rover((3, 3), 'N')
        rover.move(['r', 'r', 'r'])
        assert rover.direction == 'W'

    def test_turns_right_four_times(self):
        rover = Rover((3, 3), 'N')
        rover.move(['r', 'r', 'r', 'r'])
        assert rover.direction == 'N'


class TestMoveForwards():
    def test_moves_forwards_north(self):
        rover = Rover((3, 3), 'N')
        rover.move(['f', 'f'])
        assert rover.position == (3, 5)

    def test_moves_forwards_east(self):
        rover = Rover((3, 3), 'E')
        rover.move(['f', 'f'])
        assert rover.position == (5, 3)

    def test_moves_forwards_south(self):
        rover = Rover((3, 3), 'S')
        rover.move(['f', 'f'])
        assert rover.position == (3, 1)

    def test_moves_forwards_west(self):
        rover = Rover((3, 3), 'W')
        rover.move(['f'])
        assert rover.position == (2, 3)


class TestMoveBackwards():
    def test_moves_backwards_facing_north(self):
        rover = Rover((3, 3), 'N')
        rover.move(['b'])
        assert rover.position == (3, 2)

    def test_moves_backwards_facing_east(self):
        rover = Rover((3, 3), 'E')
        rover.move(['b', 'b'])
        assert rover.position == (1, 3)

    def test_moves_backwards_facing_south(self):
        rover = Rover((2, 2), 'S')
        rover.move(['b'])
        assert rover.position == (2, 3)

    def test_moves_backwards_facing_west(self):
        rover = Rover((2, 2), 'W')
        rover.move(['b'])
        assert rover.position == (3, 2)


class TestEdgeCases():
    def test_ignores_unrecognised_instruction(self):
        rover = Rover((3, 3), 'N')
        rover.move(['x'])
        assert rover.position == (3, 3)


class TestEastWestWrapping():
    def test_moves_forwards_around_mars_to_east(self):
        rover = Rover((3, 3), 'E')
        rover.move(['f', 'f', 'f'])
        assert rover.position == (1, 3)

    def test_moves_backwards_around_mars_to_east(self):
        rover = Rover((3, 3), 'W')
        rover.move(['b', 'b', 'b'])
        assert rover.position == (1, 3)

    def test_moves_forwards_around_mars_to_west(self):
        rover = Rover((3, 3), 'W')
        rover.move(['f', 'f', 'f'])
        assert rover.position == (5, 3)

    def test_moves_backwards_around_mars_to_west(self):
        rover = Rover((3, 3), 'E')
        rover.move(['b', 'b', 'b'])
        assert rover.position == (5, 3)


class TestNorthSouthWrapping():
    """
    Assumes that north pole wrapping happens at y > 5.
    """

    def test_moves_forwards_over_south_pole(self):
        rover = Rover((1, 1), 'S')
        rover.move(['f'])
        assert rover.position == (5, 1)
        assert rover.direction == 'N'

    def test_moves_backwards_over_south_pole(self):
        rover = Rover((1, 1), 'N')
        rover.move(['b'])
        assert rover.position == (5, 1)
        assert rover.direction == 'S'

    def test_moves_forwards_over_north_pole(self):
        rover = Rover((2, 5), 'N')
        rover.move(['f'])
        assert rover.position == (4, 5)
        assert rover.direction == 'S'

    def test_moves_backwards_over_north_pole(self):
        rover = Rover((1, 5), 'S')
        rover.move(['b'])
        assert rover.position == (5, 5)
        assert rover.direction == 'N'


class TestObstacles():
    def test_does_not_move_into_obstacle(self):
        rover = Rover((2, 3), 'E', [(3, 3)])
        rover.move(['f'])
        assert rover.position == (2, 3)

    def test_does_not_move_backward_into_obstacle(self):
        rover = Rover((3, 3), 'N', [(3, 2)])
        rover.move(['b'])
        assert rover.position == (3, 3)

    def test_does_not_move_again_after_hitting_obstacle(self):
        rover = Rover((3, 3), 'N', [(3, 4)])
        rover.move(['f', 'l', 'f'])
        assert rover.position == (3, 3)

    def test_reports_the_obstacle(self):
        rover = Rover((3, 3), 'N', [(1, 1), (3, 4)])
        obstacle = rover.move(['f', 'l', 'f'])
        assert obstacle == (3, 4)
