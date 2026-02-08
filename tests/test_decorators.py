from src.decorators import log


def test_log() -> None:
    @log()
    @log("pivas.txt")
    @log(filename=None)
    def delite(a: int, b: int) -> float:
        return a / b

    result = delite(66546, 3468426)
    assert result == 0.01918622452951281
    result = delite("jhgfjhg", "sdhj")
