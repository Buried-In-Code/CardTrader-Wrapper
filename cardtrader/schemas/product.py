from dataclasses import dataclass, field
from typing import Dict, Optional, Union

from dataclasses_json import Undefined, config, dataclass_json


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Price:
    cents: int
    currency: str
    currency_symbol: str
    formatted: str


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Expansion:
    id_: int = field(metadata=config(field_name="id"))
    code: str
    name: str = field(metadata=config(field_name="name_en"))


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class User:
    country_code: str
    too_many_request_for_cancel_as_seller: bool
    user_type: str
    can_sell_sealed_with_ct_zero: bool
    max_sellable_in24h_quantity: Optional[int]
    id_: int = field(metadata=config(field_name="id"))
    username: str
    can_sell_via_hub: bool


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class Product:
    quantity: int
    description: Optional[str]
    price_cents: int
    layered_price_cents: int
    blueprint_id: int
    expansion: Expansion
    graded: bool
    id_: int = field(metadata=config(field_name="id"))
    tag: Optional[str]
    bundle_size: int
    on_vacation: bool
    seller: User = field(metadata=config(field_name="user"))
    price_currency: str
    name: str = field(metadata=config(field_name="name_en"))
    price: Price
    properties: Dict[str, Union[str, bool]] = field(
        default_factory=dict, metadata=config(field_name="properties_hash")
    )
