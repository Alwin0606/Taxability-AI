
from collections import defaultdict


def generate_gstr1_summary(invoices: list[dict]) -> dict:
    summary = defaultdict(
        lambda: {
            "invoice_count": 0,
            "taxable_value": 0.0,
            "cgst": 0.0,
            "sgst": 0.0,
            "igst": 0.0,
            "total_tax": 0.0,
            "total_value": 0.0,
        }
    )

    for invoice in invoices:
        category = invoice.get("supply_category", "B2C")
        gst_rate = float(invoice["gst_rate"])
        key = (category, gst_rate)

        taxable = float(invoice["taxable_amount"])
        cgst = float(invoice.get("cgst", 0))
        sgst = float(invoice.get("sgst", 0))
        igst = float(invoice.get("igst", 0))

        tax = round(cgst + sgst + igst, 2)
        total = round(taxable + tax, 2)

        item = summary[key]
        item["invoice_count"] += 1
        item["taxable_value"] += taxable
        item["cgst"] += cgst
        item["sgst"] += sgst
        item["igst"] += igst
        item["total_tax"] += tax
        item["total_value"] += total

    rows = []

    for (category, rate), values in summary.items():
        rows.append({
            "supply_category": category,
            "gst_rate": rate,
            **{
                name: round(value, 2)
                if isinstance(value, float)
                else value
                for name, value in values.items()
            },
        })

    return {
        "invoice_count": len(invoices),
        "summary": rows,
        "totals": {
            "taxable_value": round(
                sum(i["taxable_amount"] for i in invoices), 2
            ),
            "total_tax": round(
                sum(
                    i.get("cgst", 0)
                    + i.get("sgst", 0)
                    + i.get("igst", 0)
                    for i in invoices
                ), 2
            ),
            "total_value": round(
                sum(
                    i["taxable_amount"]
                    + i.get("cgst", 0)
                    + i.get("sgst", 0)
                    + i.get("igst", 0)
                    for i in invoices
                ), 2
            ),
        },
    }
