from control.buck_model import simulate, metrics

def test_closed_loop_regulation():
    t, v, d, i = simulate()
    m = metrics(t, v, 3.3)
    assert abs(m["final_voltage"] - 3.3) < .08
    assert 0 <= d[-1] <= .95

def test_load_step_recovery():
    t, v, d, i = simulate(total_time=.025, load_step=(.012, 1.0))
    assert abs(v[-1] - 3.3) < .12
