import time 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException, Depends, Query, Request
#CREATE FAST API APPLICATION
app=FastAPI()


# MIDDLEWARE: LOG REQUEST DETAILS AND EXECUTION TIME
@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    # Record the request start time
    start_time = time.perf_counter()

    # Print incoming request details
    print(f"Incoming request: {request.method} {request.url.path}")

    # Pass the request to the next stage of the application
    response = await call_next(request)

    # Calculate request-processing time
    duration = time.perf_counter() - start_time

    # Print outgoing response details
    print(f"Response status: {response.status_code}")
    print(f"Execution time: {duration * 1000:.2f} ms")

    # Return the response to the client
    return response


# DEPENDENCY: VALIDATE AND PROVIDE PAGINATION PARAMETERS
def pagination_params(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return {
        "page": page,
        "limit": limit
    }

class Product(BaseModel):
    name:str
    price:float

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    
class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None

class SingleProductResponse(BaseModel):
    product: ProductResponse
    
class ProductCreateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductUpdateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductPartialUpdateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductDeleteResponse(BaseModel):
    message: str
    product: ProductResponse
    
#TEMPORARY STORAGE FOR PRODUCTS
products=[
    {
        "id":1,
        "name":"Laptop",
        "price":50000
    },
    {
        "id":2,
        "name":"Mouse",
        "price":1000
    },
    {
        "id":3,
        "name":"KeyBoard",
        "price":2000
    }
]
#GET METHOD (RETRIEVE ALL PRODUCTS OR FILTER BY NAME )
@app.get(
    "/products",
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK)
#PAGINATION DEPENDENCY
def get_products(
    pagination: dict = Depends(pagination_params)
    ):
    # Get pagination values from the dependency
    page = pagination["page"]
    limit = pagination["limit"]

    # Calculate the starting and ending indexes
    start = (page - 1) * limit
    end = start + limit
    
    # Select products for the requested page
    paginated_products = products[start:end]

    return {
        "products": paginated_products
    }

#RETRIEVE ALL PRODUCTS OR FILTER BY NAME 
# def get_products(name: str | None = None):

#     # If the client supplies a name, filter the products
#     if name:
#         filtered_products = [
#             product
#             for product in products
#             if name.lower() in product["name"].lower()
#         ]

#         # Return only the matching products
#         return {
#             "products": filtered_products
#         }

#     # If name is omitted, return all products
#     return {
#         "products": products
#     }

# #POST METHOD(TO SEND DATA TO THE SERVER )
# @app.post("/products",status_code=status.HTTP_201_CREATED)
# def create_product(product: Product):
#     new_product={
#         "id":len(products)+1,
#         "name": product.name,
#         "price": product.price
#     }
#     products.append(new_product)
#     return {
#         "message": "Product created successfully",
#         "product": new_product
#     }

#RETRIEVE AND FILTER PRODUCTS WITH PRICE RANGE 
# def get_products(
#     name: str | None = None,
#     min_price: float | None = None,
#     max_price: float | None = None
# ):
#     # Start with all products
#     filtered_products = products

#     # Filter products by name if supplied
#     if name:
#         filtered_products = [
#             product
#             for product in filtered_products
#             if name.lower() in product["name"].lower()
#         ]

#     # Filter products by minimum price if supplied
#     if min_price is not None:
#         filtered_products = [
#             product
#             for product in filtered_products
#             if product["price"] >= min_price
#         ]

#     # Filter products by maximum price if supplied
#     if max_price is not None:
#         filtered_products = [
#             product
#             for product in filtered_products
#             if product["price"] <= max_price
#         ]

#     # Return the matching products
#     return {
#         "products": filtered_products
#     }


#RETRIEVE SORTED PRODUCTS IN ORDER  
# def get_products(
#     sort_by: str | None = None,
#     order: str | None = None
# ):
#     # Validate the sorting field
#     if sort_by is not None:
#         sort_by = sort_by.lower()

#         if sort_by != "price":
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Unsupported sort_by. Use 'price'."
#             )

#         # Default to ascending order if order is omitted
#         sort_order = order.lower() if order else "asc"

#         # Validate the sorting direction
#         if sort_order not in ["asc", "desc"]:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Invalid order. Use 'asc' or 'desc'."
#             )

#         # Sort products by price
#         sorted_products = sorted(
#             products,
#             key=lambda product: product["price"],
#             reverse=(sort_order == "desc")
#         )

#         return {"products": sorted_products}

#     # Reject order if sort_by was not supplied
#     if order is not None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Provide sort_by=price when using order."
#         )

#     # If no sorting parameters are supplied, return products as stored
#     return {"products": products}

#RETRIEVE PRODUCTS USING PAGINATION 

# def get_products(
#     page: int = 1,
#     limit: int = 10
# ):
#     # Validate the page number
#     if page < 1:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Page must be at least 1."
#         )

#     # Validate the number of products per page
#     if limit < 1:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Limit must be at least 1."
#         )

#     # Calculate the starting index
#     start = (page - 1) * limit

#     # Calculate the ending index
#     end = start + limit

#     # Select products for the requested page
#     paginated_products = products[start:end]

#     # Return the selected products
#     return {
#         "products": paginated_products
#     }


    
#GET METHOD (TO SEND DATA OF SELECTED SPECIFIC PRODUCT)
@app.get(
    "/products/{product_id}",
    response_model=SingleProductResponse,
    status_code=status.HTTP_200_OK)
def get_product(product_id:int):
    for product in products:
        if product["id"]==product_id:
            return {
                "product":product
            }
    #PRODUCT WAS NOT FOUND 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )
            
#PUT METHOD (TO UPDATE DATA OF SELECTED ONE'S)
@app.put("/products/{product_id}",response_model=ProductUpdateResponse,status_code=status.HTTP_200_OK)
def update_product(product_id:int,product:Product):
    for item in products:
        if item["id"]==product_id:
            item["name"]=product.name
            item["price"]=product.price
            return {
                "message":"Product updated successfully",
                "product":item
            }
    #PRODUCT WAS NOT FOUND 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# PATCH METHOD (TO PARTIALLY UPDATE A PRODUCT)
@app.patch("/products/{product_id}", response_model=ProductPartialUpdateResponse,status_code=status.HTTP_200_OK)
def update_product_partially(
    product_id: int,
    product: ProductUpdate
):
    for item in products:

        # Find the product
        if item["id"] == product_id:

            # Update name only if it was provided
            if product.name is not None:
                item["name"] = product.name

            # Update price only if it was provided
            if product.price is not None:
                item["price"] = product.price

            return {
                "message": "Product partially updated successfully",
                "product": item
            }

    # Product not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )
    
      
#DELETE METHOD (TO DELETE DATA OF SELECTED ONES'S)
@app.delete("/products/{product_id}", response_model=ProductDeleteResponse,status_code=status.HTTP_200_OK)
def delete_product(product_id:int):
    for item in products:
        if item["id"]==product_id:
            products.remove(item)
            return {
                "message":"Product deleted successfully",
                "product":item
            }
    #PRODUCT NOT FOUND
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )