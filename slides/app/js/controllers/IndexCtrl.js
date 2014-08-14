/**
 * Created by ashish on 30/6/14.
 */

(function() {
  "use strict";

  /*global jsTraining*/
  jsTraining.controller("IndexCtrl", ["$scope", "TrainingsResources", function($scope, TrainingsResources) {
    $scope.trainings = TrainingsResources.query();

    this.url = function(training) {
      return "/training/" + training.id;
    };
  }]);
})();