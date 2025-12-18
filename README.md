## Homepage - Screenshot

<img src="/static/demo_images/homepage.png" height="600" />
## Product Page -Screenshot
<img src="/static/demo_images/productPage.png" height="600"/>

# Basic-Website-in-Django

## Description

A basic website built using the Django web framework with tailwind integration.
This project demonstrates Django fundamentals such as project structure, views, URLs, and templates.

## Getting Started - Follow this steps 👇

### 1️⃣ Clone the repo.Setup and run the project

```bash
git clone https://github.com/pokhrelyadav/Basic-Website-in-Django.git
```

```bash
cd Basic-Website-in-Django
```

### 2️⃣ Virtual environment and Activation

```bash
uv venv
```

### On linux/mac

```bash
source .venv/bin/activate
```

### On Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Install requirements

```bash
uv pip install -r requirements.txt
```

### Frontend (npm)

```bash
npm install --prefix ./theme/static_src
```

### 4️⃣ Run the project

python manage.py migrate

Open two terminal and run below:

Terminal 1:

```bash
python manage.py runserver
```

Terminal 2:

```bash
python manage.py tailwind start
```

After starting the server, open the app in your browser:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
