<?php

	function bubble($list)
	{
		$exchange = true;
		$len = count($list) - 1;
		while ($exchange === true && $len > 0 )
		{
			$exchange = false;
			for ($i = 0; $i < $len; $i++)
			{
				
				if ($list[$i] > $list[$i+1])
				{
					$exchange = true;
					$var = $list[$i];
					$list[$i] = $list [$i+1];
					$list[$i+1] = $var;
					
				}

			}
			$len = $len - 1;
		}

		return $list;
	}



	$list = array(6,4,7,9,3,4,5);
	$var1 = bubble($list);
	var_dump($var1);