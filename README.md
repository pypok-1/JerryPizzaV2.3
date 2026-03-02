## 🌟 Welcome to **Smart Recipe**!

> *"The delightful web experience powered by the Recipe220 project"*

Smart Recipe helps you **discover**, **create**, and **cook** amazing meals: browse our **5,000+ recipe database**, or generate new recipes instantly from the ingredients you already have. 

<p align="center">
  <img src="https://img.shields.io/badge/Ready%20to%20turn%20leftovers%20into%20magic%3F-Let's%20cook!-F58220?style=for-the-badge" />
</p>

---

<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

## 📋 Table of Contents

<p align="center">
  <a href="#about"><img src="https://img.shields.io/badge/About-2D4635?style=for-the-badge&logo=readthedocs&logoColor=white" /></a>
  <a href="#functionality"><img src="https://img.shields.io/badge/Functionality-2D4635?style=for-the-badge&logo=codeigniter&logoColor=white" /></a>
  <a href="#key-features"><img src="https://img.shields.io/badge/Key_Features-2D4635?style=for-the-badge&logo=starship&logoColor=white" /></a>
  <a href="#how-it-works"><img src="https://img.shields.io/badge/How_It_Works-2D4635?style=for-the-badge&logo=react&logoColor=white" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech_Stack-2D4635?style=for-the-badge&logo=stackshare&logoColor=white" /></a>
  <a href="#getting-started"><img src="https://img.shields.io/badge/Getting_Started-2D4635?style=for-the-badge&logo=roadmap&logoColor=white" /></a>
  <a href="#developers"><img src="https://img.shields.io/badge/Developers-2D4635?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

## 📖 About

Smart Recipe is a modern, friendly site built from the [Recipe220](https://github.com/AndriyPy/Recipe220) project. Its core idea: **combine a large curated recipe collection (5,000+ recipes) with an intelligent generator** that crafts recipe suggestions based on the exact ingredients you have on hand. 

Whether you want a tried-and-true classic or a brand-new creation, Smart Recipe helps you move from **pantry to plate** effortlessly.

---

## 🎯 Functionality

### 👥 **User Management**
<table>
  <tr>
    <td>✅ Registration with email verification</td>
    <td><img src="https://img.shields.io/badge/6--digit%20code-✓-success?style=flat-square" /></td>
  </tr>
  <tr>
    <td>✅ Cloudflare Turnstile bot protection</td>
    <td><img src="https://img.shields.io/badge/Bot%20Protection-✓-success?style=flat-square" /></td>
  </tr>
  <tr>
    <td>✅ Google SSO authentication</td>
    <td><img src="https://img.shields.io/badge/Google%20SSO-✓-success?style=flat-square" /></td>
  </tr>
  <tr>
    <td>✅ Profile editing (gender, birth date, country)</td>
    <td><img src="https://img.shields.io/badge/Profile%20Customization-✓-success?style=flat-square" /></td>
  </tr>
</table>

### 📚 **Recipes**
| Feature | Status | Badge |
|---------|--------|-------|
| Database of 5,000+ recipes | ✅ Ready | ![5000+](https://img.shields.io/badge/5k%2B-recipes-brightgreen) |
| Fuzzy search (typo-tolerant) | ✅ Ready | ![Fuzzy](https://img.shields.io/badge/Fuzzy%20Search-✓-success) |
| Search by name & ingredients | ✅ Ready | ![Search](https://img.shields.io/badge/Search-✓-success) |
| Sorting (name, rating, time, servings) | 🔜 Soon | ![Soon](https://img.shields.io/badge/Sorting-Soon-orange) |
| Recipe details page | 🔜 Soon | ![Soon](https://img.shields.io/badge/Details-Soon-orange) |

### 🤖 **AI Assistant**
- ✨ Generate recipes based on available ingredients
- ✨ Personalized recommendations
- ✨ OpenRouter AI integration

### 📊 **Monitoring Stack**
<p align="center">
  <img src="https://img.shields.io/badge/Grafana-✓-F46800?style=for-the-badge&logo=grafana" />
  <img src="https://img.shields.io/badge/Prometheus-✓-E6522C?style=for-the-badge&logo=prometheus" />
  <img src="https://img.shields.io/badge/Loki-✓-FFA500?style=for-the-badge&logo=grafana" />
  <img src="https://img.shields.io/badge/cAdvisor-✓-00ADD8?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Promtail-✓-FFA500?style=for-the-badge&logo=grafana" />
</p>
## Table of Contents
- [About](#about)
- [Functionality](#functionality)
- [KeyFeatures](#key-features)
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

## ✨ Key Features

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/search--v1.png" width="60"/><br/>
        <b>Smart Search</b><br/>
        <sub>Fuzzy search finds recipes even with typos</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" width="60"/><br/>
        <b>AI Generator</b><br/>
        <sub>Create recipes from your ingredients</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/google-logo.png" width="60"/><br/>
        <b>Google SSO</b><br/>
        <sub>One-click login</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/dashboard.png" width="60"/><br/>
        <b>Full Monitoring</b><br/>
        <sub>Grafana + Prometheus stack</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/docker.png" width="60"/><br/>
        <b>Docker Ready</b><br/>
        <sub>Easy deployment with containers</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/cloudflare.png" width="60"/><br/>
        <b>Bot Protection</b><br/>
        <sub>Cloudflare Turnstile</sub>
      </td>
    </tr>
  </table>
</div>

---

## 🔄 How It Works

```mermaid
graph LR
    A[You] --> B[Enter Ingredients]
    B --> C{Choose Path}
    C --> D[Search Database]
    C --> E[AI Generation]
    D --> F[5,000+ Recipes]
    E --> G[Custom Recipe]
    F --> H[Cook & Enjoy!]
    G --> H
```

---

## 🛠️ Tech Stack

<details>
<summary><b>Click to expand full tech stack</b></summary>

### **Backend**
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Gunicorn-20.1-499848?style=for-the-badge&logo=gunicorn&logoColor=white" />
</p>

### **Frontend**
<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Font_Awesome-528DD7?style=for-the-badge&logo=font-awesome&logoColor=white" />
</p>

### **DevOps**
<p align="center">
  <img src="https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker_Compose-✓-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

### **Monitoring**
<p align="center">
  <img src="https://img.shields.io/badge/Grafana-10.2-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-2.48-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Loki-2.9-FFA500?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/cAdvisor-✓-00ADD8?style=for-the-badge&logo=google&logoColor=white" />
</p>

### **Integrations**
<p align="center">
  <img src="https://img.shields.io/badge/Cloudflare_Turnstile-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_SSO-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenRouter_AI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/SMTP-✓-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</p>
</details>

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version | Badge |
|------|---------|-------|
| Docker | 24.0+ | ![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED?logo=docker) |
| Python | 3.11+ | ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python) |
| PostgreSQL | 15+ | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?logo=postgresql) |

### 🐳 Install & Run (Docker)

```bash
# Clone the repository
git clone https://github.com/AndriyPy/Recipe220.git
cd Recipe220/project/monitoring

# Create .env file
cp .env.example .env
# Edit .env with your keys

# Start the project
docker-compose up -d

# Apply migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### 💻 Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL and run
python manage.py migrate
python manage.py runserver
```

### 📊 Service Access

| Service | URL | Credentials |
|---------|-----|-------------|
| Django App | http://localhost:8000 | Your users |
| Django Admin | http://localhost:8000/admin | Superuser |
| Grafana | http://localhost:3000 | admin / admin |
| Prometheus | http://localhost:9090 | - |
| cAdvisor | http://localhost:8081 | - |

---

## 💡 Usage Examples

<details>
<summary><b>🔍 Search for recipes</b></summary>

```python
# Fuzzy search example
recipes = Recipe.objects.filter(name__icontains="chicken")
# Or use the built-in fuzzy search
results = recipe_search("chiken")  # Works even with typo!
```
</details>

<details>
<summary><b>🤖 Generate recipe with AI</b></summary>

```python
# Generate recipe from ingredients
ingredients = ["chicken", "rice", "onion", "garlic"]
ai_recipe = generate_recipe(ingredients)
print(f"Try this: {ai_recipe.name}")
```
</details>

---

## 📁 Database & Content

<p align="center">
  <img src="https://img.shields.io/badge/Total_Recipes-5%2C000%2B-4CAF50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Users-15%2B-2196F3?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SQLite-✓-003B57?style=for-the-badge" />
</p>

Our database contains **over 5,000 carefully curated recipes**, each with:
- ✅ Title & description
- ✅ Ingredients list
- ✅ Preparation time
- ✅ Cooking time
- ✅ Rating system
- ✅ High-quality images

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Report%20Bug-F58220?style=for-the-badge&logo=bugatti&logoColor=white" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Suggest%20Feature-2D4635?style=for-the-badge&logo=lightbulb&logoColor=white" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Submit%20PR-4CAF50?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" />
</p>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developers

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <a href="https://github.com/AndriyPy">
          <img src="https://avatars.githubusercontent.com/u/187444054?v=4" width="120" style="border-radius: 50%; border: 3px solid #F58220;"/><br/>
          <b>AndriyPy</b>
        </a>
        <br/>
        <sub>Backend Developer</sub>
        <br/>
        <a href="https://github.com/AndriyPy">
          <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" />
        </a>
      </td>
      <td align="center" width="200">
        <a href="https://github.com/pypok-1">
          <img src="https://avatars.githubusercontent.com/u/187442340?v=4" width="120" style="border-radius: 50%; border: 3px solid #2D4635;"/><br/>
          <b>pypok-1</b>
        </a>
        <br/>
        <sub>DevOps / Monitoring</sub>
        <br/>
        <a href="https://github.com/pypok-1">
          <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" />
        </a>
      </td>
    </tr>
  </table>
</div>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer&gradient=F58220,2D4635" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-❤️-F58220?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Made%20in-Ukraine-FFD700?style=for-the-badge&logo=ukraine&logoColor=white" />
</p>

<p align="center">
  <b>⭐ Star us on GitHub — it motivates us to cook more features! ⭐</b>
</p>
