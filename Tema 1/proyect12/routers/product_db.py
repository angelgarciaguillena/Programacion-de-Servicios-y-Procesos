from fastapi import APIRouter, HTTPException
from db.models.product import Product
from db.client import db_client
from db.schemas.product import product_schema, products_schema

from bson import ObjectId

router = APIRouter(prefix = "/productsdb", tags = ["productsdb"])

products_list = []


@router.get("/", response_model = list[Product])
async def products():
    return products_schema(db_client.test.products.find())


@router.get("/{id_product}", response_model = Product)
async def product(id_product: str):
    return search_product_id(id_product)


@router.post("/", response_model=Product, status_code=201)
async def add_product(product: Product):

    if type(search_product(product.name)) == Product:
        raise HTTPException(status_code=409, detail="Product already exists")
    
    product_dict = product.model_dump()
    del product_dict["id"]

    id = db_client.test.products.insert_one(product_dict).inserted_id

    product_dict["id"] = str(id)
    return Product(**product_dict)


@router.put("/{id_product}", response_model=Product)
async def modify_product(id_product: str, new_product: Product):

    product_dict = new_product.model_dump()

    del product_dict["id"]
    updated = db_client.test.products.find_one_and_replace({"_id": ObjectId(id_product)}, product_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return search_product_id(id_product)


@router.delete("/{id_product}", response_model=Product)
async def delete_product(id_product: str):

    found = db_client.test.products.find_one_and_delete({"_id": ObjectId(id_product)})

    if not found:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**product_schema(found))


def search_product_id(id: str):

    product_data = db_client.test.products.find_one({"_id": ObjectId(id)})

    if not product_data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product = product_schema(product_data)

    return Product(**product)


def search_product(name: str):
    try:
        product = product_schema(db_client.test.products.find_one({"name": name}))
        return Product(**product)
    except:
        return {"error": "Product not found"}
    
""""
def next_id():
    return (max(product.id for product in products_list)) + 1"""