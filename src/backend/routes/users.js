const express = require('express');
const router = express.Router();

// Define rutas específicas para usuarios
router.get('/', (req, res) => {
  res.send('Lista de usuarios');
});

router.post('/', (req, res) => {
  res.send('Crear un usuario');
});

module.exports = router;