Job-Matching Platform (Prototype)

🚀 Overview

This is a prototype job-matching platform that helps job seekers and employers connect using swipe-based interactions and video resumes. The platform is designed for early feedback and investor interest.

✨ Key Features

1. User Onboarding (Signup/Login)

Email & password signup (or OAuth with Google/LinkedIn).

Basic profile setup for job seekers and employers.

2. Profile Creation

🔹 Job Seekers

Create a basic profile (name, job title, skills, experience).

Upload or record a 15-45 second video resume.

🔹 Employers

Create a company profile (company name, industry, brief description).

Post job openings with basic details (job title, role description).

3. Swipe-Based Matching

Job seekers swipe through job postings.

Employers swipe through video resumes.

Swipe right = Interested / Swipe left = Pass.

Basic match notifications (if both swipe right).

4. In-App Messaging (Basic)

If a match occurs, allow text-based chat.

Simple message notifications.

5. Basic AI Job Matching (Optional)

Simple job recommendations based on skills, experience, and employer preferences.

Not advanced yet—just a rule-based or lightweight AI suggestion system.

6. Video Processing

Users can record, upload, and view short video resumes.

Basic compression & storage (e.g., using AWS S3 or Firebase).

7. Employer Dashboard

List of shortlisted candidates.

Basic job post management.

8. Simple Analytics

Track profile views & swipes (basic engagement stats).

9. Admin Panel (Basic Moderation)

Ability to remove inappropriate content.

User reports for spam or misuse.

❌ What’s NOT Included in the Bare-Bones Version?

🚫 Advanced AI Interview Analysis🚫 Full Profile Customization🚫 Video Editing/Enhancements🚫 Detailed Analytics for Employers🚫 Monetization Features (Ads, Subscriptions, etc.)

🎯 Goal of This Prototype

Get early feedback from job seekers & employers.

Showcase to investors and venture capitals.

🛠 Tech Stack

Backend: Django + Django REST Framework (DRF)

Database: PostgreSQL (AWS RDS)

Storage: AWS S3 or Firebase (for videos)

Authentication: Django Auth (with OAuth for Google/LinkedIn)

Frontend: React or Next.js (future integration)

📂 Project Setup

1️⃣ Clone the Repository

$ git clone https://github.com/your-repo/job-matching-platform.git
$ cd job-matching-platform

2️⃣ Create a Virtual Environment & Install Dependencies

$ python3 -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt

3️⃣ Run Migrations

$ python manage.py makemigrations
$ python manage.py migrate

4️⃣ Start the Development Server

$ python manage.py runserver

🔑 Environment Variables (.env)



🛠 API Endpoints (Example)

Endpoint

Method

Description

/api/auth/signup/

POST

User registration

/api/auth/login/

POST

User login

/api/profile/

GET

Get user profile

/api/jobpostings/

POST

Create a job posting (Employer)

/api/jobpostings/my_jobs/

GET

Get employer's job posts

/api/matches/

GET

Get matched candidates/jobs

