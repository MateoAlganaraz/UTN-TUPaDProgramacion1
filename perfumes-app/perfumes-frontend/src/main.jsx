// src/main.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App'; // ← Catálogo público
import AdminLogin from './AdminLogin';
import AdminDashboard from './AdminDashboard';

const router = createBrowserRouter([
  { path: "/", element: <App /> },
  { path: "/admin", element: <AdminLogin /> },
  { path: "/admin/dashboard", element: <AdminDashboard /> },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
