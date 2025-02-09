from ..script import main


class TestScript:
    def test_main(self):
        v = main()
        assert v == "Hello from module-a!"
