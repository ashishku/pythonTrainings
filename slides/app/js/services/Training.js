/**
 * Created by ashish on 30/6/14.
 */

(function () {
  "use strict";

  /*global jsTraining*/
  jsTraining.factory("Training", ["TrainingsResources", "$location", function (TrainingsResources, $location) {
    var tId, training, currentSlide = 0, totalSlides = 0;

    function changeSlide() {
      var slide;
      if (currentSlide === 0) {
        $location.url("/training/" +  tId);
      }
      else if (currentSlide === 1) {
        $location.url("/training/" +  tId + "/" + "agenda");
      }
      else if(currentSlide < totalSlides) {
        slide = training.slides[currentSlide];
        $location.url("/training/" +  tId + "/" + slide.type + "/" + slide.id);
      }
    }

    return {
      isLoaded: function() {
        return !!tId;
      },
      fetchSlide: function(slide) {
        var i, s;

        for(i=0; i<training.slides.length; i++) {
          s = training.slides[i];
          if ( s.id === slide ) {
            currentSlide = i;
            break;
          }
        }

        return TrainingsResources.get({training: tId, slide: slide});
      },
      fetchTraining: function(trnId) {
        currentSlide = 0;
        tId = trnId;

        training = TrainingsResources.get({training: tId});

        totalSlides = training.$promise.then(function(data) {
          data.slides.unshift({id: "__agenda__", title: "Agenda"});
          data.slides.unshift({id: "__info__", title: "____"});

          totalSlides = data.slides.length;
        });

        return training;
      },
      hasNextSlide: function() {
        return currentSlide < totalSlides - 1;
      },
      hasPreviousSlide: function() {
        return currentSlide > 0;
      },
      nextSlide: function() {
        currentSlide++;
        changeSlide();
      },
      previousSlide: function() {
        currentSlide--;
        changeSlide();
      }
    };
  }]);
})();