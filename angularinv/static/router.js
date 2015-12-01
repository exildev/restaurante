 app.config(['$routeProvider','$locationProvider', '$httpProvider',
 	function($routeProvider, $locationProvider, $httpProvider){
			//$httpProvider.defaults.headers.common.Authorization = 'Token 1';
			$routeProvider.
			when('/dashboard', {
				templateUrl: '/angularinv/dashboard.html',
				controller: 'cont1'
			})
			.when('/ventas',{
				templateUrl: '/angularinv/ventas.html'
			})
			.when('/requisicion',{
				templateUrl: '/angularinv/requisicion.html',
				controller:'RequisicionController'
			})
			.when('/inventario',{
				templateUrl:'/angularinv/inventario.html'
			})
			.when('/recetas',{
				templateUrl:'/angularinv/recetas.html'
			})
			.otherwise({
				redirectTo: '/dashboard'
			});
		}
]);