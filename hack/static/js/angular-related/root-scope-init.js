angular.module('app').
    run(['$rootScope',
        function ($rootScope) {
            $rootScope.tweets = [
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
                {
                    id: 1,
                    data: "lorem ipsum tweet lorem ipsum",
                    created: new Date(),
                    user_id: 10,
                },
            ];

        }
    ]);
