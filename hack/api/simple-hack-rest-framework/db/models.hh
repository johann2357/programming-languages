<?hh

require_once 'db.hh';

abstract class Model {

  protected $table_name = '';
  protected $table_fields = array();
  private $db;

  public function __construct() {
    $this->db = new Db();
  }

  public function select($args, $kwargs=array()) {
    $fields = '';
    foreach ($args as $field) {
      if (in_array($field, $this->table_fields)) {
        $fields .= "`$field`,";
      }
    }
    $fields = rtrim($fields, ",");
    if (empty($fields)) {
      return array();
    }

    $query = "SELECT $fields FROM `$this->table_name` ";

    if (!empty($kwargs)) {
      $query_conditions = '';
      foreach ($kwargs as $clause => $value) {
        $query_conditions .=  " $clause $value ";
      }
      $query .= $query_conditions;
    }
    return $this->db->select($query);
  }

  public function insert($args) {
    $columns = '';
    foreach ($this->table_fields as $col) {
      $columns .=  "`$col`,";
    }
    $columns = rtrim($columns, ",");

    $values = '';
    foreach ($args as $row) {
      $row_value = '(';
      foreach ($this->table_fields as $field) {
        if (isset($row[$field])) {
          $row_value .= $this->db->quote($row[$field]) . ',';
        } else {
          $row_value .= 'NULL,';
        }
      }
      $values .= rtrim($row_value, ",") . '),';
    }
    $values = rtrim($values, ",");
    $query = "INSERT INTO `$this->table_name` ($columns) VALUES $values" ;
    echo "$query";
    return $this->db->query($query);
  }
}
