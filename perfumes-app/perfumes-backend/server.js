const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Datos simulados (luego podrías usar una DB real)
let perfumes = [
  {
    id: 1,
    nombre: "Eau de Parfum",
    descripcion: "Fragancia floral fresca.",
    precio: 89.99,
    stock: 15,
    imagen: "/images/eau-de-perfum.jpeg"
  },
  {
    id: 2,
    nombre: "Musk Noir",
    descripcion: "Notas de madera y especias.",
    precio: 120.00,
    stock: 5,
    imagen: "/images/musc-noir.jpeg"
  },
  {
    id: 3,
    nombre: "Ocean Breeze",
    descripcion: "Frescura marina y cítrica.",
    precio: 65.50,
    stock: 0, // Sin stock
    imagen: "/images/ocean-breeze.jpeg"
  }
];

// Endpoint: Obtener todos los perfumes
app.get('/api/perfumes', (req, res) => {
  res.json(perfumes);
});

// Endpoint: Obtener un perfume por ID
app.get('/api/perfumes/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const perfume = perfumes.find(p => p.id === id);
  if (!perfume) {
    return res.status(404).json({ error: "Perfume no encontrado" });
  }
  res.json(perfume);
});

// Endpoint: Agregar nuevo perfume
app.post('/api/perfumes', (req, res) => {
  const { nombre, descripcion, precio, stock, imagen } = req.body;

  const nuevoPerfume = {
    id: perfumes.length + 1,
    nombre,
    descripcion,
    precio,
    stock,
    imagen: imagen || "/images/placeholder.jpg"
  };

  perfumes.push(nuevoPerfume);
  res.status(201).json(nuevoPerfume);
});

// Endpoint: Actualizar stock (ya lo tenías, pero lo mejoramos)
app.patch('/api/perfumes/:id/stock', (req, res) => {
  const id = parseInt(req.params.id);
  const { cantidad } = req.body; // cantidad es el nuevo stock total (no delta)

  const perfume = perfumes.find(p => p.id === id);
  if (!perfume) {
    return res.status(404).json({ error: "Perfume no encontrado" });
  }

  perfume.stock = parseInt(cantidad); // Asigna directamente el nuevo stock
  res.json(perfume);
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`✅ Backend corriendo en http://localhost:${PORT}`);
});