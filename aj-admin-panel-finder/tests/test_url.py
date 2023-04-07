import pytest

from AJadminfinder._classes import AJadminfinder


@pytest.mark.parametrize(
    "urls, expected_urls",
    [
        ("https://example.com", True),
        ("http://example.com", True),
        ("https://www.example.com", True),
        ("http://www.example.com", True),
    ],
)
def test_url(urls, expected_urls):
    assert (
        AJadminfinder.check_url(urls, headers=None, proxies=None) == expected_urls
    )  # noqa: E501


@pytest.mark.parametrize(
    "bad_urls", [("example.com"), ("www.example.com"), ("example")]
)
def test_bad_urls(bad_urls):
    with pytest.raises(SystemExit):
        AJadminfinder.create_link(bad_urls)


@pytest.mark.parametrize(
    "proxies,expected_proxies",
    [
        (
            "127.0.0.1:80",
            {"http": "http://127.0.0.1:80", "https": "http://127.0.0.1:80"},
        ),
    ],
)
def test_proxy(proxies, expected_proxies):
    assert AJadminfinder.get_proxy(proxies) == expected_proxies
