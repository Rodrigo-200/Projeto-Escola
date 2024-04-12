const express = require('express');
const fs = require('fs');
const app = express();
app.use(express.json()); // Middleware to parse JSON bodies

app.get('/webhook', (req, res) => {
    fs.readFile('https://indigo-guttural-daphne.glitch.me/data.json', (err, data) => {
        if (err) {
            res.status(500).send('Error reading data file');
            return;
        }
        res.status(200).send(data);
    });
});

app.post('/webhook', (req, res) => {
    console.log('Received data:', req.body);
    fs.writeFile('https://indigo-guttural-daphne.glitch.me/data.json', JSON.stringify(req.body, null, 4), (err) => {
        if (err) {
            console.error('Error writing file:', err);
            return res.sendStatus(500); // Internal Server Error
        }
        console.log('Data written to data.json');
        res.sendStatus(200); // OK
    });
});

const listener = app.listen(process.env.PORT, () => {
    console.log('Your app is listening on port ' + listener.address().port);
});
