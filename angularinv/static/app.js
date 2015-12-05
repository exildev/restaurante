var app = angular.module('restaurante', [
	'ngRoute',
	'controllers',
	'angularUtils.directives.dirPagination'
]);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});


app.config(function(paginationTemplateProvider) {
    paginationTemplateProvider.setPath('/angularinv/dirPagination.tpl.html');
});