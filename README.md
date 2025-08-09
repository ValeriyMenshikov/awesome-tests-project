# Awesome Tests Project

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-8.4.1-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

Awesome Tests Project is a sample framework for integration testing of microservice architectures. The project demonstrates approaches to testing various technologies and protocols for service interactions.

The framework provides a unified approach to writing tests for different types of services and technologies, enabling the creation of reliable and maintainable tests.

## Supported Technologies

The project includes examples of testing the following technologies:

- **HTTP REST API** - testing RESTful services using Python clients
- **gRPC** - testing services that use the gRPC protocol (planned)
- **PostgreSQL** - testing interactions with PostgreSQL databases (planned)
- **Redis** - testing caching and queues in Redis (planned)
- **Kafka** - testing event-driven architecture with Apache Kafka (planned)

## Tech Stack

- **Python 3.11+** - primary development language
- **Poetry** - dependency and virtual environment management
- **Pytest** - framework for writing and running tests
- **Pydantic** - data validation and configuration management
- **Docker** - containerization of the test environment
- **Custom Code Generation Libraries** - the project utilizes custom-built code generation libraries developed by the author to streamline API client creation and test data generation

## Project Architecture

```
awesome-tests-project/
├── framework/                  # Core framework code
│   ├── config/                 # Configuration and settings
│   ├── fixtures/               # Fixtures for various services
│   │   ├── http/               # HTTP fixtures
│   │   ├── grpc/               # gRPC fixtures (planned)
│   │   ├── db/                 # Database fixtures (planned)
│   │   ├── redis/              # Redis fixtures (planned)
│   │   └── kafka/              # Kafka fixtures (planned)
│   ├── helpers/                # Helper functions and classes
│   └── internal/               # Internal framework components
├── tests/                      # Tests
│   ├── e2e/                    # End-to-end tests
│   ├── smoke/                  # Smoke tests
│   └── unit/                   # Unit tests
├── local.env                   # Local environment variables
├── pyproject.toml              # Poetry configuration and dependencies
└── README.md                   # Project documentation
```

## Running Tests

### Local Execution

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run tests:
   ```bash
   poetry run pytest
   ```

## Configuration

The project supports configuration through `.env` files and environment variables:

- For local development, `local.env` is used
- In CI/CD pipelines, environment variables are used

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Valeriy Menshikov** - [GitHub](https://github.com/ValeriyMenshikov)