angular.module('app').
    controller('SessionCtrl', [
        '$scope', '$rootScope', '$location', '$http', '$timeout',
        function ($scope, $rootScope, $location, $http, $timeout) {
            $scope.authenticate = function() {
              $http.post(
                  '/api/users/authenticate',
                  $.param({
                      username: $scope.userData.username,
                      password: $scope.userData.password
                  })
                ).
                success(function(data, status, headers, config) {
                    $scope.userData.isLoggedIn = data;
                    if (data) {
                        $scope.userData.error = '';
                        $location.path('/feed');
                    } else {
                        $scope.userData.error = 'The password or username are incorrect!';
                    }
                }).
                error(function(data, status, headers, config) {
                    console.error(data);
                });
            };

            $scope.init = function () {
                $rootScope.userData.location = $location.path();
                $scope.userData = $rootScope.userData;
            }
            $scope.init();
        }
    ]
);
