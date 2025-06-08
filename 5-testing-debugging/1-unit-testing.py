def double_num(n):
    return n * 2

def test_double_num():
    assert double_num(4) == 8
    assert double_num(2.5) == 5.0
    assert double_num("Tofu") == "TofuTofu"
    print("✅ All tests passed!")

test_double_num()
