# FastAPI Backend

A modern FastAPI backend application with authentication, database integration, and Docker support.

## Features

- ✅ **FastAPI Framework**: High-performance async web framework
- ✅ **SQLAlchemy ORM**: Database operations with PostgreSQL
- ✅ **Pydantic Models**: Data validation and serialization
- ✅ **JWT Authentication**: Secure user authentication and authorization
- ✅ **Alembic Migrations**: Database schema version control
- ✅ **Docker Support**: Containerized deployment with Docker Compose
- ✅ **CRUD Operations**: Complete Create, Read, Update, Delete examples
- ✅ **Environment Configuration**: .env file support for configuration

## Project Structure

```
fastapi-backend/
├── app/
│   ├── core/
│   │   ├── config.py          # Application configuration
│   │   ├── security.py        # JWT and password hashing utilities
│   │   └── dependencies.py    # FastAPI dependencies
│   ├── models/
│   │   └── models.py          # SQLAlchemy models
│   ├── schemas/
│   │   ├── schemas.py         # Pydantic schemas
│   │   └── auth.py            # Authentication schemas
│   ├── crud/
│   │   └── crud.py            # CRUD operations
│   ├── routers/
│   │   ├── auth.py            # Authentication endpoints
│   │   ├── users.py           # User endpoints
│   │   └── items.py           # Item endpoints
│   ├── database.py            # Database connection
│   └── main.py                # FastAPI application
├── alembic/
│   ├── versions/              # Migration files
│   └── env.py                 # Alembic environment
├── alembic.ini                # Alembic configuration
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Docker image definition
├── requirements.txt           # Python dependencies
└── .env.example               # Environment variables template

```

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL (or use Docker)
- Docker and Docker Compose (optional)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/anzilmo/fastapi-backend.git
cd fastapi-backend
```

2. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Choose your setup method**

#### Option A: Docker (Recommended)

```bash
# Start the application with Docker Compose
docker-compose up -d

# Run migrations
docker-compose exec web alembic upgrade head
```

#### Option B: Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make sure PostgreSQL is running and update DATABASE_URL in .env

# Run migrations
alembic upgrade head

# Start the application
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token

### Users

- `GET /users/me` - Get current user information (Protected)
- `GET /users/{user_id}` - Get user by ID
- `GET /users/` - List all users
- `PUT /users/{user_id}` - Update user (Protected)
- `DELETE /users/{user_id}` - Delete user (Protected)

### Items

- `POST /items/` - Create a new item (Protected)
- `GET /items/{item_id}` - Get item by ID
- `GET /items/` - List all items
- `GET /items/user/me` - Get current user's items (Protected)
- `PUT /items/{item_id}` - Update item (Protected)
- `DELETE /items/{item_id}` - Delete item (Protected)

### Health Check

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint

## Usage Examples

### 1. Register a new user

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "SecurePassword123"
  }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=SecurePassword123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Create an item (authenticated)

```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "title": "My First Item",
    "description": "This is a test item"
  }'
```

### 4. Get current user information

```bash
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migration

```bash
alembic downgrade -1
```

## Environment Variables

Key environment variables in `.env`:

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Secret key for JWT token generation
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (default: 30)
- `APP_NAME`: Application name
- `APP_VERSION`: Application version
- `DEBUG`: Debug mode (True/False)

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Code Formatting

```bash
# Install formatting tools
pip install black isort

# Format code
black .
isort .
```

## Docker Commands

```bash
# Build and start containers
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Rebuild containers
docker-compose up -d --build

# Access the app container
docker-compose exec web bash

# Run migrations in container
docker-compose exec web alembic upgrade head
```

## Security Notes

⚠️ **Important for Production:**

1. Change the `SECRET_KEY` in `.env` to a strong, random value
2. Update CORS settings in `app/main.py` to allow only specific origins
3. Use environment variables for sensitive data
4. Enable HTTPS in production
5. Use strong passwords and consider password policies
6. Implement rate limiting for authentication endpoints

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Alembic**: Database migration tool
- **PostgreSQL**: Relational database
- **JWT**: JSON Web Tokens for authentication
- **Docker**: Containerization platform
- **Uvicorn**: ASGI server implementation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on GitHub.
