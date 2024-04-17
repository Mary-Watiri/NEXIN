from models import Admin
from flask import jsonify, request

def admin():
    if request.method == 'GET':
        admin = Admin.query.all()
        admin_list = []
        for admin in admin:
            admin_list.append({
                'staff_id': admin.staff_id,
                'first_name': admin.first_name,
                'last_name': admin.last_name,
                'user_name': admin.user_name,
                'position': admin.position,
                'phone_number': admin.phone_number,
                'email': admin.email
            })
        return jsonify(admin_list)
    elif request.method == 'POST':
        return 'Post request received'
            