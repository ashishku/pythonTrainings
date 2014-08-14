/**
 * Created by ashish on 30/6/14.
 */

(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.factory("TrainingsResources", ["$resource", function ($resource) {
    var url = "api/:training/:slide.json";

    return $resource(url, {slide: "__info__"}, {
      query: {method: "GET", params: {training: "."}, isArray: true}
    });
  }]);
})();