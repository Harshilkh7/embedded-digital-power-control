from control.pi_controller import PIController

def test_duty_is_bounded():
    c = PIController(10, 100, .001)
    for _ in range(100):
        assert 0 <= c.update(10, 0) <= .95

def test_reset():
    c = PIController(1, 2, .01)
    c.update(.2, 0)
    assert c.integral != 0
    c.reset()
    assert c.integral == 0
