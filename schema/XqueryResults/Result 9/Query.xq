(: This query returns the Tweets that have the word 'bug' mentioned in the Tweet text :)
for $t in /Tweets/Tweet[contains(lower-case(text), 'bug')]
order by $t/retweetcount descending, $t/created descending
return <BugTweets>{$t}</BugTweets>