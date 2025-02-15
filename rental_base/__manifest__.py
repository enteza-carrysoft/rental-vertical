# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    "name": "Rental Base",
    "version": "15.0.1.0.0",
    "category": "Rental",
    "summary": "Manage Rental of Products",
"author": "zvERP.com, elego Software Solutions GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/flinq-ingenieria/rental-vertical",
    "description": """
Base Module for Rental Management

This module provides a new menu for rental management.
It is based on the sale_rental module that currently can be found in sale-workflow repository.
""",
    "depends": [
        "account",
        "product_analytic",
        "sale",
        "sale_order_type",
        "sale_rental",
        "sale_start_end_dates",
        "sale_stock",
        "sales_team",
    ],
    "data": [
        "security/ir.model.access.csv",
	"data/res_config.xml",
        "data/ir_sequence_data.xml",
        "data/order_type_data.xml",
        "data/product_uom_data.xml",
        "wizard/update_sale_line_date_view.xml",
        "views/res_config_settings_view.xml",
        "views/stock_picking_views.xml",
        "views/product_views.xml",
        "views/menu_view.xml",
        "views/sale_view.xml",
    ],
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}
