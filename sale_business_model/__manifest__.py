{
    'name': "Sale - Business Model",
    'summary': """
        Add a way to categorize client based on Business Model""",
    'description': """
        v1.0.0:
            * Add new field Business Model inside sale
            * Change SO display name to include the business model
            * Group SO based on business model
            * Show tax on SO Line based on business model
    """,
    'author': "Akhmad Maulana Akbar",
    'website': "https://akhmad.id",
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
        'views/account_tax_views.xml',
    ],
}
