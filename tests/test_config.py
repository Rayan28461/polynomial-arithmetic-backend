from src.config import Config


class TestConfig:
    class TestApp:
        def test_title(self) -> None:
            assert Config.APP.TITLE == "Polynomial Arithmetic Calculator"

        def test_description(self) -> None:
            assert (
                Config.APP.DESCRIPTION
                == "A simple polynomial arithmetic calculator API"
            )

        def test_version(self) -> None:
            assert Config.APP.VERSION == "0.1.0"

    class TestTesting:
        class TestRandom:
            def test_seed(self) -> None:
                assert Config.Testing.RANDOM.SEED == 0
