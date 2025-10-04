// src/App.jsx
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function App() {
  const [perfumes, setPerfumes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:3000/api/perfumes')
      .then(res => res.json())
      .then(data => {
        setPerfumes(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Cargando catálogo...</div>;

  return (
    <div style={{ padding: '20px' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>✨ Perfumería "El Aroma Perfecto"</h1>
        <Link to="/admin" style={{ padding: '8px 16px', backgroundColor: '#4CAF50', color: 'white', textDecoration: 'none', borderRadius: '4px' }}>
          🔐 Admin
        </Link>
      </header>

      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px', marginTop: '20px' }}>
        {perfumes.map(perfume => (
          <div key={perfume.id} style={{
            border: '1px solid #ddd',
            borderRadius: '8px',
            padding: '16px',
            width: '220px',
            boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
          }}>
            <div style={{
              width: '100%',
              height: '180px',
              backgroundColor: '#f0f0f0',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              borderRadius: '4px',
              color: '#666'
            }}>
              🖼️ Imagen de {perfume.nombre}
            </div>
            <h3>{perfume.nombre}</h3>
            <p>{perfume.descripcion}</p>
            <p><strong>Precio:</strong> ${perfume.precio}</p>
            <p>
              <strong>Stock:</strong>{' '}
              <span style={{ color: perfume.stock > 0 ? 'green' : 'red' }}>
                {perfume.stock > 0 ? `${perfume.stock} disponibles` : 'AGOTADO'}
              </span>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;