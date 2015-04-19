<?php


function insertion($list)
{
	//$var2 = count($list) - 1;
	for ($i = 1; $i <  count($list); $i++ )
	{
		$current = $list[$i];
		$position = $i;
		while($position > 0 && $list[$position-1] > $current)
		{
			$list[$position] = $list[$position-1];
			//$list[$position-1] = $current;
			$position = $position - 1;

		}
		$list[$position] = $current;
	}
	return $list;
}


$list = array(9,8,7,6,5,3,2);
$var = insertion($list);
var_dump($var);


?>