from utils import dict_transactions


def test_dict_transactions():
    assert dict_transactions("../data/operation.json") == []
    data:list[dict] = dict_transactions("../data/operations.json")
    assert data[0]['id'] == 441945886
    assert dict_transactions("../tests/empty.json") == []
    assert dict_transactions("../tests/dict.json") == []