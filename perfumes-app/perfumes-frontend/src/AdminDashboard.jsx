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

  useEffect(() => {
    // Verifica si el usuario está logueado
    if (!localStorage.getItem('isAdmin')) {
      navigate('/admin');
    }

    fetch('http://localhost:3000/api/perfumes')
      .then(res => res.json())
      .then(data => setPerfumes(data))
      .catch(err => console.error("Error al cargar perfumes:", err));
  }, [navigate]);

  const handleAgregarPerfume = async (e) => {
    e.preventDefault();
    const nuevoPerfume = {
      nombre: nuevoNombre,
      descripcion: nuevaDescripcion,
      precio: parseFloat(nuevoPrecio),
      stock: parseInt(nuevoStock),
      imagen: "/images/placeholder.jpg" // ← Placeholder por ahora
    };

    try {
      const response = await fetch('http://localhost:3000/api/perfumes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevoPerfume)
      });

      if (response.ok) {
        alert('Perfume agregado correctamente');
        setNuevoNombre('');
        setNuevaDescripcion('');
        setNuevoPrecio('');
        setNuevoStock('');
        // Recarga la lista
        const updated = await fetch('http://localhost:3000/api/perfumes').then(r => r.json());
        setPerfumes(updated);
      }
    } catch (err) {
      console.error(err);
      alert('Error al agregar perfume');
    }
  };

  const handleActualizarStock = async (id, nuevoStock) => {
    try {
      const response = await fetch(`http://localhost:3000/api/perfumes/${id}/stock`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cantidad: parseInt(nuevoStock) - getStock(id) })
      });

      if (response.ok) {
        alert('Stock actualizado');
        // Recarga la lista
        const updated = await fetch('http://localhost:3000/api/perfumes').then(r => r.json());
        setPerfumes(updated);
      }
    } catch (err) {
      console.error(err);
      alert('Error al actualizar stock');
    }
  };

  const getStock = (id) => {
    const perfume = perfumes.find(p => p.id === id);
    return perfume ? perfume.stock : 0;
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>📊 Panel de Administrador</h2>
      <button onClick={() => navigate('/')}>Volver al catálogo</button>

      <h3>➕ Agregar nuevo perfume</h3>
      <form onSubmit={handleAgregarPerfume} style={{ marginBottom: '20px' }}>
        <input
          placeholder="Nombre"
          value={nuevoNombre}
          onChange={(e) => setNuevoNombre(e.target.value)}
          required
          style={{ margin: '5px', padding: '8px' }}
        />
        <input
          placeholder="Descripción"
          value={nuevaDescripcion}
          onChange={(e) => setNuevaDescripcion(e.target.value)}
          required
          style={{ margin: '5px', padding: '8px' }}
        />
        <input
          placeholder="Precio"
          value={nuevoPrecio}
          onChange={(e) => setNuevoPrecio(e.target.value)}
          type="number"
          step="0.01"
          required
          style={{ margin: '5px', padding: '8px' }}
        />
        <input
          placeholder="Stock"
          value={nuevoStock}
          onChange={(e) => setNuevoStock(e.target.value)}
          type="number"
          required
          style={{ margin: '5px', padding: '8px' }}
        />
        <button type="submit" style={{ margin: '5px', padding: '8px' }}>Agregar</button>
      </form>

      <h3>📦 Lista de perfumes</h3>
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
            <p><strong>Stock actual:</strong> {perfume.stock}</p>
            <input
              type="number"
              defaultValue={perfume.stock}
              onChange={(e) => handleActualizarStock(perfume.id, e.target.value)}
              style={{ width: '80px', margin: '5px' }}
            />
            <button onClick={() => handleActualizarStock(perfume.id, document.querySelector(`[data-id="${perfume.id}"]`)?.value)} style={{ margin: '5px' }}>Actualizar</button>
          </div>
        ))}
      </div>
    </div>
  );
}