# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using FastAPI by creating endpoints, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Set up a FastAPI app with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a root `GET /` endpoint
- Return JSON with a welcome message, such as `{"message": "Welcome to the FastAPI app"}`

### 🛠️ Add Item Endpoints

#### Description
Implement CRUD-like endpoints for managing a simple in-memory collection of items.

#### Requirements
Completed program should:

- Define a Pydantic model `Item` with `id`, `name`, `price`, and `in_stock` fields
- Add `GET /items/` to return all items
- Add `GET /items/{item_id}` to return a single item or raise a 404 error if not found
- Add `POST /items/` to create and return a new item
- Add `PUT /items/{item_id}` to update an existing item
- Add `DELETE /items/{item_id}` to remove an item

### 🛠️ Use Query Parameters and Validation

#### Description
Add query parameter support and validation to improve the API behavior.

#### Requirements
Completed program should:

- Add `GET /search/` accepting query parameters such as `q` and `max_price`
- Use Pydantic validation for request payloads and responses
- Return clear JSON error responses when invalid data is submitted
- Verify the API works using a tool like `uvicorn` and browser or API client requests
