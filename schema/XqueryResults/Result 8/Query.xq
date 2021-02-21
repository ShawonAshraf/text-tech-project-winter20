(: This query returns the number of how many tweets have mentioned the word 'bug' in the Tweet text :)
let $c := count(/Tweets/Tweet[contains(lower-case(text), 'bug')])
return <BugTweetsCount>{$c}</BugTweetsCount>