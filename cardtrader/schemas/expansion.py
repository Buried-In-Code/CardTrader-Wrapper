from dataclasses import dataclass, field

from dataclasses_json import Undefined, config, dataclass_json


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Expansion:
    id_: int = field(metadata=config(field_name="id"))
    game_id: int
    code: str
    name: str
