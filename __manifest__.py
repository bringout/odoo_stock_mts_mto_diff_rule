# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock MTS+MTO Diff Rule",
    "summary": "Add a MTS+MTO route that orders only the difference (Ordered - Qty Available)",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Warehouse",
    "website": "https://github.com/bringout/stock_mts_mto_diff_rule",  # Update with your repo
    "author": "bring.out doo Sarajevo, Odoo Community Association (OCA)",  # Customize
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock"],
    "data": ["data/stock_data.xml", "views/pull_rule.xml", "views/warehouse.xml"],
}