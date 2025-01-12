const express = require('express');
const router = express.Router();

// Define rutas específicas para productos
router.get('/', (req, res) => {
  res.send('Lista de productos');
});

router.post('/', (req, res) => {
  res.send('Crear un producto');
});

module.exports = router;

const express = require('express');
const app = express();
const routes = require('./routes');

app.use('/api', routes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});