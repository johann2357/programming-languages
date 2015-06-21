<?hh

trait TwitterAuthUtils {
  abstract protected function getRequest();
  abstract protected function getModel($str);
  protected function auth() {
    $user = $this->getModel('User');
    $request = $this->getRequest();
    $usr = $request['username'];
    $pwd = $request['password'];
    return (! is_null(
      $user->get(
        array(
          'id', 'username'
        ), array(
          'WHERE' => "username='$usr' AND password='$pwd'"
        )
      )
    ));
  }
}
