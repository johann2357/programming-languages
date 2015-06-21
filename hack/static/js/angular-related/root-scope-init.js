angular.module('app').
    run(['$rootScope', '$http',
        function ($rootScope, $http) {
            $rootScope.init = function () {
                $rootScope.userData = {
                    'location': 'feed',
                    'isLoggedIn': false,
                    'username': '',
                    'password': '',
                    'token': '',
                    'error': '',
                };
                $rootScope.tweets = [];
            };
            $rootScope.init();
        }
    ]);
