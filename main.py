"""
main.py
Hi ma'am this is the python file that runs both pages of our site through PyScript.

We have two functions here:
  - SKU_generator: takes the category, product name, and quantity the user
    typed in and turns it into a SKU code (used on index.html)
  - create_order: checks which menu items the user ticked, adds up the
    total, and shows a receipt (used on receipt_generator.html)
"""
from pyscript import document


def SKU_generator(e):
    """Builds the SKU code from whatever the user picked/typed and shows
    it on the page."""
    output = document.getElementById('sku_output')
    output.innerHTML = ""

    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value.strip()
    stock_qty = document.getElementById('quantity').value

    # We need both of these filled in, otherwise the SKU wouldn't make sense
    if not product_name or not stock_qty:
        output.innerHTML = "<p class='text-danger mb-0'>Please enter a product name and quantity.</p>"
        return

    # We padded the quantity to 3 digits so every SKU comes out the same length
    qty_padded = str(int(stock_qty)).zfill(3)
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + qty_padded

    output.innerHTML = f"""
        <div class='result-box'>
            <p class='mb-1 text-muted'>Generated SKU:</p>
            <p class='sku-code mb-0'>{sku}</p>
        </div>
    """


def create_order(e):
    """Goes through the menu checkboxes, figures out which ones were
    checked, adds up the total, and displays the receipt."""
    output = document.getElementById('show')
    output.innerHTML = ""

    # These are the ids we gave each checkbox in the HTML
    menu_item_ids = ["item1", "item2", "item3", "item4", "item5"]

    order_lines = []  # we'll collect each selected item's line here
    total = 0          # running total in pesos

    for item_id in menu_item_ids:
        checkbox = document.getElementById(item_id)

        if checkbox.checked:
            price = int(checkbox.value)
            label_text = document.getElementById(item_id + "-label").innerText
            total += price

            order_lines.append(
                f"""<div class='d-flex justify-content-between mb-1'>
                        <span>{label_text}</span>
                        <span>₱{price}</span>
                    </div>"""
            )

    # If nothing was checked, we didn't want to show an empty receipt
    if not order_lines:
        output.innerHTML = "<p class='text-danger mb-0'>Please select at least one item.</p>"
        return

    items_html = "".join(order_lines)

    output.innerHTML = f"""
        <div class='result-box'>
            <p class='mb-2 text-muted'>Order Summary:</p>
            {items_html}
            <hr class='my-2'>
            <div class='d-flex justify-content-between'>
                <span class='fw-bold'>Total</span>
                <span class='receipt-total'>₱{total}</span>
            </div>
        </div>
    """