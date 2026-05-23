from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.models import Expense
from app.extensions import db

from sqlalchemy import extract
from datetime import datetime
expense_bp = Blueprint('expenses', __name__)
@expense_bp.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():

    user_id = get_jwt_identity()

    data = request.get_json()

    new_expense = Expense(
        title=data.get('title'),
        amount=data.get('amount'),
        category=data.get('category'),
        user_id=user_id
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify({
        "message": "Expense added"
    }), 201

@expense_bp.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():

    user_id = get_jwt_identity()

    expenses = Expense.query.filter_by(user_id=user_id).all()

    result = []

    for expense in expenses:
        result.append({
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "created_at": expense.created_at
        })

    return jsonify(result), 200

@expense_bp.route('/expenses/<int:id>', methods=['GET'])
@jwt_required()
def get_single_expense(id):

    user_id = get_jwt_identity()

    expense = Expense.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not expense:
        return jsonify({
            "message": "Expense not found"
        }), 404

    return jsonify({
        "id": expense.id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category
    }), 200

@expense_bp.route('/expenses/<int:id>', methods=['PUT'])
@jwt_required()
def update_expense(id):

    user_id = get_jwt_identity()

    expense = Expense.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not expense:
        return jsonify({
            "message": "Expense not found"
        }), 404

    data = request.get_json()

    expense.title = data.get('title')
    expense.amount = data.get('amount')
    expense.category = data.get('category')

    db.session.commit()

    return jsonify({
        "message": "Expense updated"
    }), 200

@expense_bp.route('/expenses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_expense(id):

    user_id = get_jwt_identity()

    expense = Expense.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not expense:
        return jsonify({
            "message": "Expense not found"
        }), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense deleted"
    }), 200

@expense_bp.route('/expenses/category/<string:category>', methods=['GET'])
@jwt_required()
def category_filter(category):

    user_id = get_jwt_identity()

    expenses = Expense.query.filter_by(
        category=category,
        user_id=user_id
    ).all()

    result = []

    for expense in expenses:
        result.append({
            "title": expense.title,
            "amount": expense.amount
        })

    return jsonify(result), 200

@expense_bp.route('/expenses/monthly-summary', methods=['GET'])
@jwt_required()
def monthly_summary():

    user_id = get_jwt_identity()

    current_month = datetime.utcnow().month

    expenses = Expense.query.filter(
        Expense.user_id == user_id,
        extract('month', Expense.created_at) == current_month
    ).all()

    total = 0

    for expense in expenses:
        total += expense.amount

    return jsonify({
        "month": current_month,
        "total_expense": total
    }), 200
