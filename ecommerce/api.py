import frappe

@frappe.whitelist(allow_guest=True)
def get_items():
    get_product = frappe.get_doc(
        "Website Settings",  # This is likely incorrect, you're trying to get a single Website Setting
        
    )
    return get_product

@frappe.whitelist(allow_guest=True)
def get_banner():
    get_product = frappe.get_all(
        "Banner",  # Now the doctype exists
        fields=[ "title", "image", "description", "subtitle", "button_label", "route", "background_color", "title_class", "subtitle_class", "reverse" ,
           "description_class"       ]  # You can add more fields here if needed
    )
    return get_product

@frappe.whitelist(allow_guest=True)
def get_hero():
    get_product = frappe.get_all(
        "hero right",  # Now the doctype exists
        fields=[ "title", "image", "description", "subtitle", "phone_image", "background_image", "button_label", "button_label1"
              ]  # You can add more fields here if needed
    )
    return get_product




@frappe.whitelist(allow_guest=True)
def get_products():
    get_product = frappe.get_all(
        "Item",  # Now the doctype exists
        fields=[ "item_name", "image", "description", "item_description", "item_code",  ]  # You can add more fields here if needed
    )
    return get_product




@frappe.whitelist(allow_guest=True)
def get_allproducts(page=1, limit=10):
    start = (page - 1) * limit
    get_product = frappe.get_all(
        "Item",
        fields=["item_name", "image", "description", "item_description"],
        limit=limit,  # Use 'limit' instead of 'limit_page_length'
        start=start
    )
    total_count = frappe.db.count("Item")
    return {
        "products": get_product,
        "total_count": total_count
    }


@frappe.whitelist(allow_guest=True)
def place_order(products):
    if not products:
        frappe.throw("Can't place order with no items")

    current_user = frappe.session.user
    

    new_order = frappe.new_doc("Quotation")
    new_order.customer = current_user
    
    # Iterate through the products and create items for the Quotation
    for product in products:
        # Check if the quantity is zero
        if product.get("qty", 0) == 0:
            frappe.throw("Item quantity cannot be zero")

        new_order.append("items", {
            "item_name": product.get("item_name"),  # Assuming 'item_name' is present in the product
            "qty": product.get("qty"),  # Add quantity to the item
            # Add other item properties as needed (e.g., price, etc.)
        })

    new_order.insert(ignore_permissions=True)
    return new_order