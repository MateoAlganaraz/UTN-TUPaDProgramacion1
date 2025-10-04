import { useState, useEffect } from 'react';

function App() {
  const [perfumes, setPerfumes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Llamada al backend
    fetch('http://localhost:3000/api/perfumes')
      .then(response => {
        if (!response.ok) {
          throw new Error('Error al cargar los perfumes');
        }
        return response.json();
      })
      .then(data => {
        setPerfumes(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Cargando catálogo de perfumes...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h1>🌟 Catálogo de Perfumes</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
        {perfumes.map(perfume => (
          <div
            key={perfume.id}
            style={{
              border: '1px solid #ddd',
              borderRadius: '8px',
              padding: '16px',
              width: '220px',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
            }}
          >
            <img
              src={perfume.imagen}
              alt={perfume.nombre}
              style={{ width: '100%', height: '200px', objectFit: 'cover'}}
            />
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
