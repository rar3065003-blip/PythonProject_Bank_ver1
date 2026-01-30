from src.decorators import log


def test_log() -> None:
    @log()
    @log("pivas.txt")
    def delite(a: int, b: int) -> float:
        return a / b
