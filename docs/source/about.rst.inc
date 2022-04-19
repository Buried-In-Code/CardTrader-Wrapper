**CardTrader - Wrapper** is a python wrapper for the CardTrader API.

.. code-block:: python

    from cardtrader.service import CardTrader
    from cardtrader.sqlite_cache import SQLiteCache

    session = CardTrader(access_token="Access Token", cache=SQLiteCache())

    # List Games
    results = session.games()
    for game in results:
        print(f"{game.id_} | {game.display_name}")

    # List Magic: the Gathering Expansions
    results = [x for x in session.expansions() if x.game_id == 1]
    for expansion in results:
    	print(f"{expansion.id_} | {expansion.code} - {expansion.name}")

    # List Magic: the Gathering - Game Night Cards for sale
    blueprints = session.blueprints(expansion_id=1)
    for card_blueprint in blueprints:
    	products = session.products_by_blueprint(blueprint_id=card_blueprint.id_)
    	for product in products:
    		print(f"{product.price.formatted} | {card_blueprint.name}")
