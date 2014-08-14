/**
 * Created by ashish on 1/7/14.
 */

(function() {
  "use strict";

  /*global jsTraining*/
  jsTraining.controller("MasterCtrl", ["$scope", function($scope) {
    var keys = {
      LEFT: 37, DOWN: 40,
      UP: 38, RIGHT: 39, SPACE: 32
    };
    this.flyInControls = function ($event) {
      $scope.$broadcast("flyInControls");

      if($event.type === "keydown") {
        if($event.keyCode === keys.UP || $event.keyCode === keys.RIGHT || $event.keyCode === keys.SPACE) {
          $scope.$broadcast("nextSlide");
        }
        if($event.keyCode === keys.DOWN || $event.keyCode === keys.LEFT) {
          $scope.$broadcast("previousSlide");
        }
      }
    };
  }]);
})();