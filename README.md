# DevSearch Collaboration Platform

### Introduction

DevSearch is a collaboration platform designed for software developers to find partners for open-source or freelance projects. It enables networking, team formation, and direct collaboration on diverse development tasks.

The platform includes:

-   User Profiles for showcasing skills and interests.

-   Project Listings for open-source/freelance work.

-   Direct Messaging (Inbox) for seamless communication.

-   Team Management to organize and manage contributors.

The primary objective is to create a dedicated niche for developers to connect, collaborate, and build impactful projects together.

### Visual References

##### Login Page
![Login Page](https://github.com/user-attachments/assets/c94dad3b-3e2e-477f-958a-f0b5181d0de4)

##### Profile Page
![image](https://github.com/user-attachments/assets/103661ee-30ca-44e6-8ffe-8b0269b448c0)

##### Message Inbox Page
![image](https://github.com/user-attachments/assets/69e9afef-0f82-49d0-b1a8-340088a62989)

### Features

-   User Profiles: Developers can showcase their skills, experience, and interests.

-   Project Listings: Post projects with goals, requirements, and collaboration requests.

-   Search Functionality: Search developers or projects by tags, names, and skills.

-   Direct Messaging: Inbox for real-time communication.

-   Team Management: Manage collaborators and project teams.

-   REST API: Built with Django REST Framework for flexible integrations.

-   GraphQL API: Added with Graphene for fine-grained querying and mutations.

-   Background Tasks with Celery: Handle asynchronous tasks such as email notifications and scheduled jobs.

-   Containerization: Fully Dockerized with Compose for consistent local development and production deployments.

### 🛠 Tools & Technologies

-   Backend: Django (Python)

-   API Layer: Django REST Framework (RESTful APIs) + Graphene-Django (GraphQL support)

-   Frontend: HTML, CSS, JavaScript

-   Database: SQLite (development), MySQL (production)

-   Authentication: Django’s built-in auth + DRF JWT (via rest_framework_simplejwt)

-   Task Queue: Celery with Redis broker (for async background jobs like sending notifications)

-   Containerization: Docker & Docker Compose (for reproducible environments)

-   Testing: Postman (API testing & documentation)

-   Deployment: Hosted on [PythonAnywhere](https://freelancereddy.pythonanywhere.com/).

### Key Implementations

1.  GraphQL Integration

The project now includes GraphQL endpoints powered by Graphene-Django.

-   Benefits:

    -   Clients query only the data they need, reducing over-fetching.

    -   Supports both queries (fetch projects, profiles, tags, reviews) and mutations (voting on projects, adding reviews, etc.).

-   Example Query:

    ```         
      query {
          allProjects {
              id
              title
              tags {
              name
              }
          }
      }
    ```

-   Example Mutations:

    ```         
      mutation {
          voteProject(projectId: 1, value: "up") {
              project {
              title
              reviews {
                  value
              }
              }
          }
      }
    ```

Access Endpoint: /graphql/ with GraphiQL IDE enabled.

2.  Celery for Background Tasks

To improve scalability, Celery has been integrated with Redis as the message broker.

-   Use Cases in DevSearch:

    -   Sending async email notifications (e.g., when a collaborator joins a project).

    -   Handling scheduled jobs (e.g., cleanup tasks, reminders).

-   Benefits:

    -   Offloads time-consuming tasks from the main Django process.

    -   Keeps the user experience smooth by processing heavy jobs in the background.

-   Celery Setup:

    -   celery.py added in project root.

    -   Tasks can be defined in Django apps (tasks.py).

    -   Worker and Beat services run via Docker Compose.

3.  Docker & Docker Compose

The project is fully containerized for development and deployment.

-   Services Defined in docker-compose.yml:

    -   Web (Django app)

    -   Database (MySQL)

    -   Redis (broker for Celery)

    -   Celery Worker

    -   Celery Beat (scheduler)

-   Benefits:

-   Consistency across environments.

-   Easier onboarding: run with a single command.

-   Quick Start:

    docker-compose up --build

🔧 Installation (Manual Setup Without Docker) Prerequisites

-   Python 3.x

-   pip

-   Virtual environment (recommended)

Steps

```         
    # Clone repository
    git clone https://github.com/EdwinKingori/DevSearch.git
    cd DevSearch

    # Create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Apply migrations
    python3 manage.py migrate

    # Create superuser
    python3 manage.py createsuperuser

    # Run development server
    python3 manage.py runserver
```

# Contributions

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch:

```         
    git checkout -b feature/your-feature-name
```

Commit your changes:

```         
    git commit -m "Add your feature description"
```

Push to the branch:

```         
    git push origin feature/your-feature-name
```

Open a pull request.

# Contact

For any questions, critics, suggestions, or feedback, please contact:

Email: [devedwinkingori\@gmail.com](mailto:devedwinkingori@gmail.com){.email}

GitHub: <https://github.com/DevEddyKingori/Developers-Search>

# HAVE FUN :) !
