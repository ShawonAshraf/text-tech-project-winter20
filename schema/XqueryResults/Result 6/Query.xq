(: This query returns how much each HashTag has been mentioned :)
for $groupedHashTags in (
  for $x in /Tweets/Tweet/tokenize(text,'#')[position() = (2 to 1000)]
  for $hashtag in tokenize($x, ' ')[position() = (1)]
  return <result>{$hashtag}</result>
)
let $full := $groupedHashTags
group by $full
let $count := count($groupedHashTags)
order by $count descending
return <HashTag>
        <Tag>{$full}</Tag>
        <Count>{$count}</Count>
       </HashTag>