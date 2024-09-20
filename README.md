# Social Network

A social media platform inspired by Instagram, where users can create profiles, follow others, post content, and interact with posts through likes and comments.

## Features

- **User Profiles:** Each user has a personal profile where they can share their posts and display their followers and followings.
- **Follow System:** Follow other users to see their posts in your feed.
- **Posting Content:** Users can create and share posts with text, images, or videos.
- **Likes & Comments:** Engage with posts by liking them or leaving comments.
- **Feed:** View posts from users you follow in your personalized feed.
- **Search:** Find users and explore new content easily.

## Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates (or your preferred front-end framework)
- **Database:** PostgreSQL (or any preferred database)

## Getting Started

### Prerequisites

- Python 3.10+
- Django 4.0+
- Virtualenv (optional but recommended)
- PostgreSQL (or any other preferred database)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/doostiyan/social_network_project
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your database settings and any other necessary configurations in `settings.py`.**

5. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Visit the site:**

    Open your browser and go to `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please contact us at support@example.com.
