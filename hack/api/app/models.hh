<?hh

require_once "$SIMPLE_HACK_REST_FRAMEWORK/db/models.hh";

class TwitterUserModel extends Model {
  protected $table_name = 'twitter_user';
  protected $table_fields = array(
    'id',
    'username',
    'password',
  );
}

class TwitterTweetModel extends Model {
  protected $table_name = 'twitter_tweet';
  protected $table_fields = array(
    'id',
    'data',
    'created',
    'user_id',
  );
}
