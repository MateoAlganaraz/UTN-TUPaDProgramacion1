import { useEffect, useState } from 'react';

function App() {
  const [perfumes, setPerfumes] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/api/perfumes')
      .then(res => res.json())
      .then(data => setPerfumes(data))
      .catch(err => console.error("Error al cargar perfumes:", err));
  }, []);

  return (
    <div className="App">
      <h1>🌟 Catálogo de Perfumes</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
        {perfumes.map(perfume => (
          <div key={perfume.id} style={{
            border: '1px solid #ccc',
            padding: '15px',
            borderRadius: '8px',
            width: '250px'
          }}>
            <img src={perfume.imagen} alt={perfume.nombre} style={{ width: '100%', height: '200px', objectFit: 'cover' }} />
            <h3>{perfume.nombre}</h3>
            <p>{perfume.descripcion}</p>
            <p><strong>Precio:</strong> ${perfume.precio}</p>
            <p>
              <strong>Stock:</strong> 
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
