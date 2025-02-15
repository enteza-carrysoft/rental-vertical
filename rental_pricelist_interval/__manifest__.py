# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    "name": "Rental Pricelist (Interval)",
    "summary": "Enables the user to define different rental prices "
    "time uom (Month, Day and Hour).",
    "version": "15.0.1.0.0",
    "category": "Rental",
"author": "zvERP.com, elego Software Solutions GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/flinq-ingenieria/rental-vertical",
    "description": """
This Module implements a new rental service product for interval pricing under consideration
of odoo price lists. This enables to rent out products and charge for day interval ranges.

These ranges can be configured freely on general and/or product level. In contrast to rentals
on daily, monthly or yearly bases a different price computation is applied in sale order lines.
""",
    "configuration": """
To configure this module, you need to:

#. Go to company settings and define the default interval ranges on 'Rental Interval Prices' tab.
   These ranges will be applied for computation of price intervals for rental service products when interval pricing is activated
   in stockable product.

#. If desired go to 'RS (Prefix and Suffix)' tab an define how rental interval service product
   names and reference numbers are created.
""",
    "contributors": [
        "Ben Brich <b.brich@humanilog.org> (www.humanilog.org)",
        "Yu Weng <yweng@elegosoft.com> (www.elegosoft.com)",
    ],
    "depends": [
        "rental_pricelist",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/product_uom_data.xml",
        "data/product_pricelist_data.xml",
        "views/product_pricelist_view.xml",
        "views/product_view.xml",
        "views/res_company_view.xml",
    ],
    "demo": [],
    "qweb": [],
    "post_init_hook": "set_product_def_interval_pricelist_id",
    "application": False,
    "installable": True,
    "license": "AGPL-3",
}
