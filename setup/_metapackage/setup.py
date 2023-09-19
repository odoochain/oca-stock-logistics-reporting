import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-reporting",
    description="Meta package for oca-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-delivery_line_sale_line_position>=15.0dev,<15.1dev',
        'odoo-addon-stock_account_valuation_report>=15.0dev,<15.1dev',
        'odoo-addon-stock_card_report>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_report_valued>=15.0dev,<15.1dev',
        'odoo-addon-stock_report_quantity_by_location>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
