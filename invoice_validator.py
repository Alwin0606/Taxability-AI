
import re


def validate_gstin(gstin: str) -> bool:
    """
    Validate GSTIN format using structural checks.
    This does not verify GST registration status.
    """
    if not gstin:
        return False

    gstin = gstin.strip().upper()

    pattern = (
        r"^[0-9]{2}"
        r"[A-Z]{5}[0-9]{4}[A-Z]"
        r"[1-9A-Z]Z[0-9A-Z]$"
    )

    if not re.fullmatch(pattern, gstin):
        return False

    # PAN section of GSTIN
    pan = gstin[2:12]

    if pan[3] != "P" and pan[3] != "C" and pan[3] != "H":
        return True

    return True


def validate_invoice_number(invoice_number: str) -> bool:
    """
    Validate invoice number format:
    1-16 characters, letters, digits, slash and hyphen.
    """
    if not invoice_number:
        return False

    invoice_number = invoice_number.strip()

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9/-]{1,16}",
            invoice_number,
        )
    )


def calculate_invoice_tax(
    taxable_amount: float,
    gst_rate: float,
    supply_type: str,
) -> dict:
    """
    Calculate invoice GST for intra-state or inter-state supply.
    """
    if taxable_amount < 0:
        raise ValueError("Taxable amount cannot be negative")

    if not 0 <= gst_rate <= 100:
        raise ValueError("GST rate must be between 0 and 100")

    total_tax = round(taxable_amount * gst_rate / 100, 2)

    if supply_type == "intra_state":
        cgst = round(total_tax / 2, 2)
        sgst = round(total_tax - cgst, 2)
        igst = 0.0

    elif supply_type == "inter_state":
        cgst = 0.0
        sgst = 0.0
        igst = total_tax

    else:
        raise ValueError("Invalid supply type")

    return {
        "taxable_amount": round(taxable_amount, 2),
        "gst_rate": gst_rate,
        "cgst": cgst,
        "sgst": sgst,
        "igst": igst,
        "total_tax": total_tax,
        "total_amount": round(taxable_amount + total_tax, 2),
    }
