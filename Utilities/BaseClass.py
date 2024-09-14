import pytest

from conftest import setup


@pytest.mark.usefixtures("setup")
class Baseclass():
    pass