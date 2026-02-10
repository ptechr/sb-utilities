from sb_utilities import remove_non_ascii

def test_remove_non_ascii():
    assert remove_non_ascii('Test') == "Test"