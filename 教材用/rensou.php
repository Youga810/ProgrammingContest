<?php
$name_lst = array(); //一杯いれれる箱があります 配列
$name_lst[0] = 'John';
$name_lst[1] = 'Kate';
$name_lst[2] = 'Bob';

//foreach ($name_lst as $name) {
//  echo $name . ' ';
//}




//var_dump($name_lst);


$ryousuke_lst = array();
$ryousuke_lst[0] = 'ryousuke';
$ryousuke_lst[1] = 18;
$ryousuke_lst[2] = 'ラーメン';
//var_dump($ryousuke_lst);



$ryousukeRensouLst = array();
$ryousukeRensouLst = array('name' => 'ryousuke', 'age' => 18, 'favoriteFood' => 'ラーメン');

//echo $ryousuke_lst[1];
//echo $ryousukeRensouLst['age'];
//var_dump($ryousukeRensouLst);

foreach ($ryousukeRensouLst as $value) {
  echo $value;
}
