# Educere -- Project Deployment & Cloud Technology Case Study

### Innolift Ventures \| Full Stack AI Developer Program \| Day 53

## Overview

Day 53 focused on preparing **Educere -- Intelligent Student Risk &
Performance Analytics** for cloud deployment and studying suitable
deployment platforms.

Educere consists of a React/Vite frontend, Flask backend/API, MySQL
database, and integrated ML model.

## Deployment Architecture

``` text
React / Vite Frontend
        ↓
      Vercel
        ↓
    Flask REST API
        ↓
      Render
     ↙      ↘
  MySQL     ML Model
```

## Platforms Studied

-   Render
-   Railway
-   Vercel
-   Netlify
-   AWS
-   Microsoft Azure
-   Google Cloud

The comparison considered frontend/backend deployment, databases,
environment variables, pricing/free tiers, scalability, and security.

## Vercel

Suitable for modern frontend applications such as React and Vite.
Educere's React/Vite frontend is deployed through Vercel and
communicates with the Flask backend through the configured API base URL.

## Render

Suitable for Python web services and REST APIs. Educere's Flask backend
is deployed using Render for authentication, student management, ML
predictions, and database operations.

## Railway

Considered as an alternative platform for backend services and
databases.

## Netlify

Considered as an alternative frontend hosting platform for React and
other modern web applications.

## AWS

Provides extensive cloud services for frontend hosting, backend
services, databases, ML workloads, storage, networking, security, and
monitoring. It offers flexibility and scalability but generally requires
more configuration.

## Microsoft Azure

Provides cloud hosting, databases, storage, networking, security,
analytics, and AI services and is suitable for larger cloud-based
applications.

## Google Cloud

Provides application hosting, databases, storage, analytics, networking,
and machine-learning services.

## Environment Variables

Sensitive values should never be hard-coded:

``` text
VITE_API_BASE_URL
FLASK_SECRET_KEY
CORS_ALLOWED_ORIGINS
DATABASE_HOST
DATABASE_USER
DATABASE_PASSWORD
DATABASE_NAME
```

## Security Considerations

-   Use HTTPS
-   Keep secrets out of source code
-   Restrict CORS to trusted origins
-   Use a strong Flask secret key
-   Protect administrative routes
-   Validate API inputs
-   Do not expose database credentials
-   Monitor production logs

## Cost / Free-Tier Considerations

Free tiers are useful for academic demonstrations but can have
limitations such as instance spin-down, compute limits, storage limits,
bandwidth quotas, and reduced performance. A production-scale system
should evaluate paid plans and managed database options.

## Platform Selection

For Educere, **Vercel + Render** is a practical deployment strategy: -
**Vercel:** React/Vite frontend - **Render:** Flask backend/API

This keeps frontend and backend responsibilities separated while
communicating through REST APIs.

## Deployment Workflow

``` text
Local Development
       ↓
GitHub Repository
   ↙          ↘
Vercel       Render
Frontend     Backend
                ↓
             Database
                ↓
             ML Model
```

## Final Outcome

The Day 53 activity established a deployment strategy for moving Educere
from development into a cloud-hosted environment and documented platform
selection, environment-variable management, API integration, cost
considerations, and basic security requirements.

## Project

**Educere -- Intelligent Student Risk & Performance Analytics**

**Developer:** Salman Maricar
