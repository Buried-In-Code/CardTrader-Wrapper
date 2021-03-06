from cardtrader.service import CardTrader


def test_expansions(session: CardTrader):
    results = session.expansions()
    result = [x for x in results if x.expansion_id == 1]
    assert len(result) == 1
    assert result[0].expansion_id == 1
    assert result[0].game_id == 1
    assert result[0].code == "gnt"
    assert result[0].name == "Game Night"
