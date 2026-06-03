"""Data contract customizations for Reed's streaming consumer."""

from typing import Final

from streaming.data_validation.data_contract_case import (
    SALES_REQUIRED_FIELDS,
)

CONSUMED_FIELDNAMES: Final[list[str]] = [
    *SALES_REQUIRED_FIELDS,
    "subtotal",
    "currency_subtotal",
    "tax_amount",
    "total",
    "_kafka_key",
    "_kafka_partition",
    "_kafka_offset",
]
