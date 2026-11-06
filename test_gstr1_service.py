
from app.services.gstr1_service import generate_gstr1_summary


def test_gstr1_intra_state_summary():
    invoices = [
        {
            "invoice_number": "INV-001",
            "supply_category": "B2B",
            "taxable_amount": 10000,
            "gst_rate": 18,
            "cgst": 900,
            "sgst": 900,
            "igst": 0,
        }
    ]

    result = generate_gstr1_summary(invoices)

    assert result["invoice_count"] == 1
    assert result["totals"]["taxable_value"] == 10000
    assert result["totals"]["total_tax"] == 1800
    assert result["totals"]["total_value"] == 11800


def test_gstr1_inter_state_summary():
    invoices = [
        {
            "invoice_number": "INV-002",
            "supply_category": "B2B",
            "taxable_amount": 5000,
            "gst_rate": 18,
            "cgst": 0,
            "sgst": 0,
            "igst": 900,
        }
    ]

    result = generate_gstr1_summary(invoices)

    assert result["totals"]["taxable_value"] == 5000
    assert result["totals"]["total_tax"] == 900
    assert result["totals"]["total_value"] == 5900


def test_gstr1_multiple_invoices():
    invoices = [
        {
            "supply_category": "B2B",
            "taxable_amount": 10000,
            "gst_rate": 18,
            "cgst": 900,
            "sgst": 900,
            "igst": 0,
        },
        {
            "supply_category": "B2C",
            "taxable_amount": 2000,
            "gst_rate": 5,
            "cgst": 50,
            "sgst": 50,
            "igst": 0,
        },
    ]

    result = generate_gstr1_summary(invoices)

    assert result["invoice_count"] == 2
    assert result["totals"]["taxable_value"] == 12000
    assert result["totals"]["total_tax"] == 1900
    assert result["totals"]["total_value"] == 13900
    assert len(result["summary"]) == 2
