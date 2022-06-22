### A full stack web application with technologies of Docker PostGIS, Django, Celery, Redis, Pytest, Django-REST API, Nginx, Axios, React

# There applications are included for now:

## 1. Shale Well Drill and Completion Optimizaation

The application deployed 4 data models that are created with Scikit-learn Machine Learning . The process collected over 3000 horizontal oil and gas wells frilled before 2020 in north-east BC, tested over 25 data features with four Scikit-learn regression algorithms (Artificial Neural Networks, Adaboost, Support Vector Machine and Random Forest), eventually choosen Random Forest algorithm with 6 data features and produced 4 models for the well optimization and production prediction.

The data models help to optimize horizontal well design and frac parameter planning to achieve maximum financial performance

A breif presentation of the project can be found in the blog section of this website.

## 2. A Interactive Calgary Traffice Accident Map

## 3. American Navy Vessel Tracking Map

## 4. Canadadian Stock Analytics Application

### APIs

# 1. jwt user login api path:

localhost:8080/api/v1/auth/jwt/create/
{
"email": 'user.example@email.com',
"password": 'mypassword'
}

two jwt tokens are generated "refresh": and "access":
the "access" token will be used for all the operations permitted unser the user credentials.

# 2. get all the agents:

localhost:8080/api/v1/profile/agents/all/

# 3. get all the top agents:

localhost:8080/api/v1/profile/top-agents/all/

# 4. get all user's profile:

localhost:8080/api/v1/profile/me/

# 5. Update profile:

localhost:8000/api/v1/profile/update/<username>/
