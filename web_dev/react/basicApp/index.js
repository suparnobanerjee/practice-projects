const express = require('express');
const app = express();

function userMiddlewares(req, res, next) {
  const username = req.headers.username;
  const pass = req.headers.pass;
  if (!(username == 'sparno' || pass == 'abc123')) {
    res.status(403).json({
      "Msg": 'incorrect credentials',
    });
    return;
  } else {
    next();
  }
}

app.get('/user-check', userMiddlewares, (req, res) => {
  res.send('Logged in. Welcome!');
});

app.listen(3000);
