<?hh

require_once "$SIMPLE_HACK_REST_FRAMEWORK/db/models.hh";

class TwitterUserModel extends Model {
  protected string $table_name = 'twitter_user';
  protected array<string> $table_fields = array(
    'id',
    'username',
    'password',
  );
}

class TwitterTweetModel extends Model {
  protected string $table_name = 'twitter_tweet';
  protected array<string> $table_fields = array(
    'id',
    'data',
    'created',
    'user_id',
  );
}
