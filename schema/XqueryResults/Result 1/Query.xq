(: This query returns the new Tweets that we have obtained :)
/Tweets/Tweet[translate(created, "-:T", "") > translate("2021-01-21T00:00:00", "-:T", "")]