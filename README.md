# jumatechs-assignment
A simple event management system developed in Django

#### Requirements
- [x] Create events: Each event should have a title, description, date, time, and location.
- [x] List of events: There should be an event display page
- [x] Event details page
- [x] User registration, authentication
- [x] User can register to an event. Note, only signed up users can register, and users should only be able to unregister from events they've registered for.
- [x] Keyword-based search
- [x] Utilize Django Admin Panel
- [x] Create a user dashboard where they can see and manage their registered events.

#### Project Installation

##### Prerequisites
- Docker engine has to be installed

##### Installation (for local linux desktop)
1. clone the git repo
2. run `docker compose up --build -d` and the application will boot up with seed data

#### Technology used
1. Backend: Python, Django
2. Frontend: Jinja2 Template Engine along with HTML and Bootstrap4
3. Database: PostgreSQL
4. Server: AWS EC2 (t2.micro free tier eligible)
5. Containerization: Docker
6. Reverse proxy: Nginx
7. DNS: Cloudflare

#### Scope of improvements
- In user registration, we could use Google OAuth2
- Caching can be introduces for faster query
- Using Cloudinary/AWS S3 to store media files
- Scale and encrypt media files before storing