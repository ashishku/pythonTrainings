/**
 * Created by ashish on 1/7/14.
 */

(function() {
  "use strict";

  /*global jsTraining*/
  jsTraining.controller("MasterCtrl", ["$scope", function($scope) {
    this.flyInControls = function () {
      $scope.$broadcast("flyInControls");
    };
  }]);
})();