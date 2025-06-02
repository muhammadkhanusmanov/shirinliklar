# test_api.py

import requests

BASE_URL = 'http://localhost:8000/api/'  # Localhost test uchun
AUTH_ENDPOINT = BASE_URL + 'auth/'

# Admin login
def get_admin_token(username, password):
    response = requests.post(AUTH_ENDPOINT, data={
        'username': username,
        'password': password
    })
    token = response.json().get('token')
    return token

# 1. Foydalanuvchi: mahsulotlar ro‘yxatini olish
def test_product_list():
    response = requests.get(BASE_URL + 'products/')
    print("Mahsulotlar:", response.status_code)
    print(response.json())

# 2. Foydalanuvchi: buyurtma yaratish
def test_create_order():
    order_data = {
        "customer_name": "Ali Valiyev",
        "phone_number": "+998901112233",
        "product": 1,  # mavjud mahsulot ID
        "is_box": False
    }
    response = requests.post(BASE_URL + 'orders/', json=order_data)
    print("Buyurtma yaratildi:", response.status_code)
    print(response.json())

# 3. Admin: mahsulot qo‘shish
def test_admin_create_product(token):
    headers = {'Authorization': f'Token {token}'}
    product_data = {
        "name": "Shokoladli tort",
        "description": "Juda mazali va yangi",
        "price": 20000,
        "box_price": 100000,
        "has_box": True,
        "box_count": 6,
        "box_description": "Yaxshi qadoqlangan",
        "is_active": True
    }
    files = {
        'image': open('cake.jpg', 'rb')  # Lokal rasm fayli
    }
    response = requests.post(BASE_URL + 'admin/products/', data=product_data, files=files, headers=headers)
    print("Mahsulot qo‘shish:", response.status_code)
    print(response.json())

# 4. Admin: buyurtmalarni olish
def test_admin_get_orders(token):
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(BASE_URL + 'admin/orders/', headers=headers)
    print("Buyurtmalar ro‘yxati:", response.status_code)
    print(response.json())

# 5. Admin: buyurtma statusini yangilash
def test_admin_update_status(token, order_id):
    headers = {'Authorization': f'Token {token}'}
    data = {"status": "confirmed"}
    response = requests.patch(BASE_URL + f'admin/orders/{order_id}/status/', json=data, headers=headers)
    print("Status yangilandi:", response.status_code)
    print(response.json())

# 6. Admin: statistika
def test_statistics(token):
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(BASE_URL + 'admin/statistics/', headers=headers)
    print("Statistika:", response.status_code)
    print(response.json())


# ========== TEST QILISH ==========
if __name__ == '__main__':
    admin_token = get_admin_token('admin', '123')  # login: admin

    test_product_list()
    test_create_order()
    
    if admin_token:
        test_admin_create_product(admin_token)
        test_admin_get_orders(admin_token)
        test_admin_update_status(admin_token, order_id=1)  # mavjud ID bo‘lishi kerak
        test_statistics(admin_token)
    else:
        print("Admin login muvaffaqiyatsiz!")
