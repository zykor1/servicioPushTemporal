var WebSocket = require('ws');
var wamp = require('wamp.io');
var queryString = require( "querystring" );
var url = require( "url" );
/*
 * GET home page.
 */


// Este metodo es un RESTful que nos permite que el servidor se comunique con los dispositivos conectados
exports.notificacion = function(req, res){
	var theUrl = url.parse( req.url );
    var queryObj = queryString.parse( theUrl.query );
    var datosDesdeServidor =  queryObj;

	ws = wamp.connect('ws://localhost:9000', function (session, res)
		{
			console.log("Open session");

			// Creamos el prefijo
			session._send([1, "notificacion" , "http://filper.com/pubSub/notifications#"]);
			// Nos inscribimos al prefijo :D
			session._send([5, "notificacion:"+datosDesdeServidor.to]);
			// Enviamos la informacion
			session._send([7, "notificacion:"+datosDesdeServidor.to, datosDesdeServidor]);

		}, function(session){
			console.log("WAMP session close");
		});

		res.send({
        	from: datosDesdeServidor.from,
        	to: datosDesdeServidor.to,
        	message: datosDesdeServidor.message
    	});

};




/*
 * Este metodo es por si algun dia se quiere habilitar una comunicacion rpc entre  servidor-cliente 
exports.inscribe = function(req, res){
	var theUrl = url.parse( req.url );
    var queryObj = queryString.parse( theUrl.query );
    var datosDesdeServidor =  queryObj;

	ws = wamp.connect('ws://localhost:9000', function (session)
		{
			
			even =  datosDesdeServidor
			session.call("http://filper.com/rpc/notifications#changeUserStateConexion", even).promise.then(
					function(reply){
						console.log(reply);
					},

					function(error, desc){
						console.log("error" + error);
						console.log("desc" + desc);
					}
				)

		}, function(session){
			console.log("WAMP session close");
			});


		res.send({
        	message: 'Inscribe user'
    	});
};*/






