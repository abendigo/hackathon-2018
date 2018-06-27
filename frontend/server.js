const express = require('express');
const bodyParser = require('body-parser');

const fs = require('fs');

const port = process.env.PORT || 3000;
let app = express();

app.listen(port);
app.use(express.static('public'));

const audio = {
    content: fs.readFileSync("public/audio/stereo.flac").toString('base64'),
};

// app.use(bodyParser);
let parse = bodyParser.text();

app.post('/img2mus', parse, (req, res) => {
    console.log('woot', req.body);
    res.json({audio: audio})
});

console.log('todo list RESTful API server started on: ' + port);
