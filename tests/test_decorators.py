from decorators import log


def test_log():
    @log()
    @log("pivas.txt")
    def delite(a,b):
        return a / b