# import fastapi

# print(fastapi.__version__)

from fastapi import FastAPI,Request
from mockData import products
from dtos import ProductDTO
app = FastAPI()

@ app.get("/")
def home():
    return "Welcome home!";

# @app.get("/contact")
# def contact():
#     return "You can connect us on anytime";

@app.get("/products")
def get_products():
    return products


#Path params
# @app.get("/product/{product_id}")
# def get_one_product(product_id:int):
#     return {
#         "id": product_id
#     }

@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    #if product available with the id, return the product, else return the error
   
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return {
        "error": "Product not found for this id"
    }


#Query params
# @app.get("/greet")
# def greet_user(name:str, age:int):
#     return {
#      "greet":f"Hello {name}, Your age is {age}"
#     }


@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    # print(query_params)
    return {
     "greet":f"Hello {query_params.get('name')}, Your age is {query_params.get('age')}"
    }

#Methods of sending data: body, header --> request headers, query params 
#different types of http methods

# @app.post("/create_product")
# def create_product():
#     return {"Status": "Product created successfully"}


@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()    #model_dump() is used to convert the pydantic model to a dictionary
    # print(product_data)
    products.append(product_data)
    return {"Status": "Product created successfully", "data": products}




@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):

    for index,oneProduct in enumerate(products):
        # print(oneProduct, index)   
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "Product updated successfully", "product": product_data}


    return {"error": "Product not found for this id"}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
     for index,oneProduct in enumerate(products):
          if oneProduct.get("id") == product_id:
              deleted_product = products.pop(index)
              return {"Status": "Product deleted successfully", "product":{deleted_product}}

     return {"error": "Product not found for this id"}
#pydentic 

#POSTMAN


#how to call different http methods. -->Any TOOL?


#how to validate data. -DTOS




