/**
 * Created by ashish on 1/7/14.
 */
(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.directive("pptFlyInControls", ["$document", "$timeout", function ($document, $timeout) {
    var selectBox = "<span class='slide-ctrl'><select>" +
      "<option>Slide 1</option>" +
      "<option>Slide 2</option>" +
      "<option>Slide 3</option>" +
      "<option>Slide 4</option>" +
      "<option>Slide 5</option>" +
      "</select></span>";

    var template = "<span class='text-as-link' ng-class='{\"disable-link\": !leftArrowShow}' ng-click='clickArrow(\"left\")'>&#xe4a1;</span>" +
      "<span class='link-separator'>&#x007c</span>" +
      "<a class='text-as-link' href='#'>&#x24bd;</a>" +
      "<span class='link-separator'>&#x007c</span>" +
      selectBox +
      "<span class='link-separator'>&#x007c</span>" +
      "<span class='text-as-link fullscreen-ctrl' ng-hide='inFullScreenMode' ng-click='fullScreen()'>&#xe310;</span>" +
      "<span class='text-as-link fullscreen-ctrl' ng-show='inFullScreenMode' ng-click='fullScreen()'>&#xe311;</span>" +
      "<span class='link-separator'>&#x007c</span>" +
      "<span class='text-as-link' ng-class='{\"disable-link\": !rightArrowShow}' ng-click='clickArrow(\"right\")'>&#xe4a2;</span>";

    return {
      restrict:    "A",
      templateUrl: "app/partials/directives/pptFlyInControls.html",
      scope:       {
        leftArrowClick:  "&",
        rightArrowClick: "&",
        leftArrowShow:   "=",
        rightArrowShow:  "=",
        slidesList:      "=",
        selectedSlide:   "="
      },
      link:        function (scope, elem) {
        angular.forEach(scope.slidesList, function (s) {
          if( s.id === scope.selectedSlide.id) {
            scope.selectedSlide = s;
          }
        });

        scope.clickArrow = function (dir) {
          if ( dir === "left" && scope.leftArrowShow ) {
            scope.leftArrowClick();
          }
          else if ( dir === "right" && scope.rightArrowShow ) {
            scope.rightArrowClick();
          }
        };
        scope.inFullScreenMode = _isFullscreenActive();

        scope.fullScreen = function () {
          scope.inFullScreenMode = !scope.inFullScreenMode;

          if ( scope.inFullScreenMode ) {
            _enter($document.find("html")[0]);
          }
          else {
            _exit($document[0]);
          }
        };

        $document.on("webkitfullscreenchange mozfullscreenchange fullscreenchange", function () {
          if ( !_isFullscreenActive() ) {
            scope.$apply(function () {
              scope.inFullScreenMode = false;
            });
          }
        });

        scope.$on("flyInControls", function () {
          if ( scope.timeoutControls ) {
            $timeout.cancel(scope.timeoutControls);
            scope.timeoutControls = undefined;
          }

          elem.removeClass("hide-ppt-fly-in-controls");
          elem.addClass("ppt-fly-in-controls");

          scope.timeoutControls = $timeout(function () {
            elem.removeClass("ppt-fly-in-controls");
            elem.addClass("hide-ppt-fly-in-controls");

            scope.timeoutControls = undefined;
          }, 2500);
        });
      }
    };
  }]);
  function _isFullscreenActive() {
    return (document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement) !== null;
  }

  function _enter(elem) {
    if ( "requestFullscreen" in elem ) {
      elem.requestFullscreen();
    }
    else if ( "msRequestFullscreen" in elem ) {
      elem.msRequestFullscreen();
    }
    else if ( "mozRequestFullScreen" in elem ) {
      elem.mozRequestFullScreen();
    }
    else if ( "webkitRequestFullscreen" in elem ) {
      elem.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
  }

  function _exit(doc) {
    if ( "exitFullscreen" in doc ) {
      doc.exitFullscreen();
    }
    else if ( "mozCancelFullScreen" in doc ) {
      doc.mozCancelFullScreen();
    }
    else if ( "webkitExitFullscreen" in doc ) {
      doc.webkitExitFullscreen();
    }
    else if ( "msExitFullscreen" in doc ) {
      doc.msExitFullscreen();
    }
  }
})();