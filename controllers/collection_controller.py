from init import db, bcrypt
from flask import Blueprint, request
from models.user import User
from models.collection import Collection, collection_schema, collections_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

collections_bp = Blueprint('collections', __name__, url_prefix='/collections')

@collections_bp.route('/')
def get_all_collections():
    stmt = db.select(Collection).order_by(Collection.id.desc())
    collections = db.session.scalars(stmt)
    return collections_schema.dump(collections)

@collections_bp.route('/<int:id>')
def get_one_controller(id):
    stmt = db.select(Collection).filter_by(id=id)
    collection = db.session.scalar(stmt)
    if collection:
        return collection_schema.dump(collection)
    else:
        return {'error': f'A collection with the id {id} does not exist.'}, 404
    
@collections_bp.route('/', methods=['POST'])
@jwt_required()
def create_collection():
    json_data = collection_schema.load(request.get_json)
    collection = Collection(
        name=json_data.get('name'),
        user=get_jwt_identity()
    )
    db.session.add(collection)
    db.session.commit()
    return collection_schema.dump(collection), 201

@collections_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_collection(id):
    admin_status = authorise_admin
    if not admin_status:
        return {'error': 'You must have admin permissions to delete collections.'}
    stmt = db.select(Collection).filter_by(id)
    collection = db.session.scalar(stmt)
    if collection:
        return {'error': f'Collection {collection.id} has been deleted succesfully.'}
    else:
        return {'error': f'A collection with the id {id} does not exist.'}, 404