(: This query returns the new Tweets order based on the retweet count :)
for $t in /Tweets/Tweet[translate(created, "-:T", "") 
> translate("2021-01-21T00:00:00", "-:T", "")]
let $x := xs:integer($t/retweetcount)
order by $x descending, $t/created descending
return <TweetAfterRelease>
	{$t/retweetcount}
    {$t/created}
    {$t/text}
	{$t/userlocation}
    </TweetAfterRelease>