from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": 'apples', "price": 1.0, "quantity": 100},
    {"id": 2, "name": 'bananas', "price": 0.5, "quantity": 200},
    {"id": 3, "name": 'cherries', "price": 2.0, "quantity": 50},
    {"id": 4, "name": 'lemons', "price": 3.0, "quantity": 25},
    {"id": 5, "name": 'oranges', "price": 1.5, "quantity": 75},
    {"id": 6, "name": 'peaches', "price": 2.5, "quantity": 100},
    {"id": 7, "name": 'pears', "price": 1.25, "quantity": 125},
    {"id": 8, "name": 'plums', "price": 1.75, "quantity": 150},
    {"id": 9, "name": 'raspberries', "price": 4.0, "quantity": 50},
    {"id": 10, "name": 'strawberries', "price": 3.5, "quantity": 75},
]

@app.route("/products", methods=['GET'])
def get_products():
    return jsonify({
        "products": products
    })

@app.route('/products/<int:product_id>', methods= ["GET"])
def get_products_by_product_id(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    p = jsonify(product)
    if product:
        print(product.get("name"))
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404


@app.route('/products', methods=["POST"])
def edit_product():
    new_product_data = request.get_json()
    
    if not new_product_data:
        return jsonify({"message": "Invalid request data"}), 400
    
    for product in products:
        if new_product_data.get("id") == product.get("id"):
            if new_product_data.get("flag") == "remove":
                product["quantity"] += new_product_data.get("quantity")
                return jsonify({"message": "Product has been updated"}), 200
            elif new_product_data.get("flag") == "add":
                product["quantity"] -= new_product_data.get("quantity")
                return jsonify({"message": "Product has been updated"}), 200
            else:
                return jsonify({"message": "Product not found"}), 404

    new_product = {
        "id": len(products) + 1,
        "name": new_product_data.get("name"),
        "price": new_product_data.get("price"), 
        "quantity": new_product_data.get("quantity")
    }

    products.append(new_product)
    return jsonify({"message": "New product has been added", "product": new_product}), 201


if __name__ == '__main__':
    app.run(port=4000, debug=True)