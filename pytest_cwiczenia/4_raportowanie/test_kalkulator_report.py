from kalkulator import add, odejmowanie
import pytest
import logging


# pytest-html
# na końcu komendy uruchomiena testu --html=report.html --self-contained-html
# np.: python -m pytest -v -m register --html=report.html --self-contained-html

# python -m pytest -v -m register -> odpala testy z mark.register
# python -m pytest -v -m "smoke and register" odpala testy z mark.register i odpala testy z mark.smoke

@pytest.fixture
def logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%H:%M:%S"
    )
    log = logging.getLogger(__name__)
    log.info("Logger fixture initialized")
    return log


@pytest.mark.smoke
def test_add_positive():
    assert add(2, 2) == 4
    assert add(0, 2) == 2
    assert add(25, 44) == 69
    assert add(2, 2) == 4
    assert add(0, 2) == 2

@pytest.mark.register
def test_2(logger):
    logger.info("Running test_2")
    assert True
    logger.info("Finished test_2")


@pytest.mark.skip(reason="test w trakcie developmentu")
def test_3():
    assert False

@pytest.mark.xfail(reason="failuje bo tak")
def test_4():
    assert False

@pytest.mark.register
@pytest.mark.smoke
def test_5():
    assert True
