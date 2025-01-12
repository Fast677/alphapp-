# API Documentation

## Endpoints

### GET /api/v1/resource
- **Description**: Retrieves a list of resources.
- **Parameters**: 
  - `page` (optional): Page number for pagination.
  - `limit` (optional): Number of items per page.
- **Response**:
  - `200 OK`: Returns a JSON array of resources.
  - `400 Bad Request`: Invalid parameters.

### POST /api/v1/resource
- **Description**: Creates a new resource.
- **Parameters**: 
  - `name` (required): Name of the resource.
  - `description` (optional): Description of the resource.
- **Response**:
  - `201 Created`: Returns the created resource.
  - `400 Bad Request`: Invalid parameters.

### PUT /api/v1/resource/{id}
- **Description**: Updates an existing resource.
- **Parameters**: 
  - `id` (required): ID of the resource to update.
  - `name` (optional): New name of the resource.
  - `description` (optional): New description of the resource.
- **Response**:
  - `200 OK`: Returns the updated resource.
  - `404 Not Found`: Resource not found.

### DELETE /api/v1/resource/{id}
- **Description**: Deletes an existing resource.
- **Parameters**: 
  - `id` (required): ID of the resource to delete.
- **Response**:
  - `204 No Content`: Resource successfully deleted.
  - `404 Not Found`: Resource not found.
