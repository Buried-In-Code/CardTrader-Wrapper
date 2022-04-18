from dataclasses import dataclass, field

from dataclasses_json import Undefined, config, dataclass_json


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Game:
    id_: int = field(metadata=config(field_name="id"))
    name: str
    display_name: str
