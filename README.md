# FastAPI Social Media API

A full-featured REST API for a social media application built with FastAPI, PostgreSQL, and SQLModel. This API provides user authentication, post management, and voting functionality with comprehensive database migrations using Alembic.

## Features

- **User Management**: User registration, authentication, and profile management
- **Post Management**: Create, read, update, and delete posts with pagination and search
- **Voting System**: Like/dislike posts with vote counting
- **Authentication**: JWT-based authentication with OAuth2
- **Database Migrations**: Automated database schema management with Alembic
- **Containerization**: Docker and Docker Compose support for easy deployment
- **Testing**: Comprehensive test suite with pytest
- **Admin Interface**: PostgreSQL administration with pgAdmin

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLModel (built on SQLAlchemy)
- **Authentication**: JWT with passlib and bcrypt
- **Migrations**: Alembic
- **Testing**: pytest
- **Containerization**: Docker & Docker Compose
- **Database Admin**: pgAdmin

## Project Structure

```
API-Development-Project/
├── src/
│   ├── routers/
│   │   ├── auth.py          # Authentication routes
│   │   ├── post.py          # Post management routes
│   │   ├── user.py          # User management routes
│   │   └── vote.py          # Voting system routes
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection and session
│   ├── main.py             # FastAPI application entry point
│   ├── model.py            # SQLModel database models
│   ├── outh2.py            # OAuth2 authentication logic
│   ├── schemas.py          # Pydantic schemas for API
│   └── utils.py            # Utility functions
├── alembic/
│   └── versions/           # Database migration files
├── tests/
│   ├── conftest.py         # Test configuration
│   ├── test_post.py        # Post endpoint tests
│   ├── test_user.py        # User endpoint tests
│   └── test_vote.py        # Vote endpoint tests
├── docker-compose.yaml     # Multi-container setup
├── Dockerfile             # API container configuration
├── requirements.txt       # Python dependencies
└── alembic.ini           # Alembic configuration
```

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL (or use Docker)
- Docker & Docker Compose (optional, for containerized setup)

### Option 1: Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd API-Development-Project
   ```

2. **Start the services**
   ```bash
   docker-compose up -d
   ```

This will start:
- PostgreSQL database (port 5432)
- pgAdmin interface (http://localhost:8080)
- FastAPI application (http://localhost:8000)

### Option 2: Local Development Setup

1. **Clone and setup virtual environment**
   ```bash
   git clone <repository-url>
   cd API-Development-Project
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup PostgreSQL database**
   - Install PostgreSQL locally
   - Create a database for the project
   - Update database configuration in `src/config.py`

4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   cd src
   uvicorn main:app --reload
   ```

## API Documentation

Once the application is running, you can access:

- **Interactive API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc
- **pgAdmin Database Interface**: http://localhost:8080 (Docker setup only)
  - Email: admin@admin.com
  - Password: root

## API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration

### Users
- `POST /users/` - Create a new user
- `GET /users/{id}` - Get user by ID

### Posts
- `GET /posts/` - Get all posts (with pagination, search, and vote counts)
- `POST /posts/` - Create a new post
- `GET /posts/{id}` - Get a specific post
- `PUT /posts/{id}` - Update a post
- `DELETE /posts/{id}` - Delete a post

### Votes
- `POST /votes/` - Vote on a post (like/unlike)

## Database Models

### Users
- `id`: Primary key
- `email`: Unique user email
- `password`: Hashed password
- `created_at`: Timestamp of account creation

### Posts
- `id`: Primary key
- `title`: Post title
- `content`: Post content
- `published`: Publication status
- `created_at`: Timestamp of post creation
- `user_id`: Foreign key to Users table

### Votes
- `user_id`: Foreign key to Users table
- `post_id`: Foreign key to Posts table
- `direction`: Vote direction (like/unlike)

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src tests/
```

## Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Downgrade to previous migration:
```bash
alembic downgrade -1
```

## Environment Variables

Key environment variables (configure in Docker Compose or locally):

- `DATABASE_HOST`: Database host (default: localhost)
- `DATABASE_PORT`: Database port (default: 5432)
- `DATABASE_USERNAME`: Database username
- `DATABASE_PASSWORD`: Database password
- `DATABASE_NAME`: Database name
- `SECRET_KEY`: JWT secret key
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Use descriptive commit messages
- Create database migrations for schema changes

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email [your-email] or create an issue in the repository.