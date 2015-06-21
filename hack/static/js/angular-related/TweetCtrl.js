angular.module('app').
    controller('TweetCtrl', [
        '$scope', '$rootScope', '$location', '$http', '$timeout',
        function ($scope, $rootScope, $location, $http, $timeout) {
            $scope.tweet = function() {
              $http.post(
                  '/api/tweets',
                  $.param($scope.userTweet)
                ).
                success(function(data, status, headers, config) {
                  $location.path('/feed');
                }).
                error(function(data, status, headers, config) {
                  console.error(data);
                });
            };

            $scope.init = function () {
                $rootScope.userData.location = $location.path();
                $scope.userTweet = {
                    'username': $rootScope.userData.username,
                    'password': $rootScope.userData.password,
                    'data': '',
                };
            }
            $scope.init();
        }
    ]
);
