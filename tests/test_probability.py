from src.probability import simple_probability

def test_simple_probability():
    assert simple_probability(5,10) == 0.5
    assert simple_probability(0,10) == 0.0
    assert simple_probability(3,0) == 0.0
