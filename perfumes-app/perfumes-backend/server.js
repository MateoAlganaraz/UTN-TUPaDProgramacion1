// GET: todos los perfumes (público)
app.get('/api/perfumes', (req, res) => {
  res.json(perfumes);
});

// POST: agregar perfume (solo admin)
app.post('/api/perfumes', (req, res) => {
  const { nombre, descripcion, precio, stock } = req.body;
  const nuevo = {
    id: perfumes.length > 0 ? Math.max(...perfumes.map(p => p.id)) + 1 : 1,
    nombre,
    descripcion,
    precio,
    stock,
    imagen: "/images/placeholder.jpg"
  };
  perfumes.push(nuevo);
  res.status(201).json(nuevo);
});

// PATCH: actualizar stock (solo admin)
app.patch('/api/perfumes/:id/stock', (req, res) => {
  const id = parseInt(req.params.id);
  const { cantidad } = req.body; // nuevo stock total
  const perfume = perfumes.find(p => p.id === id);
  if (!perfume) return res.status(404).json({ error: "No encontrado" });
  perfume.stock = parseInt(cantidad);
  res.json(perfume);
});