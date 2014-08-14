/**
 * Created by ashish on 30/6/14.
 */

(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.controller("TrainingCtrl", ["$scope", "$routeParams", "Training", function ($scope, $routeParams, Training) {

    $scope.training = Training.fetchTraining($routeParams.trnId);
    $scope.slide = {id: "__info__", title: "____"};

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
  }]);
})();