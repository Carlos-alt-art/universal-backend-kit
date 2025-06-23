# 🌐 Universal Backend Kit

**Universal Backend Kit** es una colección de backends modulares escritos en diferentes lenguajes y frameworks, diseñados con una arquitectura limpia, desacoplada y fácilmente adaptable a múltiples motores de base de datos como **MongoDB**, **PostgreSQL**, **MySQL**, entre otros.

El objetivo es proporcionar plantillas reutilizables y extensibles para proyectos reales, facilitando la integración y migración entre tecnologías.

---

## 🚀 Características principales

- 🔁 **Base de datos intercambiable** (Mongo ↔ SQL) mediante configuración `.env`
- 🧩 **Arquitectura desacoplada**: separación entre lógica de negocio y acceso a datos
- 🌍 **Multilenguaje**: incluye ejemplos en FastAPI, Express, Spring Boot, y más
- 📦 **Listo para Docker**: configuración básica con Docker y Docker Compose
- 🔬 **Ideal para pruebas, aprendizaje y prototipos reales**

---

## 📁 Estructura del proyecto

```bash
universal-backend-kit/
│
├── fastapi/
│   ├── app/
│   ├── db/
│   │   ├── mongo_repo.py
│   │   └── sql_repo.py
│   ├── main.py
│   └── .env
│
├── express/
│   ├── src/
│   ├── repositories/
│   │   ├── user.mongo.js
│   │   └── user.sql.js
│   ├── server.js
│   └── .env
│
├── springboot/
│   ├── src/
│   ├── repository/
│   │   ├── UserRepository.java
│   │   ├── MongoUserRepo.java
│   │   └── SqlUserRepo.java
│   └── application.properties
│
├── docs/
│   └── arquitectura.md
│
└── README.md
```

## 🛠️ Tecnologías y stacks incluidos

| Lenguaje | Framework | DB por defecto | Arquitectura | Docker |
|----------|-----------|---------------|--------------|--------|
| Python | FastAPI | PostgreSQL | Desacoplada | ✅ |
| JS | Express.js | MongoDB | Modular | ✅ |
| Java | Spring Boot | MySQL | Clean Arch | ✅ |
| (más...) | (próximamente) | - | - | - |

## 🧠 Filosofía del proyecto

**La lógica de negocio debe ser independiente de la base de datos.**

Esto permite reusar el código, facilitar pruebas, y migrar tecnologías sin romper tu app.

## 📦 Cómo empezar

Cada carpeta es un proyecto independiente. Revisa el README.md dentro de cada uno para ver instrucciones específicas.

Ejemplo para FastAPI:

```bash
cd fastapi
cp .env.example .env
docker-compose up --build
```

## 📌 Contribuciones

¿Quieres añadir otro stack (NestJS, Django, Rust, Go...)?

¡Las PRs están abiertas! Solo asegúrate de seguir la estructura desacoplada y documentar bien tu implementación.

## 📄 Licencia

MIT © Carlos – 2025

---

¿Quieres que te genere también un README.md individual para una de las carpetas como `fastapi/README.md`?
