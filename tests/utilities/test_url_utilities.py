from utilities.url_utilities import load_url_from_files


def test_load_file():
    tests_urls = load_url_from_files("input.txt")
    assert (len(tests_urls) > 1)
