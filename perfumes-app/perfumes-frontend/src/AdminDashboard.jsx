// src/AdminDashboard.jsx
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AdminDashboard() {
  const [perfumes, setPerfumes] = useState([]);
  const [nuevoNombre, setNuevoNombre] = useState('');
  const [nuevaDescripcion, setNuevaDescripcion] = useState('');
  const [nuevoPrecio, setNuevoPrecio] = useState('');
  const [nuevoStock, setNuevoStock] = useState('');
  const navigate = useNavigate();

  // Verifica si el usuario está logueado
  useEffect(() => {
    if (!localStorage.getItem('isAdmin')) {
      navigate('/admin');
    }

    fetch('http://localhost:3000/api/perfumes')
      .then(res => res.json())
      .then(data => setPerfumes(data));
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('isAdmin');
    navigate('/');
  };

  const handleAgregarPerfume = async (e) => {
    e.preventDefault();
    const nuevoPerfume = {
      nombre: nuevoNombre,
      descripcion: nuevaDescripcion,
      precio: parseFloat(nuevoPrecio),
      stock: parseInt(nuevoStock),
      imagen: "/images/placeholder.jpg"
    };

    const res = await fetch('http://localhost:3000/api/perfumes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevoPerfume)
    });

    if (res.ok) {
      alert('Perfume agregado');
      const updated = await fetch('http://localhost:3000/api/perfumes').then(r => r.json());
      setPerfumes(updated);
      // Limpiar form
      setNuevoNombre('');
      setNuevaDescripcion('');
      setNuevoPrecio('');
      setNuevoStock('');
    }
  };

  const handleActualizarStock = async (id, nuevoStock) => {
    const res = await fetch(`http://localhost:3000/api/perfumes/${id}/stock`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cantidad: parseInt(nuevoStock) })
    });

    if (res.ok) {
      alert('Stock actualizado');
      const updated = await fetch('http://localhost:3000/api/perfumes').then(r => r.json());
      setPerfumes(updated);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2>👨‍💼 Panel de Administrador</h2>
        <button onClick={handleLogout} style={{ padding: '8px 16px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px' }}>
          Cerrar sesión
        </button>
      </header>

      <button onClick={() => navigate('/')} style={{ marginBottom: '20px' }}>
        👀 Ver catálogo público
      </button>

      <h3>➕ Agregar nuevo perfume</h3>
      <form onSubmit={handleAgregarPerfume} style={{ marginBottom: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
        <input placeholder="Nombre" value={nuevoNombre} onChange={e => setNuevoNombre(e.target.value)} required />
        <input placeholder="Descripción" value={nuevaDescripcion} onChange={e => setNuevaDescripcion(e.target.value)} required />
        <input placeholder="Precio" type="number" step="0.01" value={nuevoPrecio} onChange={e => setNuevoPrecio(e.target.value)} required />
        <input placeholder="Stock" type="number" value={nuevoStock} onChange={e => setNuevoStock(e.target.value)} required />
        <button type="submit">Agregar</button>
      </form>

      <h3>📦 Lista de perfumes (editable)</h3>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
        {perfumes.map(perfume => (
          <div key={perfume.id} style={{
            border: '1px solid #ccc',
            padding: '15px',
            borderRadius: '8px',
            width: '250px'
          }}>
            <h4>{perfume.nombre}</h4>
            <p>{perfume.descripcion}</p>
            <p><strong>Precio:</strong> ${perfume.precio}</p>
            <div>
              <label>Stock:</label>
              <input
                type="number"
                defaultValue={perfume.stock}
                onChange={(e) => handleActualizarStock(perfume.id, e.target.value)}
                style={{ width: '80px', margin: '5px' }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}