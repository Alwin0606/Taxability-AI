
from app.schemas.tax import GSTRequest, GSTResponse, TaxCategory, SupplyType


def calculate_gst(data: GSTRequest) -> GSTResponse:
    rate = data.gst_rate if data.tax_category == TaxCategory.TAXABLE else 0.0

    total_tax = round(data.amount * rate / 100, 2)
    cgst = 0.0
    sgst = 0.0
    igst = 0.0

    if data.tax_category == TaxCategory.TAXABLE:
        if data.supply_type == SupplyType.INTRA_STATE:
            cgst = round(total_tax / 2, 2)
            sgst = round(total_tax - cgst, 2)
        else:
            igst = total_tax

    return GSTResponse(
        amount=data.amount,
        tax_category=data.tax_category,
        supply_type=data.supply_type,
        gst_rate=rate,
        cgst=cgst,
        sgst=sgst,
        igst=igst,
        total_tax=total_tax,
        total_amount=round(data.amount + total_tax, 2),
    )
