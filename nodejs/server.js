// Start express server and listen for socket.io connections
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

server.listen(4000, function(){
  console.log('listening to requests on port 4000')
});

// Static files
app.use(express.static('public'));

// Socket setup
io.on('connection', function(socket) {
  console.log('made socket connection', socket.id);

  socket.on('chat', function(data){
    io.sockets.emit('chat', data);
  });

  socket.on('typing', function(data){
    socket.broadcast.emit('typing', data);
  });

});
