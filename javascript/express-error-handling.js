const express = require('express');

const app = express();

app.get('/', safeHandler(handler));

app.listen(3000);

function safeHandler(handler) {
  return function(req, res) {
    handler(req, res).catch(error => res.status(500).send(error.message));
  };
}

async function handler(req, res) {
  await new Promise((resolve, reject) => reject(new Error('Hang!')));
  res.send('Hello, World!');
}

