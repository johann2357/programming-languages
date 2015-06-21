angular.module('app').
    controller('FeedCtrl', [
        '$scope', '$rootScope', '$location', '$http', '$timeout',
        function ($scope, $rootScope, $location, $http, $timeout) {
            $scope.init = function () {
                $rootScope.userData.location = $location.path();
                $http.get('/api/feeds').
                  success(function(data, status, headers, config) {
                      $rootScope.tweets = data;
                  }).
                  error(function(data, status, headers, config) {
                      console.error(data);
                  });
            }
            $scope.init();
        }
    ]
);
