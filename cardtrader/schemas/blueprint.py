from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from dataclasses_json import Undefined, config, dataclass_json


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Property:
    name: str
    type_: str = field(metadata=config(field_name="type"))
    default_value: Optional[str] = None
    possible_values: List[Union[str, bool]] = field(default_factory=list)


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Blueprint:
    id_: int = field(metadata=config(field_name="id"))
    name: str
    version: Optional[str] = None
    game_id: int
    category_id: int
    expansion_id: int
    image_url: str
    card_market_id: int
    tcg_player_id: Optional[int] = None
    scryfall_id: str
    fixed_properties: Dict[str, str] = field(default_factory=dict)
    editable_properties: List[Property] = field(default_factory=list)
