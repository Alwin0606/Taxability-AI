
from enum import Enum
from pydantic import BaseModel, Field


class TaxCategory(str, Enum):
    TAXABLE = "taxable"
    EXEMPT = "exempt"
    NON_GST = "non_gst"


class SupplyType(str, Enum):
    INTRA_STATE = "intra_state"
    INTER_STATE = "inter_state"


class GSTRequest(BaseModel):
    amount: float = Field(gt=0, description="Taxable value in INR")
    tax_category: TaxCategory
    supply_type: SupplyType
    gst_rate: float = Field(
        default=18.0,
        ge=0,
        le=100,
        description="GST rate percentage"
    )


class GSTResponse(BaseModel):
    amount: float
    tax_category: TaxCategory
    supply_type: SupplyType
    gst_rate: float
    cgst: float
    sgst: float
    igst: float
    total_tax: float
    total_amount: float

