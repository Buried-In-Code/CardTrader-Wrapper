"""
The Test Info module.

This module contains tests for Info objects.
"""
from cardtrader.service import CardTrader


def test_info(session: CardTrader):
    """Test the Info function."""
    result = session.info()
    assert result.id_ == 4263
    assert result.name == "BuriedInCode App 20220418050011"
