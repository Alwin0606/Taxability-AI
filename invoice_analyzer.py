
import re
from typing import Any


def analyze_invoice(invoice: dict[str, Any]) -> dict[str, Any]:
    errors = []
    warnings = []

    invoice_number = invoice.get("invoice_number")
    supplier_gstin = invoice.get("supplier_gstin")
    customer_gstin = invoice.get("customer_gstin")
    amount = invoice.get("amount")
    gst_rate = invoice.get("gst_rate")

    if not invoice_number:
        errors.append("Invoice number is missing.")

    if not supplier_gstin:
        errors.append("Supplier GSTIN is missing.")
    elif not re.fullmatch(
        r"[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]",
        supplier_gstin.upper()
    ):
        errors.append("Supplier GSTIN format is invalid.")

    if customer_gstin and not re.fullmatch(
        r"[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]",
        customer_gstin.upper()
    ):
        errors.append("Customer GSTIN format is invalid.")

    if amount is None or amount <= 0:
        errors.append("Invoice amount must be greater than zero.")

    if gst_rate is not None and not 0 <= gst_rate <= 100:
        errors.append("GST rate must be between 0 and 100.")

    if supplier_gstin and customer_gstin:
        if supplier_gstin[:2] != customer_gstin[:2]:
            warnings.append(
                "Supplier and customer GSTIN state codes differ. "
                "Verify place of supply and applicable tax type."
            )

    return {
        "invoice_number": invoice_number,
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "status": "valid" if not errors else "invalid",
    }

