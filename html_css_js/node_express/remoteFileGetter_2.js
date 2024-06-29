    const express = require('express');
    const fs = require('fs');
    const app = express();
    
    app.get('/:fileName',(req,res)=>{
      const name=req.params.fileName;
      fs.readFile(name,'utf-8',(err,data)=>{
        if(err){
          return res.status(500).json({
            error: "file sending error"
          });
        }
        res.json({
          data
        });
      });
    });

    app.listen(3000,()=>{
      console.log("Server running on port 3000")
    });
