var app = angular.module("app", [
    'ngRoute',
]);

app.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/feed', {
                controller: 'FeedCtrl',
                templateUrl: 'partials/feed.html',
            }).
            when('/user-info', {
                controller: 'UserCtrl',
                templateUrl: 'partials/feed.html',
            }).
            when('/tweet', {
                controller: 'TweetCtrl',
                templateUrl: 'partials/tweet.html',
            }).
            when('/login', {
                controller: 'SessionCtrl',
                templateUrl: 'partials/login.html',
            }).
            when('/signup', {
                controller: 'SessionCtrl',
                templateUrl: 'partials/signup.html',
            }).
            when('/logout', {
                controller: 'SessionCtrl',
                templateUrl: 'partials/logout.html',
            }).
            otherwise({
                redirectTo: '/feed'
            });
    }]);
