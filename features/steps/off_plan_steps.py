from behave import given, when, then


@then('Verify the right page opens')
def verify_off_plan_page_open(context):
    context.app.off_plan_page.verify_off_plan_page_open()


@when('Filter the products by price range from {price_from} to {price_to} AED')
def select_filter_by_price_range(context, price_from, price_to):
    context.app.off_plan_page.select_filter_by_price_range(price_from, price_to)


@then('Verify the price in all cards is inside the range ({price_from} - {price_to})')
def verify_products_in_price_range(context, price_from, price_to):
    context.app.off_plan_page.verify_products_in_price_range(price_from, price_to)
