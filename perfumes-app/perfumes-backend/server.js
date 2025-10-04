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
    imagen: "/images/Eau-de-perfum.jpeg"
  },
  {
    id: 2,
    nombre: "Musk Noir",
    descripcion: "Notas de madera y especias.",
    precio: 120.00,
    stock: 5,
    imagen: "/images/Musca-noir.jpeg"
  },
  {
    id: 3,
    nombre: "Ocean Breeze",
    descripcion: "Frescura marina y cítrica.",
    precio: 65.50,
    stock: 0, // Sin stock
    imagen: "/images/Ocean-breeze.jpeg"
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

// Endpoint: Actualizar stock (simulación)
app.patch('/api/perfumes/:id/stock', (req, res) => {
  const id = parseInt(req.params.id);
  const { cantidad } = req.body;

  const perfume = perfumes.find(p => p.id === id);
  if (!perfume) {
    return res.status(404).json({ error: "Perfume no encontrado" });
  }

  perfume.stock += cantidad; // Sumar o restar (si cantidad es negativo, reduce stock)
  res.json(perfume);
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`✅ Backend corriendo en http://localhost:${PORT}`);
});