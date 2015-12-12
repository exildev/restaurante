var controllers = angular.module('controllers', []);


controllers.controller('cont1', ['$scope', '$http',
	function ($scope, $http) {
		$scope.hola=2;
	}
]);

controllers.controller('TabController', function(){
	this.tab = 1;

	this.selectTab = function(tab){
		this.tab = tab;
	};

	this.isSelect = function(tab){
		return this.tab === tab;
	};
});

controllers.controller('RequisicionController',['$http','$scope',function($http, $scope){
	$('.datepicker').pickadate({
	    selectMonths: true, // Creates a dropdown to control month
	    selectYears: 15 ,// Creates a dropdown of 15 years to control year
	    today: 'Hoy',
		clear: 'Limpiar',
		close: 'Cerrar',
		labelMonthNext: 'Proximo mes',
		labelMonthPrev: 'Mes anterior',
		labelMonthSelect: 'Seleccionar un mes',
		labelYearSelect: 'Seleccionar un año',
		monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
		monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
		weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
		weekdaysShort: ['Dom', 'LUn', 'Mar', 'Mier', 'Jue', 'Vier', 'Sab'],
		format:'yyyy/mm/dd'
	});
	$scope.$on('requesiciones', function(){
		$http.get('/inventario/requisiciondecompra/list/').success(function(data){
			$scope.requesiciones = data.object_list;
			$scope.totalrequisicion = data.num_rows;
		});
	});
	$scope.$emit('requesiciones');
	$scope.sortKey;
	$scope.reverse;
   	$scope.sort = function(keyname){
        $scope.sortKey = keyname;   //set the sortKey to the param passed
        $scope.reverse = !$scope.reverse; //if true make it false and vice versa
    }
	$scope.openModal = function(){
		$('#modal1').openModal();
		$('select').material_select();
	};
	$scope.addForm = addForm;
	$scope.singleRequisicion = singleRequisicion;
}]);

var addForm = controllers.directive('addForm', function(){
	return {
		restrict:'E',
		templateUrl:'/angularinv/form/requisicion.html',
		controller: 'formControllers',
		controllerAs:'formController'
	}
});

controllers.controller('formControllers', ['$http','$scope', function($http, $scope){
	
	/*$scope.productos = [
		{
			"id":1,
			"nombre": "Producto 1"
		},
		{
			"id":2,
			"nombre":"Producto 2"
		}
	];
	*/
	$http.get('/inventario/producto/list/').success(function(data){
			$scope.productos = data.object_list
	});
	$scope.activar = [];

	var data = $scope.data = [];
	$scope.presentacionP = [];
	$scope.total = 2;
	$scope.range = function(min, max, step){
	    var step = step || 1;
	    var input = [];
	    for (var i = min; i <= max; i += step) input.push(i);
	    $('select').material_select();
	    return input;
	};
	$scope.presentaciones = function(lista, n){
		if(lista.object_list.length > 0){
			$scope.presentacionP = lista.object_list;
			$scope.activar[n] = false;
		}else{
			$scope.presentacionP = [];
			$scope.activar[n] = true;
		};
	};
	$scope.enviarForm = function(){
		var dataSend = {};
		if(data.codigo){
			dataSend.codigo = data.codigo;
		}if(data.producto){
			for (p in data.producto ) {
				dataSend["solicituddeproducto_set-"+p+"-producto"] = data.producto[p].id;
			};
		}if(data.presentacion){
			for (k in data.presentacion) {
				dataSend["solicituddeproducto_set-"+k+"-presentacion"] = data.presentacion[k];
			};
		}if (data.cantidad) {
			for (h in data.cantidad) {
				dataSend["solicituddeproducto_set-"+h+"-cantidad"] = data.cantidad[h];
			}				
		}if (data.deletE) {
			for (d in data.deletE){
				dataSend["solicituddeproducto_set-"+d+"-DELETE"] = data.deletE[d];
			}
		};
		dataSend["csrfmiddlewaretoken"] = $("input[name='csrfmiddlewaretoken']").val();
		dataSend["solicituddeproducto_set-TOTAL_FORMS"] = $scope.total;
		dataSend["solicituddeproducto_set-INITIAL_FORMS"] = 0;
		dataSend["solicituddeproducto_set-MIN_NUM_FORMS"] = 0;
		dataSend["solicituddeproducto_set-MAX_NUM_FORMS"] = 1000;
		$http({
			method:'POST',
			url:'/inventario/requisiciondecompra/form/',
			data:$.param(dataSend),
			headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
		}).then(function successCallback(response){
			$scope.$emit('requesiciones');
			$('#modal1').closeModal();
			Materialize.toast('Guardado Exitoso', 4000);
			$scope.total = 2;
			$scope.data = [];
		}, function errorCallback(response){
			var datos = response.data;
			if(datos.inlines.length>0){
				for (var i = 0; i < datos.inlines.length; i++) {
					if(datos.inlines[i].producto){
						for(pro in datos.inlines[i].producto){
							Materialize.toast('Producto: ' +datos.inlines[i].producto[pro], 4000);
						}
					}
					if(datos.inlines[i].cantidad){
						for(pro in datos.inlines[i].cantidad){
							Materialize.toast('Cantidad: ' +datos.inlines[i].cantidad[pro], 4000);
						}
					}
					if(datos.inlines[i].presentacion){
						for(pro in datos.inlines[i].presentacion){
							Materialize.toast('Presentacion: ' +datos.inlines[i].presentacion[pro], 4000);
						}
					}
				};
			}
		});
		
	};
	$scope.addStact = function(){
		$scope.total += 1;
	};
	var eliminar = [];
	$scope.selectDelete = function(num, bool){
		var index = eliminar.indexOf(num);
		if (index > -1 && !bool) {
		   eliminar.splice(index, 1);
		}if(index === -1 && bool){
			eliminar.push(num);
		}
	};
	$scope.hideSelect = function(){
		var index = 0;
		for(c in data.check){
			index = eliminar.indexOf(parseInt(c));
			if(index > -1){
				data.check[c] = true;
			}
		}
	};
}]);	

var singleRequisicion = controllers.directive('singleRequisicion', function(){
	return {
		restrict:'E',
		templateUrl:'/angularinv/singleRequisicion.html',
		controller: 'singleController',
		controllerAs:'single'
	};
});

controllers.controller('singleController', ['$http','$scope', function($http, $scope){
	$scope.singleModal = function(id){
		$scope.singler = [];
		$http({
			method:'GET',
			url:'/inventario/requisiciondecompra/detail/'+id+'/',
		}).then(function successCallback(response){
			$scope.singler = response.data;
		}, function errorCallback(response){
			console.log(response);
		});
		$scope.editar = false;
		$('#modal2').openModal();

	};
	$scope.eliminarP = function(producto){
		var datos = {};
		datos["csrfmiddlewaretoken"] = $("input[name='csrfmiddlewaretoken']").val();
		$http({
			method:'POST',
			data:$.param(datos),
			headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
			url:'/inventario/requisiciondecompra/delete/'+producto.pk+'/'
		}).then(function  successCallback(response){
			var index = $scope.singler.productos.object_list.indexOf(producto);
			$scope.singler.productos.object_list.splice(index, 1);	
			Materialize.toast('Eliminado correctamente', 4000);
		}, function errorCallback(response){
			console.log(response);
		});
	};
}]);
