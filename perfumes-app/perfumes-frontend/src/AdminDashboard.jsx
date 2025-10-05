// src/AdminDashboard.jsx
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AdminDashboard() {
  const [perfumes, setPerfumes] = useState([]);
  const [nuevoNombre, setNuevoNombre] = useState('');
  const [nuevaDescripcion, setNuevaDescripcion] = useState('');
  const [nuevoPrecio, setNuevoPrecio] = useState('');
  const [nuevoStock, setNuevoStock] = useState('');
  const [editandoId, setEditandoId] = useState(null);
  const [editForm, setEditForm] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    stock: ''
  });
  const navigate = useNavigate();

  useEffect(() => {
    if (!localStorage.getItem('isAdmin')) {
      navigate('/admin');
    }
    cargarPerfumes();
  }, [navigate]);

  const cargarPerfumes = () => {
    fetch('http://localhost:3000/api/perfumes')
      .then(res => res.json())
      .then(data => setPerfumes(data));
  };

  const handleLogout = () => {
    localStorage.removeItem('isAdmin');
    navigate('/');
  };

  // Agregar nuevo perfume
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
      cargarPerfumes();
      setNuevoNombre('');
      setNuevaDescripcion('');
      setNuevoPrecio('');
      setNuevoStock('');
    }
  };

  // Iniciar edición
  const iniciarEdicion = (perfume) => {
    setEditandoId(perfume.id);
    setEditForm({
      nombre: perfume.nombre,
      descripcion: perfume.descripcion,
      precio: perfume.precio.toString(),
      stock: perfume.stock.toString()
    });
  };

  // Guardar edición
  const guardarEdicion = async (id) => {
    const res = await fetch(`http://localhost:3000/api/perfumes/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(editForm)
    });

    if (res.ok) {
      alert('Perfume actualizado');
      cargarPerfumes();
      setEditandoId(null);
    }
  };

  // Eliminar perfume
  const eliminarPerfume = async (id) => {
    if (!window.confirm('¿Seguro que quieres eliminar este perfume?')) return;

    const res = await fetch(`http://localhost:3000/api/perfumes/${id}`, {
      method: 'DELETE'
    });

    if (res.status === 204) {
      alert('Perfume eliminado');
      cargarPerfumes();
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2>👨‍💼 Panel de Administrador</h2>
        <button 
          onClick={handleLogout} 
          style={{ padding: '8px 16px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
        >
          Cerrar sesión
        </button>
      </header>

      <button 
        onClick={() => navigate('/')} 
        style={{ marginBottom: '20px', padding: '8px 16px', backgroundColor: '#2196F3', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        👀 Ver catálogo público
      </button>

      {/* Formulario para agregar */}
      <section style={{ marginBottom: '30px', padding: '15px', border: '1px solid #ddd', borderRadius: '8px' }}>
        <h3>➕ Agregar nuevo perfume</h3>
        <form onSubmit={handleAgregarPerfume} style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
          <input placeholder="Nombre" value={nuevoNombre} onChange={e => setNuevoNombre(e.target.value)} required style={{ padding: '6px' }} />
          <input placeholder="Descripción" value={nuevaDescripcion} onChange={e => setNuevaDescripcion(e.target.value)} required style={{ padding: '6px' }} />
          <input placeholder="Precio" type="number" step="0.01" value={nuevoPrecio} onChange={e => setNuevoPrecio(e.target.value)} required style={{ padding: '6px', width: '80px' }} />
          <input placeholder="Stock" type="number" value={nuevoStock} onChange={e => setNuevoStock(e.target.value)} required style={{ padding: '6px', width: '70px' }} />
          <button type="submit" style={{ padding: '6px 12px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Agregar</button>
        </form>
      </section>

      {/* Lista de perfumes */}
      <section>
        <h3>📦 Lista de perfumes (editable)</h3>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
          {perfumes.map(perfume => (
            <div key={perfume.id} style={{
              border: '1px solid #ccc',
              padding: '15px',
              borderRadius: '8px',
              width: '280px',
              backgroundColor: '#f9f9f9'
            }}>
              {editandoId === perfume.id ? (
                // Formulario de edición
                <div>
                  <input 
                    value={editForm.nombre} 
                    onChange={e => setEditForm({...editForm, nombre: e.target.value})} 
                    style={{ width: '100%', marginBottom: '8px', padding: '4px' }} 
                  />
                  <textarea 
                    value={editForm.descripcion} 
                    onChange={e => setEditForm({...editForm, descripcion: e.target.value})} 
                    rows="2"
                    style={{ width: '100%', marginBottom: '8px', padding: '4px' }} 
                  />
                  <input 
                    type="number" 
                    step="0.01"
                    value={editForm.precio} 
                    onChange={e => setEditForm({...editForm, precio: e.target.value})} 
                    style={{ width: '100%', marginBottom: '8px', padding: '4px' }} 
                  />
                  <input 
                    type="number" 
                    value={editForm.stock} 
                    onChange={e => setEditForm({...editForm, stock: e.target.value})} 
                    style={{ width: '100%', marginBottom: '12px', padding: '4px' }} 
                  />
                  <div>
                    <button 
                      onClick={() => guardarEdicion(perfume.id)} 
                      style={{ marginRight: '8px', padding: '4px 8px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px' }}
                    >
                      Guardar
                    </button>
                    <button 
                      onClick={() => setEditandoId(null)} 
                      style={{ padding: '4px 8px', backgroundColor: '#9E9E9E', color: 'white', border: 'none', borderRadius: '4px' }}
                    >
                      Cancelar
                    </button>
                  </div>
                </div>
              ) : (
                // Vista normal
                <>
                  <h4>{perfume.nombre}</h4>
                  <p><strong>Descripción:</strong> {perfume.descripcion}</p>
                  <p><strong>Precio:</strong> ${perfume.precio}</p>
                  <p><strong>Stock:</strong> {perfume.stock}</p>
                  <div style={{ marginTop: '10px' }}>
                    <button 
                      onClick={() => iniciarEdicion(perfume)} 
                      style={{ marginRight: '8px', padding: '4px 8px', backgroundColor: '#2196F3', color: 'white', border: 'none', borderRadius: '4px' }}
                    >
                      ✏️ Editar
                    </button>
                    <button 
                      onClick={() => eliminarPerfume(perfume.id)} 
                      style={{ padding: '4px 8px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px' }}
                    >
                      🗑️ Eliminar
                    </button>
                  </div>
                </>
              )}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}