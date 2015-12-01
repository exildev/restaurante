var app = angular.module('restaurante', [
	'ngRoute',
	'controllers',
]);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});
