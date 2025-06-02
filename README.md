# Shirinliklar API Documentation

## Endpoints

### 1. Admin Endpoints

#### 1.1. List and Create Products
- **Endpoint:** `/api/admin/products/`
- **Method:** `GET`, `POST`
  
**GET Request:**
- **Description:** Retrieve a list of all products.
- **Response:**
  - **200 OK**
    - **Content:** List of products with details.

**POST Request:**
- **Description:** Create a new product.
- **Request Body:**
  ```json
  {
    "name": "string",
    "image": "string",
    "description": "string",
    "price": "decimal",
    "box_price": "decimal (optional)",
    "has_box": "boolean",
    "box_count": "integer",
    "box_description": "string (optional)"
  }
  ```
- **Response:**
  - **201 Created**
    - **Content:** Details of the created product.

#### 1.2. Retrieve, Update, and Delete a Product
- **Endpoint:** `/api/admin/products/<int:pk>/`
- **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

**GET Request:**
- **Description:** Retrieve a product by ID.
- **Response:**
  - **200 OK**
    - **Content:** Product details.

**PUT Request:**
- **Description:** Update a product completely.
- **Request Body:** Same as POST request.
- **Response:**
  - **200 OK**
    - **Content:** Updated product details.

**PATCH Request:**
- **Description:** Update specific fields of a product.
- **Request Body:** Fields to update.
- **Response:**
  - **200 OK**
    - **Content:** Updated product details.

**DELETE Request:**
- **Description:** Delete a product by ID.
- **Response:**
  - **204 No Content**

#### 1.3. List Orders
- **Endpoint:** `/api/admin/orders/`
- **Method:** `GET`
  
**GET Request:**
- **Description:** Retrieve a list of all orders.
- **Response:**
  - **200 OK**
    - **Content:** List of orders with details.

#### 1.4. Update Order Status
- **Endpoint:** `/api/admin/orders/<int:pk>/status/`
- **Method:** `PATCH`

**PATCH Request:**
- **Description:** Update the status of an order.
- **Request Body:**
  ```json
  {
    "status": "string"  // e.g., "new", "confirmed", "done", "archived"
  }
  ```
- **Response:**
  - **200 OK**
    - **Content:** Updated order details.

#### 1.5. Search Orders
- **Endpoint:** `/api/admin/orders/search/`
- **Method:** `GET`

**GET Request:**
- **Description:** Search for orders by customer name, phone number, or order code.
- **Query Parameters:**
  - `query`: Search term.
- **Response:**
  - **200 OK**
    - **Content:** List of matching orders.

#### 1.6. Statistics
- **Endpoint:** `/api/admin/statistics/`
- **Method:** `GET`

**GET Request:**
- **Description:** Retrieve statistics about orders.
- **Response:**
  - **200 OK**
    - **Content:** Statistics including total income, total orders, and orders by status.

### 2. User Endpoints

#### 2.1. List Products
- **Endpoint:** `/api/products/`
- **Method:** `GET`

**GET Request:**
- **Description:** Retrieve a list of active products.
- **Response:**
  - **200 OK**
    - **Content:** List of active products with details.

#### 2.2. Create Order
- **Endpoint:** `/api/orders/`
- **Method:** `POST`

**POST Request:**
- **Description:** Create a new order.
- **Request Body:**
  ```json
  {
    "customer_name": "string",
    "phone_number": "string",
    "product": "integer (product ID)",
    "is_box": "boolean"
  }
  ```
- **Response:**
  - **201 Created**
    - **Content:** Details of the created order.