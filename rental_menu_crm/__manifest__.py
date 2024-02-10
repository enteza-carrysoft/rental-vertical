# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    "name": "Rental Menu CRM",
    "summary": "Add CRM to the Rental Menu",
    "version": "15.0.1.0.0",
    "category": "Rental",
"author": "zvERP.com, elego Software Solutions GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/pcastelovigo/rental-vertical",
    "description": """
This module adds menu entries for CRM to the rental application.
""",
    "depends": [
        "rental_base",
        "crm",
    ],
    "data": [
        "views/menu_view.xml",
    ],
    "demo": [],
    "qweb": [],
    "application": False,
    "installable": True,
    "license": "AGPL-3",
}
