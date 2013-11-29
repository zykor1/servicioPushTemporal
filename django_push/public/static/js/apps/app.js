'use strict';

/* App Module */

var pushApp = angular.module('pushApp', [
  'ngRoute',
  'pushControllers'
]);

pushApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/agregarMensaje.html',
        controller: 'MensajesListCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);

pushApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('#{');
  $interpolateProvider.endSymbol('}');
});