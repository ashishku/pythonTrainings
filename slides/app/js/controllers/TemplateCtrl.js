/**
 * Created by ashish on 30/6/14.
 */

(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.controller("TemplateCtrl", ["$scope", "$routeParams", "Training", function ($scope, $routeParams, Training) {
    function loadTemplate() {
      var slide = ($routeParams.sldId) ? $routeParams.sldId : "__agenda__";
      $scope.slide = Training.fetchSlide(slide);
    }

    if(Training.isLoaded()) {
      loadTemplate();
    }
    else {
      $scope.training = Training.fetchTraining($routeParams.trnId);
      $scope.training.$promise.then(loadTemplate);
    }

    this.hasNextSlide = function () {
      return Training.hasNextSlide();
    };
    this.hasPreviousSlide = function () {
      return Training.hasPreviousSlide();
    };

    this.nextSlide = function () {
      return Training.nextSlide();
    };
    this.previousSlide = function () {
      return Training.previousSlide();
    };
    this.isArray = function(ref) {
      return angular.isArray(ref);
    };
  }]);
})();