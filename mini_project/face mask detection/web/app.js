const express = require('express'),
      app = express();


app.use(express.static('public'));

app.engine('html',require('ejs').renderFile);

app.set('view engine','ejs');


app.get('/',(req,res)=>{
    res.render('landing.html');
})

app.get('/about',(req,res)=>{
    res.render('about.html');
})

app.get('/stream',(req,res)=>{
    res.render('index.html');
})

const port = process.env.PORT || 5000;

app.listen(port,()=>{
    console.log(`serving on port ${port}`);
})