from init import db
from flask import Blueprint, request
from models.user import User
from models.collection import Collection, collection_schema, collections_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

collections_bp = Blueprint('collections', __name__, url_prefix='/collections')

@collections_bp.route('/')
def get_all_collections():
    '''/collections GET route displays all collections to the user'''
    stmt = db.select(Collection).order_by(Collection.id.desc()) # selects all collections from the database and sorts them in descending order
    collections = db.session.scalars(stmt) 
    return collections_schema.dump(collections) # returns collections to the user

@collections_bp.route('/<int:id>')
def get_one_controller(id):
    '''/collections/id GET route displays collection to user based on the requested ID'''
    stmt = db.select(Collection).filter_by(id=id) # filters the collections database based on the requested ID
    collection = db.session.scalar(stmt)
    if collection:
        return collection_schema.dump(collection) # if a collection with that ID is available, return to user
    else:
        return {'error': f'A collection with the id {id} does not exist.'}, 404 # if a collection with that ID is not available, return this error message
    
@collections_bp.route('/', methods=['POST'])
@jwt_required()
def create_collection():
    '''/collections POST route that will receive raw JSON with fields {name} before being validated and added to the database'''
    json_data = collection_schema.load(request.get_json()) # load the collection schema to get fields
    collection = Collection( # create new instance of collection
        name=json_data.get('name'),
        user_id=get_jwt_identity()
    )
    db.session.add(collection) # add new collection to session
    db.session.commit() # add new collection to the database
    return collection_schema.dump(collection), 201 # return the new collection to the user

@collections_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_collection(id):
    '''/collections/id DELETE route that will use the ID in the URL to locate the collection, verify the user as admin and then remove the collection from the database'''
    admin_status = authorise_admin() # function to authorise user as admin
    if not admin_status:
        return {'error': 'You must have admin permissions to delete collections.'} # if not admin return this error message
    stmt = db.select(Collection).filter_by(id=id) # filter collections by ID to find the requested collection
    collection = db.session.scalar(stmt)
    if collection:
        db.session.delete(collection)
        db.session.commit()
        return {'message': f'Collection {collection.id} has been deleted succesfully.'} # if collection is found, return this message
    else:
        return {'error': f'A collection with the id {id} does not exist.'}, 404 # if collection is not found, return this error message
    
@collections_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_collection(id):
    '''/collections/id PUT/PATCH route that will use the ID in the URL in order to find the collection, verify the user as the owner of the collection, and then allow the user to update details of the collection'''
    json_data = collection_schema.load(request.get_json(), partial=True)
    stmt = db.select(Collection).filter_by(id=id)
    collection = db.session.scalar(stmt)
    if collection:
        if str(collection.user_id) != get_jwt_identity():
            return {'error': 'You must be the owner of the collection in order to edit it.'}, 403 # if collection is found and user ID does not match the jwt, return this error message
        collection.name = json_data.get('name') or collection.name
        return collection_schema.dump(collection) # return edited collection to user
    else:
        return {'error': f'A collection with the id {id} does not exist.'}, 404 # if collection is not found return this error message
