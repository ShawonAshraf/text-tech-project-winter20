(: This query returns the Tweets grouped by the user location :)
for $t in /Tweets/Tweet
let $g := $t/userlocation 
group by $g
order by $g
return <Location userlocation="{$g}">
        {for $i in $t
          let $x := xs:integer($i/retweetcount)
            order by $x descending, $i/created descending
          return <Tweet ID="{$i/@ID}">{$i/retweetcount}{$i/text}</Tweet>
        }
       </Location>