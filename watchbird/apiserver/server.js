// server.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use('/images', express.static(path.join(__dirname, '../save')));

app.get('/api/latest-image', (req, res) => {
  const dir = path.join(__dirname, '../save');
  const files = fs.readdirSync(dir)
  .filter(file => file.startsWith('frame_') && file.endsWith('.jpg'))
  .sort((a, b) => {
    const getTime = f => {
      const match = f.match(/frame_(\d+)\.jpg/);
      return match ? parseInt(match[1]) : 0;
    };
    return getTime(b) - getTime(a);
  });

  if (files.length > 0) {
    res.json({ imageUrl: `/images/${files[0]}` });
  } else {
    res.status(404).json({ error: 'No image found' });
  }
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
