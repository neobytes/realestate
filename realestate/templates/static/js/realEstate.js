/*
------------------------------------------------------------------------------

		REAL ESTATE MANAGEMENT ANGULAR JS SCRIPT
                ________________________________________


 Creating the module for real estate called "rsModule"
 and registering controller called rsController 
 and callback functions

------------------------------------------------------------------------------
*/

var myApp = 
angular
.module("rsModule", [])
.controller("rsController", function($scope) {	

	$scope.message = "Real Estate Project By NeoBytes";

}); // controller ends here !!!!!!
