from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()




class Product(BaseModel):
  id: int
  name: str
  origin: str


products: List[Product] = []


@app.get('/')
def read_root():
  return {"message": "API running"}



@app.get('/products')
def get_products():
  return products



@app.post('/products')
def add_product(new_product: Product):
  products.append(new_product)
  return new_product


@app.put('/products/{product_id}')
def update_product(product_id:int, updated_product: Product):
  for idx,product in enumerate(products):
    if product.id == product_id:
      products[idx] = updated_product
      return updated_product

  return {"error":"no such product"}


@app.delete('/products/{product_id}')
def delete_product(product_id: int):
  for idx,product in enumerate(products):
    if products.id == product_id:
      deleted_product = products.pop(idx)
      return f"deleted {deleted_product}"

  return {"error":"no such product"}