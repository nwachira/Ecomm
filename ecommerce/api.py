import frappe

@frappe.whitelist(allow_guest=True)
def get_items():
    get_product = frappe.get_doc(
        "Website Settings",  # This is likely incorrect, you're trying to get a single Website Setting
        
    )
    return get_product



@frappe.whitelist(allow_guest=True)
def get_products():
    get_product = frappe.get_all(
        "Item",  # Now the doctype exists
        fields=[ "item_name", "image", "description", "item_description" ]  # You can add more fields here if needed
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

