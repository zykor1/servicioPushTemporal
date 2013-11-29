'use strict';


//* Configuracion */

var pushApp = angular.module('pushApp', [
  'ngRoute',
  'pushControllers'
]);

pushApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('#{');
  $interpolateProvider.endSymbol('}');
});



/* Controllers */

var pushControllers = angular.module('pushControllers', []);

pushControllers.controller('MensajesListCtrl', ['$scope', '$http',
  function PhoneListCtrl($scope, $http) {
    $http.get('/leeMensajes', {params: { "to": "saul" }}).success(function(data) {
      $scope.mensajes = data;
      $scope.msj = "Mensaje raro";
    });

    $scope.orderProp = 'tipo';
}]);

pushControllers.controller('NuevoMensajeCtrl', ['$scope', '$http',
  function nuevoMenCtrl($scope, $http) {
    $scope.nuevoMensaje = function(){
    	console.log($scope.admensaje);
    	$http.get('/enviaNotificacion', {params:
       { "to": $scope._to,
        "from" : $scope._from,
        "activity" : $scope._activity,
        "message" : $scope._message,
        "title" : $scope._title }
      }).success(function(data) {
    	   console.log(data);
   		});
    }
}]);
