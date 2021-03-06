from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()
    
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()

        return {'message': 'store not found!'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':"store with name '{}' already exists".format(name) }, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An error occured while creating store."},500

        return{"message":"Store is created!", "store": store.json()}, 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return{"message":"Store deleted!"}
                

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]},200
    



