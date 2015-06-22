<?hh

require_once 'db.hh';

abstract class Model {

  protected string $table_name = '';
  protected array<string> $table_fields = array();
  private $db;

  public function __construct() {
    $this->db = new Db();
  }

  public function getTableName() {
    return $this->table_name;
  }

  private function _select_query($args, $kwargs=array()) {
    $fields = '';
    foreach ($args as $field) {
      if (in_array($field, $this->table_fields)) {
        $fields .= "`$this->table_name`.`$field`,";
      } else {
        $fields .= "$field,";
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
    return $query;
  }

  public function select($args, $kwargs=array()) {
    return $this->db->select(
      $this->_select_query($args, $kwargs)
    );
  }

  public function get($args, $kwargs=array()) {
    return $this->db->get(
      $this->_select_query($args, $kwargs)
    );
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
    return $this->db->query($query);
  }
}
