from models import Admin
from flask import jsonify, request
from databaseconfig import db

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
        
        data = request.get_json()
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        user_name=data.get('user_name'),
        position=data.get('position'),
        phone_number=data.get('phone_number'),
        email=data.get('email')
        admin = Admin(first_name=first_name, last_name=last_name, user_name=user_name, position=position, phone_number=phone_number, email=email)
        db.session.add(admin)
        db.session.commit()
        inserted_admin = {
            'staff_id': admin.staff_id,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'user_name': admin.user_name,
            'position': admin.position,
            'phone_number': admin.phone_number,
            'email': admin.email
        }
        return jsonify(inserted_admin), 201
    
    elif request.method == 'DELETE':
        staff_id = request.args.get('staff_id')
        admin = Admin.query.filter_by(staff_id=staff_id).first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return f"Client with ID {staff_id} deleted"
        else:
            return f"Client with ID {staff_id} not found", 404
        

                