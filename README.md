# delacruz_timothylance_activities_BSIT3C
# Activity 5

---

## 📌 API Endpoints

| Method | Endpoint                             | Description                     |
|--------|--------------------------------------|---------------------------------|
| POST   | `/api/register/`                     | Register a new user             |
| POST   | `/api/login/`                        | Login and obtain JWT tokens     |
| GET    | `/api/protected/`                    | Access protected content        |
| PUT    | `/api/update/`                       | Update user info                |
| DELETE | `/api/delete/`                       | Delete user account             |

---

## 1. 📝 Register User

**URL:** `http://127.0.0.1:8000/api/register/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "username": "user123",
  "email": "user@example.com",
  "password": "userpassword"
}
```

**Sample Response:**
```json
{
  "username": "user123",
  "email": "user@example.com",
  "password": "<hashed_password>",
  "message": "User registered successfully"
}
```

---

## 2. 🔐 Login (Get JWT Tokens)

**URL:** `http://127.0.0.1:8000/api/login/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "username": "user123",
  "password": "userpassword"
}
```

**Sample Response:**
```json
{
  "refresh": "<refresh_token>",
  "access_token": "<access_token>",
  "message": "User logged in successfully"
}
```

---

## 3. 🔒 Access Protected Route

**URL:** `http://127.0.0.1:8000/api/protected/`  
**Method:** `GET`  

### Headers:
```
Authorization: Bearer <access_token>
```

**Sample Response:**
```json
{
  "message": "Hello user123, you are authenticated!"
}
```

---

## 4. ✏️ Update User Info

**URL:** `http://127.0.0.1:8000/api/update/`  
**Method:** `PUT`  

### Headers:
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "email": "newemail@example.com",
  "password": "newpassword123"
}
```

**Sample Response:**
```json
{
  "message": "User info updated successfully"
}
```

🔁 **Note:** You will need to log in again with the updated credentials.

---

## 5. ❌ Delete User Account

**URL:** `http://127.0.0.1:8000/api/delete/`  
**Method:** `DELETE`  

### Headers:
```
Authorization: Bearer <access_token>
```

**Sample Response:**
```json
{
  "message": "Account deleted successfully"
}
```

---

##  Example Flow

1. Register → `/api/register/`
2. Login → `/api/login/` → receive tokens
3. Use `access_token` to access `/api/protected/`, `/api/update/`, or `/api/delete/`

---

## 📎 Notes

- This app uses [JWT](https://jwt.io/) for stateless authentication.
- Be sure to protect your `access_token` and refresh it when expired.
- Default Django user model is used with `username` as the login field.

---
