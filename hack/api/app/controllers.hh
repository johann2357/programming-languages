<?hh

trait TwitterUserController {
  abstract protected function getMethod();
  abstract protected function getModel($str);

  protected function users() {
    if ($this->getMethod() == 'GET') {
      $user = $this->getModel('User');
      // $user->insert(
      //   array(array(
      //     'username'=>'test',
      //     'password'=>'test1',
      //   ))
      // );
      return $user->select(
        array(
          'id', 'username'
        )
      );
      // return $user->select(
      //   array(
      //     'id', 'username'
      //   ), array(
      //     'WHERE'=>'id=1'
      //   )
      // );
    } else {
      return "Only accepts GET requests";
    }
  }
}

trait TwitterTweetController {
  abstract protected function getMethod();
  abstract protected function getModel($str);

  protected function tweets() {
    if ($this->getMethod() == 'GET') {
      $tweet = $this->getModel('Tweet');
      return $tweet->select(array(
        'id', 'user_id', 'data', 'created_at'
      ));
    } else {
      return "Only accepts GET requests";
    }
  }

}
