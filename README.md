<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh2Z29nbG5xZG4zd282ZXlmYW5kaTN3cXIwZ292cWdlNGV4eXh4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Pcvj0fxvnO4I0khDQX/giphy.gif" width="60" />
</p>

<h1 align="center">
  <span style="font-size: 4em; font-weight: 800; background: linear-gradient(135deg, #F58220 0%, #2D4635 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    SMART RECIPE
  </span>
</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Playfair+Display&weight=700&size=28&duration=3000&pause=1000&color=F58220&center=true&vCenter=true&random=false&width=600&lines=Your+AI-Powered+Kitchen+Assistant;4,300%2B+Recipes+at+Your+Fingertips;Cook+Smarter%2C+Not+Harder!" alt="Typing SVG" />
</p>


![Project: Recipe220](https://img.shields.io/badge/Project-Recipe220-blue?style=for-the-badge)
![Site: Smart Recipe](https://img.shields.io/badge/Site-Smart%20Recipe-orange?style=for-the-badge)
![Recipes: 5k+](https://img.shields.io/badge/Recipes-5k%2B-brightgreen?style=for-the-badge)
![Generator: AI + Heuristics](https://img.shields.io/badge/Generator-AI%20%2B%20Heuristics-yellow?style=for-the-badge)

Welcome to **Smart Recipe** — the delightful web experience powered by the Recipe220 project. Smart Recipe helps you discover, create, and cook amazing meals: browse our 5,000+ recipe database, or generate new recipes instantly from the ingredients you already have. Ready to turn leftovers into magic? Let's cook!

---

## Table of Contents
- [About](#about)
- [Functionality](#functionality)
- [Admin Panel](#admin-panel)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Install & Run](#install--run)
- [Usage Examples](#usage-examples)
- [Database & Content](#database--content)
- [Contributing](#contributing)
- [License](#license)
- [Developers](#developers)

---

## About
Smart Recipe is a modern, friendly site built from the Recipe220 project. Its core idea: combine a large curated recipe collection (5,000+ recipes) with an intelligent generator that crafts recipe suggestions based on the exact ingredients you have on hand. Whether you want a tried-and-true classic or a brand-new creation, Smart Recipe helps you move from pantry to plate.

Project repository: [Recipe220](https://github.com/AndriyPy/Recipe220)

---

## Functionality

### **User Management**
- Registration with email verification (6-digit code)
- Login with Cloudflare Turnstile (bot protection)
- Google SSO authentication
- Profile editing (gender, birth date, country)

### **Recipes**
- **Database**: 5,000+ recipes
- **Search**: 
  - Fuzzy search (typo-tolerant)
  - Search by name and ingredients
- **Sorting (SOON)**:  
  - By name (A-Z, Z-A)
  - By rating
  - By cooking time
  - By servings
- **Recipe details (soon)** page with:
  - Ingredients list
  - Step-by-step instructions
  - Preparation time
  - Rating

### **AI Assistant**
- Generate recipes based on available ingredients
- Personalized recommendations
- OpenRouter AI integration

### **Monitoring Stack**
- **Grafana** — metrics visualization
- **Prometheus** — metrics collection
- **Loki** — log aggregation
- **cAdvisor** — container monitoring
- **Promtail** — log collection agent

---

## Admin Panel

Smart Recipe features a clean and functional Django admin interface for efficient content management.

### **User Management**
- View complete user profiles with registration dates
- Filter users by gender, country, or account status
- Activate or deactivate user accounts
- Quick search by username or email

### **Email Verification**
- Track verification codes with status indicators (Active, Used, Expired)
- Monitor code creation and expiration timestamps
- Bulk delete expired verification records

### **AI Generated Recipes**
The admin panel provides a streamlined view of all AI-generated recipes:

- **Recipe List View**: Displays recipe ID, title, author, and creation date
- **Chronological Order**: Newest recipes appear first by default
- **Date Filtering**: Filter recipes by creation date
- **Search Functionality**: Find recipes by title, ingredients, or author username
- **Clean Interface**: Focuses on essential information without technical clutter

Access the admin panel at: `https://yoursite.com/admin/`

---

## Key Features

✅ **AI Recipe Generation** - Create unique recipes from any ingredients  
✅ **5,000+ Recipe Database** - Extensive collection of curated recipes  
✅ **Smart Search** - Find recipes even with typos  
✅ **User Authentication** - Email verification + Google SSO  
✅ **Cloudflare Protection** - Bot protection on login  
✅ **Custom Admin Panel** - Complete control over users and content  
✅ **Docker Support** - Easy deployment with containers  
✅ **Full Monitoring Stack** - Grafana, Prometheus, Loki integration  

---

## How It Works

1. **User enters ingredients** in the AI generator
2. **OpenRouter AI** processes the request with Gemini 2.0
3. **Recipe is generated** following strict formatting rules
4. **Authenticated users** can save recipes to their profile
5. **Saved recipes** appear in "My Recipes" section
6. **Admin can manage** all generated content through the panel

---

## Tech Stack

- **Backend**: Django 5.2
- **Database**: PostgreSQL (production) / SQLite (development)
- **AI Integration**: OpenRouter API (Gemini 2.0)
- **Authentication**: Django Auth + Google SSO
- **Frontend**: HTML, CSS, JavaScript
- **Security**: Cloudflare Turnstile
- **Monitoring**: Grafana, Prometheus, Loki
- **Deployment**: Docker, Nginx

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- Git

### Install & Run

```bash
# Clone the repository
git clone https://github.com/AndriyPy/Recipe220.git
cd Recipe220

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
