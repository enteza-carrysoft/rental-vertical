# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    "name": "Rental Timeline",
    "summary": "Adds a timeline to products as well as a timeline view as overview of all rental products and orders",
    "description": """
This module extends the sale_rental module to create and change the timeline objects
for the rented product instances automatically.
A complete timeline view containing all rental orders will be generated for all rentable products.

This module adds the basic rental timeline view as well as an extension to the product form view.
    """,
    "usage": """
Just install this module to add the rental timeline view to your system. No further configuration is necessary.
    """,
    "version": "15.0.1.0.0",
    "category": "Rental",
"author": "zvERP.com, elego Software Solutions GmbH, Odoo Community Association (OCA)",
    "depends": [
        "web_timeline",
        "rental_base",
        "rental_product_variant",
        "web",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_timeline_view.xml",
        "views/product_view.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_backend": [
            (
                "replace",
                "web/static/src/legacy/legacy_views.js",
                "rental_timeline/static/src/js/legacy/legacy_views.js",
            ),
            (
                "replace",
                "stock/static/src/js/report_stock_forecasted.js",
                "rental_timeline/static/src/js/report_stock_forecasted.js",
            ),
            (
                "replace",
                "web/static/src/legacy/js/widgets/pie_chart.js",
                "rental_timeline/static/src/js/legacy/js/widgets/pie_chart.js",
            ),
            "rental_timeline/static/src/scss/rental_timeline.scss",
            "rental_timeline/static/src/js/timeline_view.js",
            "rental_timeline/static/src/js/timeline_renderer.js",
            "rental_timeline/static/src/js/timeline_controller.js",
            "rental_timeline/static/src/js/Popup.js",
            "rental_timeline/static/src/js/legacy/legacy_views.js",
            "rental_timeline/static/src/js/report_stock_forecasted.js",
            "rental_timeline/static/src/js/legacy/js/widgets/pie_chart.js",
        ],
    },
    "application": False,
    "license": "AGPL-3",
}
