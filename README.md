# E-Accountant

A modern accounting and inventory management system built with **Django** (Backend) and **React** (Frontend).

---

## Features

- **User Authentication** (Sign up, Login)
- **Product Management** (Add, Edit, Delete, View Products)
- **Sales & Purchases Tracking**
- **Expense Recording**
- **Profit Reports** (Daily, Monthly, Yearly)
- **Stock Statistics** (with charts)
- **Monthly Sales Analysis** (with export to Excel/PDF)
- **Admin Dashboard** with intuitive UI

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** React (TypeScript), Chart.js, Axios
- **Database:** SQLite (default, can be changed)
- **Deployment:** Vercel (Frontend), render (Backend)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/e-accountant.git
cd e-accountant
```

---

### 2. Backend Setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/`.

---

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000/`.

---

## Deployment

- **Frontend:** Deploy the `frontend` folder to [Vercel](https://vercel.com/) (auto-detects React).
- **Backend:** Deploy the `backend` folder to your preferred Python host (e.g., Heroku, Render, Railway).

---

## Customization

- **App Name & Icon:**  
  Edit `frontend/public/manifest.json`, `frontend/public/index.html`, and replace icons in `frontend/public/`.

---

## API Endpoints

- Products: `/api/products/`
- Sales: `/api/sales/`
- Purchases: `/api/purchases/`
- Expenses: `/api/expenses/`
- Profits: `/api/profits/?period=daily|monthly|yearly`
- Monthly Sales: `/api/monthly-sales/`
- Auth: `/api/auth/` (or as configured)

---

## Screenshots

_<img width="425" height="260" alt="image" src="https://github.com/user-attachments/assets/71b0d5ef-d69c-46e0-b716-063b66296d8b" />
<img width="694" height="466" alt="image" src="https://github.com/user-attachments/assets/26694981-b450-479f-a72f-600e107f2e20" />
<img width="708" height="361" alt="image" src="https://github.com/user-attachments/assets/b2841aa9-f4f6-4a9d-bc3f-1c4a6d76064c" />


_

---

## License

[MIT](LICENSE)

---

## Author

- SEKIBAALA MARK (https://github.com/SekibaalaMark)

---

**Feel free to contribute or open
