from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix = "/products", tags = ["products"])

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    idClient: int

product_list = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=1200.00, idClient=1),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=800.00, idClient=2),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=200.00, idClient=3),
    Product(id=4, name="Monitor", description="4K UHD monitor", price=400.00, idClient=4),
    Product(id=5, name="Keyboard", description="Mechanical keyboard", price=150.00, idClient=5),
]

def next_id():
    return max(product_list, key= id).id + 1


def search_product(id: int):
    return [product for product in product_list if product.id == id]


@router.get("/")
def get_products():
    return product_list


@router.get("/{id_product}")
def get_product_by_id(id_product: int):

    products = search_product(id_product)

    if len(products) != 0:
        return products[0]

    else:
        raise HTTPException(status_code=404, detail="Product not found")
    

@router.post("/", status_code=201)
def add_product(product: Product):

    product.id = next_id()

    product_list.append(product)

    return product


@router.put("/{id_product}", response_model = Product)
def modify_product(id_product: int, product: Product):
    
    for index, saved_product in enumerate(product_list):
        
        if saved_product.id == id.product:
            
            product.id = id_product

            product_list[index] = product

            return product
        
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{id_product}")
def delete_product(id_product: int):

    for saved_product in product_list:

        if saved_product.id == id_product:

            product_list.remove(saved_product)

            return {}
        
    raise HTTPException(status_code=404, detail="Product not found")