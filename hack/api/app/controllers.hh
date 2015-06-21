<?hh

require_once 'utils.hh';

trait TwitterUserController {
  abstract protected function getMethod();
  abstract protected function hasArgs();
  abstract protected function getArgs();
  abstract protected function hasVerb();
  abstract protected function getVerb();
  abstract protected function getRequest();
  abstract protected function getModel($str);
  abstract protected function auth();

  protected function users() {
    if ($this->getMethod() == 'GET') {
      $user = $this->getModel('User');
      if ($this->hasArgs()) {
        $id = $this->getArgs()[0];
        return $user->select(
          array(
            'id', 'username'
          ), array(
            'WHERE' => "id='$id'"
          )
        );
      } else {
        return $user->select(
          array(
            'id', 'username'
          )
        );
      }
    } else if ($this->getMethod() == 'POST') {
      if ($this->hasVerb() && ($this->getVerb() == 'authenticate')) {
        return $this->auth();
      }
    }
  }
}

trait TwitterTweetController {
  abstract protected function getMethod();
  abstract protected function getRequest();
  abstract protected function hasVerb();
  abstract protected function getVerb();
  abstract protected function getModel($str);
  abstract protected function auth();

  protected function tweets() {
    $tweet = $this->getModel('Tweet');
    $user = $this->getModel('User');
    if ($this->getMethod() == 'GET') {
      return $tweet->select(
        array(
          'id', 'user_id', 'data', 'created'
        ), array (
          'ORDER BY'=>'created DESC',
        )
      );
    } else if ($this->getMethod() == 'POST') {
      if ($this->auth()) {
        $request = $this->getRequest();
        $usr = $request['username'];
        $usr_id = $user->get(
          array(
            'id',
          ), array(
            'WHERE' => "username='$usr'"
          )
        )['id'];
        $data = $request['data'];
        return $tweet->insert(
          array(array(
            'user_id'=>$usr_id,
            'data'=>$data,
          ))
        );
      }
    }
  }
}

trait TwitterFeedController {
  abstract protected function getMethod();
  abstract protected function hasVerb();
  abstract protected function getVerb();
  abstract protected function getModel($str);

  protected function feeds() {
    if ($this->getMethod() == 'GET') {
      $tweet = $this->getModel('Tweet');
      $tweetTbl = $tweet->getTableName();
      $userTbl = $this->getModel('User')->getTableName();
      return $tweet->select(
        array(
          'id', 'data', 'created', 'user_id', 'username'
        ), array (
          'RIGHT JOIN'=>$userTbl,
          'ON'=>"$userTbl.id=$tweetTbl.user_id",
          'ORDER BY'=>'created DESC',
        )
      );
    } else {
      return "Only accepts GET requests";
    }
  }
}

