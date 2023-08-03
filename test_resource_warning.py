import pytest
import requests
import vcr


@pytest.fixture
def sess():
    with requests.Session() as sess:
        yield sess


def test_generate_resource_warning(sess):
    with vcr.use_cassette(path="test_generate_resource_warning.yaml"):
        sess.get("https://google.com")
        # sess.close()


def test_works_ok(sess):
    sess.get("https://google.com")
