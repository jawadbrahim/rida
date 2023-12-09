from flask import jsonify, request, json, Response
from project.model.Food import Food
from database.postgres import db
from .pydantic_models import FoodPydantic
from .messages import FAILED_TO_CREATE_FOOD, FOOD_NOT_FOUND,UPDATE_SUCCESSFULLY, CREATED_SUCCESSFULLY, DELETE_SUCCESSFULLY
from .decorators import validate_properties_existence



@validate_properties_existence
def create_foods():
    if request.method == "POST":
        try:
            data = request.json
            
            food_data_pydantic = FoodPydantic(**data)
            

            new_food = Food(
                category=food_data_pydantic.category,
                title=food_data_pydantic.title,
                description=food_data_pydantic.description,
                picture=food_data_pydantic.picture,
                ingredients=food_data_pydantic.ingredients,
            )

            

            db.session.add(new_food)
            db.session.commit()

            return jsonify(CREATED_SUCCESSFULLY)

        except Exception as e:
            return jsonify(FAILED_TO_CREATE_FOOD)

    return jsonify(CREATED_SUCCESSFULLY)
def get_foods_list():
    offset = request.args.get("offset", type=int, default=0)
    limit = request.args.get("limit", type=int, default=50)

   
    foods = db.session.query(Food).limit(limit).offset(offset).all()
    

    
    foods_data = []

    for food in foods:
        food_data = {
            "id": food.id,
            "category":food.category,
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients,
        }

        
        foods_data.append(food_data)

    response_data = {"foods": foods_data}
    response = json.dumps(response_data, ensure_ascii=False)

    return Response(response, content_type="application/json;")

def update_foods(food_id):
    data = request.json
    foods_category=data.get("category")
    foods_title = data["title"]
    foods_description = data.get("description")
    foods_picture = data.get("picture")
    foods_ingredients = data.get("ingredients")
    category_id = data.get("category_id")

    food = db.session.query(Food).get(food_id)

    if not food:
        return jsonify(FOOD_NOT_FOUND)

    
    food.category=foods_category
    food.title = foods_title
    food.description = foods_description
    food.picture = foods_picture
    food.ingredients = foods_ingredients

   

    db.session.commit()

    return jsonify(UPDATE_SUCCESSFULLY)


def get_foods_single(food_id):
    food = db.session.query(Food).get(food_id)

    if food:
        food_data = {
            "id": food.id,
            "category":food.category,
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients,
        }

        

        return jsonify(food_data)
    else:
        return jsonify(FOOD_NOT_FOUND)
def get_group_foods():
    foods = Food.query.all()
    grouped_foods = {}

    for food in foods:
        category = food.category
        if category not in grouped_foods:
            grouped_foods[category] = []

        food_data = {
            "description": food.description,
            "ingredients": food.ingredients,
            "picture": food.picture,
            "title": food.title
        }

        grouped_foods[category].append(food_data)

    response_data = {"foods": grouped_foods}
    response = json.dumps(response_data, ensure_ascii=False)

    return Response(response, content_type="application/json;")


def delete_foods(food_id):
    food = db.session.query(Food).get(food_id)
    if food:
        db.session.delete(food)
        db.session.commit()
        return jsonify(DELETE_SUCCESSFULLY)
    else:
        return jsonify(FOOD_NOT_FOUND)
