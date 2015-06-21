<?hh

$ROOT_DIRECTORY = realpath($_SERVER['DOCUMENT_ROOT']). '/api';
$SIMPLE_HACK_REST_FRAMEWORK = $ROOT_DIRECTORY . '/simple-hack-rest-framework';

require_once 'app/application.hh';

function serve() {
  // Path to the app settings file
  $GLOBALS['settings'] = $GLOBALS['ROOT_DIRECTORY'] . '/app/settings.ini';

  // Requests from the same server don't have a HTTP_ORIGIN header
  if (!array_key_exists('HTTP_ORIGIN', $_SERVER)) {
    $_SERVER['HTTP_ORIGIN'] = $_SERVER['SERVER_NAME'];
  }

  try {
    $API = new ApplicationApi($_REQUEST['request'], $_SERVER['HTTP_ORIGIN']);
    echo $API->processAPI();
  } catch (Exception $e) {
    echo json_encode(Array('error' => $e->getMessage()));
  }
}

serve();
