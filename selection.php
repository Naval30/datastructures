<?php
/*
	function selection($list)
	{

		$len = count($list);

		for ($i = 0; $i < $len; $i++)
		{
			$min = null;
			$minkey = null;
			for ($j=$i; $j < $len; $j++)
			{
				if ($min = null || $list[$j] < $min)
				{
					$min = $list[$j];
					$minkey = $j;
				}
			}
			$list[$minkey] = $list[$i];
       		$list[$i] = $min;			
		}
	}


	$list = array(7, 3, 5, 6, 8, 9, 2, 1, 4);
	$var = selection($list);
	var_dump($var);

*/
$arr = array(7, 3, 9, 6, 5, 1, 2, 0, 8, 4);
$sortedArr = selectionSort($arr);
var_dump($sortedArr);
 
function selectionSort(array $arr) {
    for ($i = 0; $i < count($arr); ++$i) {
        $min = null;
        $minKey = null;
        for($j = $i; $j < count($arr); ++$j) {
            if (null === $min || $arr[$j] < $min) {
                $minKey = $j;
                $min = $arr[$j];
            }
        }
        $arr[$minKey] = $arr[$i];
        $arr[$i] = $min;
    }
    return $arr;
}
?>