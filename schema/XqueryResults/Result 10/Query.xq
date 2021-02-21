(: This query returns the number of Tweets on each user location and order them :)
for $x in /Tweets/Tweet
let $l := $x/userlocation
group by $l
let $count := count($x)
order by $count descending
return <Location>
          <Name>{$l}</Name>
          <Count>{$count}</Count>
       </Location>