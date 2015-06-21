<?hh

require_once "$SIMPLE_HACK_REST_FRAMEWORK/rest.hh";

require_once 'models.hh';
require_once 'controllers.hh';

class TwitterApi extends RestApi
{
  use TwitterUserController;
  use TwitterTweetController;

  protected $models = array(
    'User'=>null,
    'Tweet'=>null,
  );

  public function __construct($request, $origin) {
    parent::__construct($request);
    $this->models['User'] = new TwitterUserModel();
    $this->models['Tweet'] = new TwitterTweetModel();
  }

  protected function getMethod() {
    return $this->method;
  }

  protected function getModel($model) {
    return $this->models[$model];
  }

}

$GLOBALS['settings'] = '.settings.ini';
class_alias('TwitterApi', 'ApplicationApi');
