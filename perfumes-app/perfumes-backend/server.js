const express = require('express');
const app = express();

// Middleware obligatorio
app.use(express.json());

// Middleware CORS (solo para desarrollo local)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

// Datos en memoria (¡con un ejemplo inicial!)
let perfumes = [
  {
    id: 1,
    nombre: "Chanel No. 5",
    descripcion: "Un clásico atemporal, floral y elegante.",
    precio: 120.00,
    stock: 8,
    imagen: "/images/placeholder.jpg"
  },
  {
    id: 2,
    nombre: "Dior Sauvage",
    descripcion: "Fresco, amaderado y con un toque especiado.",
    precio: 95.50,
    stock: 0,
    imagen: "/images/placeholder.jpg"
  }
];

// GET: todos los perfumes (público)
app.get('/api/perfumes', (req, res) => {
  res.json(perfumes);
});

// POST: agregar perfume (solo admin)
app.post('/api/perfumes', (req, res) => {
  const { nombre, descripcion, precio, stock } = req.body;
  const nuevo = {
    id: perfumes.length > 0  ? Math.max(...perfumes.map(p => p.id)) + 1 : 1,
    nombre,
    descripcion,
    precio: parseFloat(precio),
    stock: parseInt(stock, 10) || 0,
    imagen: "/images/placeholder.jpg"
  };
  perfumes.push(nuevo);
  res.status(201).json(nuevo);
});

// PATCH: actualizar stock (solo admin)
app.patch('/api/perfumes/:id/stock', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const { cantidad } = req.body;
  const perfume = perfumes.find(p => p.id === id);
  if (!perfume) return res.status(404).json({ error: "Perfume no encontrado" });
  perfume.stock = parseInt(cantidad, 10) || 0;
  res.json(perfume);
});

// PUT: actualizar perfume completo
app.put('/api/perfumes/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const { nombre, descripcion, precio, stock } = req.body;

  const index = perfumes.findIndex(p => p.id === id);
  if (index === -1) {
    return res.status(404).json({ error: "Perfume no encontrado" });
  }

  perfumes[index] = {
    ...perfumes[index],
    nombre,
    descripcion,
    precio: parseFloat(precio),
    stock: parseInt(stock, 10) || 0
  };

  res.json(perfumes[index]);
});

// DELETE: eliminar perfume
app.delete('/api/perfumes/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const index = perfumes.findIndex(p => p.id === id);
  if (index === -1) {
    return res.status(404).json({ error: "Perfume no encontrado" });
  }
  perfumes.splice(index, 1);
  res.status(204).send();
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ Backend corriendo en http://localhost:${PORT}`);
});                          