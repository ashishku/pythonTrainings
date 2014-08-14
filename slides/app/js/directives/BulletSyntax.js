/**
 * Created by ashish on 13/8/14.
 */
(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.directive("bulletSyntax", [function () {
    return {
      restrict: "EA",
      template: "<span></span>",
      scope: {
        text: "@",
      },
      link: function (scope, elem) {
        var match, values;
        if (match = /^SYN_LNK##(.*)/.exec(scope.text)) {
          values = match[1].split(/##/);
          if (values.length > 1) {
            elem.append("<a target='_blank' href='" + values[1] + "'>" + values[0] + "</a>");
          }
          else {
            elem.append("<a target='_blank' href='" + values + "'>" + values + "</a>");
          }
        }
        else {
          elem.append(scope.text);
        }
      }
    };
  }]);
})();